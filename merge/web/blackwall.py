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
flow_name = "flow_black_%s"%(host_num)
eth_src = "00:00:00:00:00:0%s"%(host_num)

flow = {
    'switch':switch_num,
    "name":flow_name,
    "cookie":"0",
    "priority":"4000",
    "eth_src":eth_src,
    "active":"true",
    "actions":"drop"
    }

delete = {
    'name':flow_name
}

if(sys.argv[3] == "1"):
    pusher.set(flow)
else:
    pusher.remove("name",delete)
