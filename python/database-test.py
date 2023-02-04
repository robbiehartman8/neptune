from cassandra.cluster import Cluster

if __name__ == "__main__":
    cluster = Cluster(['0.0.0.0'],port=9042)
    session = cluster.connect('neptune',wait_for_all_pools=True)
    session.execute('USE neptune')
    rows = session.execute('SELECT * FROM identity')

    for row in rows:
        print(row)