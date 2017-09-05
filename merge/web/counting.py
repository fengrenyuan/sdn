import httplib
import json
import sys

def getBill(switch_num):
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
    h1_web1 = 0
    h1_web2 = 0
    h2_web1 = 0
    h2_web2 = 0
    eth_src1 = "00:00:00:00:00:01"
    eth_src2 = "00:00:00:00:00:02"
    eth_dst1 = "00:00:00:00:00:05"
    eth_dst2 = "00:00:00:00:00:06"
    switch = "00:00:00:00:00:00:00:0%s"%(switch_num)

    result = pusher.get(data)
    for i in range(len(result[switch]["flows"])):
        if(result[switch]["flows"][i]["priority"] == "3000" and result[switch]["flows"][i]["match"]["eth_src"]==eth_src1 and result[switch]["flows"][i]["match"]["eth_dst"]==eth_dst1):
            h1_web1 = int(result[switch]["flows"][i]["byte_count"])
        if(result[switch]["flows"][i]["priority"] == "3000" and result[switch]["flows"][i]["match"]["eth_src"]==eth_src1 and result[switch]["flows"][i]["match"]["eth_dst"]==eth_dst2):
            h1_web2 = int(result[switch]["flows"][i]["byte_count"])
        if(result[switch]["flows"][i]["priority"] == "3000" and result[switch]["flows"][i]["match"]["eth_src"]==eth_src2 and result[switch]["flows"][i]["match"]["eth_dst"]==eth_dst1):
            h2_web1 = int(result[switch]["flows"][i]["byte_count"])
        if(result[switch]["flows"][i]["priority"] == "3000" and result[switch]["flows"][i]["match"]["eth_src"]==eth_src2 and result[switch]["flows"][i]["match"]["eth_dst"]==eth_dst2):
            h2_web2 = int(result[switch]["flows"][i]["byte_count"])
    if(h1_web1 != 0):
        h1_web1 = (h1_web1+0.1)/1000
    if(h1_web2 != 0):
        h1_web2 = (h1_web2+0.1)/1000
    if(h2_web1 != 0):
        h2_web1 = (h2_web1+0.1)/1000
    if(h2_web2 != 0):
        h2_web2 = (h2_web2+0.1)/1000
    return [h1_web1,h2_web1,h1_web2,h2_web2]
