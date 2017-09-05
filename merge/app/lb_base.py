import httplib
import json
import sys

class StaticFlowPusher(object):

    def __init__(self, server):
        self.server = server

    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])

    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200

    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200

    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret

pusher = StaticFlowPusher('127.0.0.1')

switch_num = "00:00:00:00:00:00:00:04"
flow_name1 = "flow_lb_base_1"
flow_name2 = "flow_lb_base_2"
eth_src = "00:00:00:00:00:05"
eth_dst = "00:00:00:00:00:06"

flow1 = {
    'switch':switch_num,
    "name":flow_name1,
    "cookie":"0",
    "priority":"1000",
    "eth_dst":eth_dst,
    "active":"true",
    "actions":"output=2"
    }

flow2 = {
    'switch':switch_num,
    "name":flow_name2,
    "cookie":"0",
    "priority":"1000",
    "eth_dst":eth_src,
    "active":"true",
    "actions":"output=1"
    }

delete1 = {
    'name':flow_name1
}

delete2 = {
    'name':flow_name2
}

if(sys.argv[1] == '1'):
    pusher.set(flow1)
    pusher.set(flow2)
else:
    pusher.remove('name',delete1)
    pusher.remove('name',delete2)
