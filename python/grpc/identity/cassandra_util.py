from cassandra.cluster import Cluster
import traceback

class CassandraUtil:

    def getConnection(self):
        try: 
            cluster = Cluster(['0.0.0.0'],port=9042)
            session = cluster.connect('neptune', wait_for_all_pools=True)
            return session
        except:
            traceback.print_exception()

    def getIdentityByHrID(self, session, hr_id):
        select_statement = session.prepare("SELECT * FROM neptune.identity WHERE hr_id = ?")
        try:
            rows = session.execute(select_statement, [hr_id])
            return rows
        except:
            traceback.print_exception()

    def insertIdentity(self, session, row):
        try:
            session.execute("INSERT INTO neptune.identity (hr_id, user_name, first_name, middle_name, last_name, job_title, location_number, location_name, manager_hr_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
        except:
            traceback.print_exception()