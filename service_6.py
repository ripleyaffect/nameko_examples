"""

    service_6
    ~~~~~~~~~

    Example of timer extension

"""

from random import choice

from nameko.timer import timer


class PingService(object):
    name = 'ping_service'

    @timer(interval=1)
    def ping(self):
        """Pings every second"""
        print choice(['SPAM', 'SPAM', 'EGG', 'BACON', 'SPAMMY SPAM'])
