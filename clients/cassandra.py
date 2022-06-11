from cassandra.cluster import Cluster


def get_cassandra_client(host, port, keyspace):
    cluster = Cluster([host], port=port)
    session = cluster.connect(keyspace, wait_for_all_pools=True)
    session.execute(f'USE {keyspace}')
    return session
