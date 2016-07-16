"""

    service_4
    ~~~~~~~~~

    Example of event publisher using rpc extension

"""

from nameko.events import EventDispatcher
from nameko.rpc import rpc


class MyEventPublisherService(object):
    name = 'my_event_publisher_service'

    dispatch = EventDispatcher()

    @rpc
    def publish(self, payload):
        """Publish an event with the passed payload

        :param payload: `str` payload to publish with the event

        """
        self.dispatch('my_event', payload)
