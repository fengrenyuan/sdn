import httplib
import json
import sys

def getTraffic(src):
    class StaticFlowPusher(object):

        def __init__(self, server):
            self.server = server

        def get(self, data):
            ret = self.rest_call({}, 'GET')
            return json.loads(ret[2])

        def set(    self, data):
            ret = self.rest_call(data, 'POST')
            return ret[0] == 200

        def remove(self, objtype, data):
            ret = self.rest_call(data, 'DELETE')
            return ret[0] == 200

        def rest_call(self, data, action):
            path = '/wm/core/switch/00:00:00:00:00:00:00:04/port/json'
            headers = {
               'Content-type': 'application/json',
                'Accept': 'application/json',
                }
            body = json.dumps(data)
            conn = httplib.HTTPConnection(self.server, 8080)
            conn.request(action, path, body, headers)
            response = conn.getresponse()
            ret = (response.status, response.reason, response.read())
            conn.close()
            return ret

    pusher = StaticFlowPusher('127.0.0.1')

    host_num = src
    result = pusher.get('')
    for i in range(len(result['port_reply'][0]['port'])):
        if(result['port_reply'][0]['port'][i]['port_number'] == host_num):
            traffic = result['port_reply'][0]['port'][i]['receive_bytes']
            return str((int(traffic)+0.1)/1024)
