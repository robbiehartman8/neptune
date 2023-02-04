from concurrent import futures
import grpc
import identity_pb2
import identity_pb2_grpc

class Identity(identity_pb2_grpc.IdentityServicer):

    # change to pickle
    def getUserDict():
        user_dict = {
            "12345": ["12345", "rxh82f6", "robert", "m", "hartman", "eng", 9999, "new york", "00001"]
        }
        return user_dict

    def getData(hr_id):
        user_dict = Identity.getUserDict()
        try:
            search_data = user_dict[hr_id]
            return search_data
        except:
            return None

    def getIdentity(self, request, context):
        data = Identity.getData(request.hr_id)
        if data:
            response_data = identity_pb2.iamData(hr_id = data[0], user_name = data[1], first_name = data[2], middle_name = data[3], last_name = data[4], job_title = data[5], location_number = data[6], location_name = data[7], manager_hr_id = data[8])
        else:
            response_data = identity_pb2.iamData(hr_id = None, user_name = None, first_name = None, middle_name = None, last_name = None, job_title = None, location_number = None, location_name = None, manager_hr_id = None)
        return response_data

    def enterIdentity(self, request, context):
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
