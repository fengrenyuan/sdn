import httplib
import json
  
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
  
flow1 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_1",
    "cookie":"0",
    "priority":"2000",
    "eth_dst":"00:00:00:00:00:04",
    "active":"true",
    "actions":"output=4"
    }

flow2 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_2",
    "cookie":"0",
    "priority":"1000",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.1/8",
    "active":"true",
    "actions":"output=5"
    }

flow3 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_3",
    "cookie":"0",
    "priority":"1000",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.2/8",
    "active":"true",
    "actions":"output=5"
    }

flow4 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_4",
    "cookie":"0",
    "priority":"1000",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.3/8",
    "active":"true",
    "actions":"output=5"
    }

flow5 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_5",
    "cookie":"0",
    "priority":"1000",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.1/8",
    "active":"true",
    "actions":"output=3"
    }
  
flow6 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_6",
    "cookie":"0",
    "priority":"1000",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.2/8",
    "active":"true",
    "actions":"output=3"
    }

flow7 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_7",
    "cookie":"0",
    "priority":"1000",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.3/8",
    "active":"true",
    "actions":"output=3"
    }

#flow8 = {
#    'switch':"00:00:00:00:00:00:00:01",
#    "name":"flow_mod_8",
#    "cookie":"0",
#    "priority":"2000",
#    "in_port":"4",
#    "active":"true",
#    "actions":"output=3"
#    }

pusher.set(flow1)
pusher.set(flow2)
pusher.set(flow3)
pusher.set(flow4)
pusher.set(flow5)
pusher.set(flow6)
pusher.set(flow7)
