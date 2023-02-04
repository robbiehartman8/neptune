from cassandra.cluster import Cluster






cluster = Cluster(['0.0.0.0'],port=9042)
session = cluster.connect('neptune',wait_for_all_pools=True)
row = [
    'lasdjfl',
    'gen',
    'lasdjfl',
    'lasdjfl',
    'lasdjfl',
    'lasdjfl',
    9999,
    'lasdjfl',
    'lasdjfl'
]
session.execute("INSERT INTO neptune.identity (hr_id, user_name, first_name, middle_name, last_name, job_title, location_number, location_name, manager_hr_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", row)