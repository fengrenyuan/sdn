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
dst_num = sys.argv[2][-1:]
switch_num = "00:00:00:00:00:00:00:01"
flow_name = "flow_port_%s"%(host_num)
ipv4_src = "10.0.0.%s"%(host_num)
ipv4_dst = "10.0.0.%s"%(dst_num)
port = sys.argv[3]

flow = {
    'switch':switch_num,
    "name":flow_name,
    "cookie":"0",
    "priority":"5000",
    "ipv4_src":ipv4_src,
    "ipv4_dst":ipv4_dst,
    "eth_type":"0x0800",
    "ip_proto":"0x06",
    "tcp_dst":port,
    "active":"true",
    "actions":"drop"
    }

delete = {
    'name':flow_name
}

if(sys.argv[4] == "1"):
    pusher.set(flow)
else:
    pusher.remove("name",delete)
