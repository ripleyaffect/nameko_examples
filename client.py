from nameko.standalone.rpc import ClusterRpcProxy

config = {
  'AMQP_URI': 'amqp://guest:guest@localhost',
}

with ClusterRpcProxy(config) as cluster_rpc:
    print cluster_rpc.expanded_greeter_service.greet("Tim the Enchanter")
