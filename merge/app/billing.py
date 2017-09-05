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

host_num = sys.argv[1][-1:]
switch_num = "00:00:00:00:00:00:00:0%s"%(sys.argv[2])
flow_name = "flow_bill_%s"%(host_num)
flow_name2 = "flow_lb_%s"%(host_num)
eth_src = "00:00:00:00:00:0%s"%(host_num)

if(sys.argv[2] == "1"):
    output1 = "output=4"
    output2 = "output=4"
elif(sys.argv[2] == "2"):
    output1 = "output=3"
    output2 = "output=3"
else:
    output1 = "output=1"
    output2 = "output=2"

flow = {
    'switch':switch_num,
    "name":flow_name,
    "cookie":"0",
    "priority":"3000",
    "eth_src":eth_src,
    "eth_dst":"00:00:00:00:00:05",
    "eth_type":"0x0800",
    "active":"true",
    "actions":output1
    }

flow2 = {
    'switch':switch_num,
    "name":flow_name2,
    "cookie":"0",
    "priority":"3000",
    "eth_src":eth_src,
    "eth_dst":"00:00:00:00:00:06",
    "eth_type":"0x0800",
    "active":"true",
    "actions":output2
    }

delete = {
    'name':flow_name
}

delete2 = {
    'name':flow_name2
}

if(sys.argv[3] == "1"):
    pusher.set(flow)
    pusher.set(flow2)
else:
    pusher.remove("name",delete)
    pusher.remove("name",delete2)
