from concurrent import futures
import grpc
import identity_pb2
import identity_pb2_grpc
from cassandra_util import CassandraUtil

class Identity(identity_pb2_grpc.IdentityServicer):

    def getIdentity(self, request, context):
        # TODO: query database for this value
        
        Cassandra = CassandraUtil()
        session = Cassandra.getConnection()
        rows = Cassandra.getIdentityByHrID(session, request.hr_id)

        for row in rows:
            response_data = identity_pb2.iamData(
                hr_id = row.hr_id, 
                user_name = row.user_name, 
                first_name = row.first_name, 
                middle_name = row.middle_name, 
                last_name = row.last_name, 
                job_title = row.job_title, 
                location_number = row.location_number, 
                location_name = row.location_name, 
                manager_hr_id = row.manager_hr_id
            )

        return response_data

    def enterIdentity(self, request, context):
        # TODO: enter data into the database 

        hr_id = request.hr_id
        user_name = 'gen'
        first_name = request.first_name
        middle_name = request.middle_name
        last_name = request.last_name
        job_title = request.job_title
        location_number = request.location_number
        location_name = request.location_name
        manager_hr_id = request.manager_hr_id

        if hr_id:
            response_data = identity_pb2.iamData(hr_id = hr_id, user_name = user_name, first_name = first_name, middle_name = middle_name, last_name = last_name, job_title = job_title, location_number = location_number, location_name = location_name, manager_hr_id = manager_hr_id)
        else:
            response_data = identity_pb2.iamData(hr_id = None, user_name = None, first_name = None, middle_name = None, last_name = None, job_title = None, location_number = None, location_name = None, manager_hr_id = None)
        return response_data

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    server()
