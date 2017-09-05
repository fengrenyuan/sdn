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
flow_name1 = "flow_load_%s"%(host_num)
flow_name2 = "flow_loadr_%s"%(host_num)
flow_name3 = "flow_loadd_%s"%(host_num)
eth_src = "00:00:00:00:00:0%s"%(host_num)
action1 = "set_ipv4_dst=10.0.0.7,set_eth_dst=00:00:00:00:00:07,output=3"
action2 = "set_ipv4_src=10.0.0.6,set_eth_src=00:00:00:00:00:06,output=1"

flow1 = {
    'switch':switch_num,
    "name":flow_name1,
    "cookie":"0",
    "priority":"2000",
    "eth_src":eth_src,
    "eth_type":"0x0800",
    "active":"true",
    "actions":action1
    }

flow2 = {
    'switch':switch_num,
    "name":flow_name2,
    "cookie":"0",
    "priority":"2000",
    "eth_src":"00:00:00:00:00:07",
    "eth_type":"0x0800",
    "active":"true",
    "actions":action2
    }

flow3 = {
    'switch':'00:00:00:00:00:00:00:04',
    "name":flow_name3,
    "cookie":"0",
    "priority":"2000",
    "eth_dst":"00:00:00:00:00:07",
    "active":"true",
    "actions":"output=2"
    }

delete1 = {
    'name':flow_name1
}

delete2 = {
    'name':flow_name2
}

delete3 = {
    'name':flow_name3
}

if(sys.argv[3] == "1"):
    pusher.set(flow1)
    pusher.set(flow2)
    pusher.set(flow3)
else:
    pusher.remove("name",delete1)
    pusher.remove("name",delete2)
    pusher.remove("name",delete3)
