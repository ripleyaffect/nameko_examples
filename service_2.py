"""

    service_2
    ~~~~~~~~~

    Example of rpc extension

"""

from nameko.rpc import rpc


class GreeterService(object):
    name = 'greeter_service'

    @rpc
    def greet(self, name):
        """Return a string greeting using the passed name

        :param name: `str` name of person to greet

        """
        return u'Hello {}!'.format(name)
