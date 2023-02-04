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