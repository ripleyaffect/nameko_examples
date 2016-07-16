"""

    service_3
    ~~~~~~~~~

    Example of rpc extension with rpc proxy dependency

"""

from nameko.rpc import rpc, RpcProxy


class ExpandedGreeterService(object):
    name = 'expanded_greeter_service'

    greeter_service = RpcProxy('greeter_service')

    @rpc
    def greet(self, name):
        """Return an expanded string greeting using the passed name

        Expands on the standard greeting provided by the greeting_service

        :param name: `str` name of person to greet

        """
        return '{} Welcome to Pygotham!'.format(
            self.greeter_service.greet(name))

