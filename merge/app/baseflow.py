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
switch1 = "00:00:00:00:00:00:00:01"
switch2 = "00:00:00:00:00:00:00:02"
switch3 = "00:00:00:00:00:00:00:03"
switch4 = "00:00:00:00:00:00:00:04"
host1 = "10.0.0.1/8"
host2 = "10.0.0.2/8"
host3 = "10.0.0.3/8"
dns = "10.0.0.4/8"
web1 = "10.0.0.5/8"
web2 = "10.0.0.6/8"

flow1 = {
    'switch':switch1,
    "name":"switch1_1",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_src":host1,
    "active":"true",
    "actions":"output=4"
    }

flow2 = {
    'switch':switch1,
    "name":"switch1_2",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_src":host2,
    "active":"true",
    "actions":"output=4"
    }

flow3 = {
    'switch':switch1,
    "name":"switch1_3",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_src":host3,
    "active":"true",
    "actions":"output=4"
    }

flow4 = {
    'switch':switch1,
    "name":"switch1_4",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":host1,
    "active":"true",
    "actions":"output=1"
    }

flow5 = {
    'switch':switch1,
    "name":"switch1_5",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":host2,
    "active":"true",
    "actions":"output=2"
    }

flow6 = {
    'switch':switch1,
    "name":"switch1_6",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":host3,
    "active":"true",
    "actions":"output=3"
    }

flow7 = {
    'switch':switch2,
    "name":"switch2_1",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":host1,
    "active":"true",
    "actions":"output=1"
    }

flow8 = {
    'switch':switch2,
    "name":"switch2_2",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":host2,
    "active":"true",
    "actions":"output=1"
    }

flow9 = {
    'switch':switch2,
    "name":"switch2_3",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":host3,
    "active":"true",
    "actions":"output=1"
    }

flow10 = {
    'switch':switch2,
    "name":"switch2_4",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":dns,
    "active":"true",
    "actions":"output=2"
    }

flow11 = {
    'switch':switch2,
    "name":"switch2_5",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":web1,
    "active":"true",
    "actions":"output=3"
    }

flow12 = {
    'switch':switch2,
    "name":"switch2_6",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":web2,
    "active":"true",
    "actions":"output=3"
    }

flow13 = {
    'switch':switch3,
    "name":"switch3_1",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":dns,
    "active":"true",
    "actions":"output=1"
    }
flow14 = {
    'switch':switch3,
    "name":"switch3_2",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_src":dns,
    "active":"true",
    "actions":"output=2"
    }

flow15 = {
    'switch':switch4,
    "name":"switch4_1",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":web1,
    "active":"true",
    "actions":"output=2"
    }

flow16 = {
    'switch':switch4,
    "name":"switch4_2",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_dst":web2,
    "active":"true",
    "actions":"output=2"
    }

flow17 = {
    'switch':switch4,
    "name":"switch4_3",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_src":web1,
    "active":"true",
    "actions":"output=3"
    }

flow18 = {
    'switch':switch4,
    "name":"switch4_4",
    "cookie":"0",
    "priority":"5",
    "eth_type":"0x0800",
    "ipv4_src":web2,
    "active":"true",
    "actions":"output=3"
    }

pusher.set(flow1)
pusher.set(flow2)
pusher.set(flow3)
pusher.set(flow4)
pusher.set(flow5)
pusher.set(flow6)
pusher.set(flow7)
pusher.set(flow8)
pusher.set(flow9)
pusher.set(flow10)
pusher.set(flow11)
pusher.set(flow12)
pusher.set(flow13)
pusher.set(flow14)
pusher.set(flow15)
pusher.set(flow16)
pusher.set(flow17)
pusher.set(flow18)
