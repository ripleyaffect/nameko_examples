"""

    service_1
    ~~~~~~~~~

    Example of http GET extension

"""

import json
from nameko.web.handlers import http


class HttpService(object):
    name = "multiply_service"

    @http('GET', '/multiply/<int:first>/<int:second>')
    def get_method(self, request, first, second):
        third = int(request.args.get('third', 1))
        return json.dumps({'value': first * second * third})
