"""

    service_5
    ~~~~~~~~~

    Example of event handler extension

"""

from nameko.events import event_handler


class MyEventHandlerServiceOne(object):
    name = 'my_event_handler_service_1'

    @event_handler('my_event_publisher_service', 'my_event')
    def publish(self, payload):
        """Handle a "my_event" payload

        :param payload: `str` payload to handle

        """
        print 'Recieved an event: {}'.format(payload)


class MyEventHandlerServiceTwo(object):
    name = 'my_event_handler_service_2'

    @event_handler('my_event_publisher_service', 'my_event')
    def publish(self, payload):
        """Also handle a "my_event" payload

        :param payload: `str` payload to handle

        """
        print 'Also recieved an event: {}'.format(payload)
