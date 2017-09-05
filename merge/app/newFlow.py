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
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow_mod_1",
    "cookie":"0",
    "priority":"2000",
    "eth_dst":"00:00:00:00:00:03",
    "active":"true",
    "actions":"drop"
    }

flow2 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow_mod_2",
    "cookie":"0",
    "priority":"2000",
    "eth_src":"00:00:00:00:00:03",
    "active":"true",
    "actions":"drop"
    }

flow3 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_3",
    "cookie":"0",
    "priority":"2000",
    "eth_src":"00:00:00:00:00:01",
    "active":"true",
    "actions":"output=4"
    }

flow4 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_4",
    "cookie":"0",
    "priority":"2000",
    "eth_src":"00:00:00:00:00:02",
    "active":"true",
    "actions":"output=4"
    }

flow5 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_5",
    "cookie":"0",
    "priority":"3000",
    "eth_type":"0x0800",
    "ip_proto":"0x06",
    "tcp_dst":"22",
    "eth_src":"00:00:00:00:00:01",
    "active":"true",
    "actions":"drop"
    }

flow6 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow_mod_6",
    "cookie":"0",
    "priority":"3000",
    "eth_type":"0x0800",
    "ip_proto":"0x06",
    "tcp_dst":"22",
    "eth_src":"00:00:00:00:00:02",
    "active":"true",
    "actions":"drop"
    }

pusher.set(flow1)
pusher.set(flow2)
pusher.set(flow3)
pusher.set(flow4)
pusher.set(flow5)
pusher.set(flow6)
