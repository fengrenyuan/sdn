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
        path = '/wm/core/switch/all/flow/json'
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

data = ''
src = sys.argv[1]
dst = sys.argv[2]
switch = "00:00:00:00:00:00:00:02"

result = pusher.get(data)
if(len(result[switch]["flows"]) > 0):
	check = 1
else:
	check = 0
if(src == "host1" and dst == "web"):
	if(check == 1):
		route = (1,1,2,2)
	else:
		route = (1,1,2,1)
elif(src == "host1" and dst == "db"):
	route = (1,1,2,3)
elif(src == "host1" and dst == "dns"):
	route = (1,1,1,1)
elif(src == "host2" and dst == "web"):
	if(check == 1):
		route = (2,1,2,2)
	else:
		route = (2,1,2,1)
elif(src == "host2" and dst == "db"):
	route = (2,1,2,3)
elif(src == "host2" and dst == "dns"):
	route = (2,1,1,1)
elif(src == "host3" and dst == "web"):
	if(check == 1):
		route = (3,1,2,2)
	else:
		route = (3,1,2,1)
elif(src == "host3" and dst == "db"):
	route = (3,1,2,3)
elif(src == "host3" and dst == "dns"):
	route = (3,1,1,1)
else:
	route = (0,0,0,0)

print route
