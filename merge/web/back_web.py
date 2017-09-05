#!/usr/bin/python
from flask import Flask
from flask import request
from traffic import *
from counting import *
from addport import *
import os
import json
import sys

app = Flask(__name__)

@app.route('/firewall', methods = ['GET','POST'])
def firewall():
    host = request.form['ip']
    switch = request.form['type']
    if(switch == 'allow'):
        os.system('python ~/merge/app/blackwall.py '+host+' 1 0')
        os.system('python ~/merge/app/whitewall.py '+host+' 1 1')
    else:
        os.system('python ~/merge/app/whitewall.py '+host+' 1 0')
        os.system('python ~/merge/app/blackwall.py '+host+' 1 1')
        return "Firewall"

@app.route('/path', methods = ['GET','POST'])
def path():
    count = 0
    lb_on = [0,0]
    lb_file = open('lb.txt')
    lines = lb_file.readlines()
    for line in lines:
        line = line.strip('\n')
        if(count == 0):
            if(line == 1):
                lb_on[0] = 1
        else:
            if(line == 1):
                lb_on[1] = 1
    lb_file.close()
    nodes = []
    links = []
    src = request.form['src'] #seq 1 2 3
    dst = request.form['dst'] # 4 5
    if(src == '0' and dst == '7'):
        nodes = [1,4,5,6,8]
        links = [1,4,5,7]
    elif(src == '1' and dst == '7'):
        nodes = [2,4,5,6,8]
        links = [2,4,5,7]
    elif(src == '2' and dst == '7'):
        nodes = [3,4,5,6,8]
        links = [3,4,5,7]
    elif(src == '0' and dst == '8'):
        if(lb_on[0] == 1 and lb_on[1] == 1):
            nodes = [1,4,5,7,10]
            links = [1,4,6,9]
        else:
            nodes = [1,4,5,7,9]
            links = [1,4,6,8]
    elif(src == '0' and dst == '8'):
        if(lb_on[0] == 1 and lb_on[1] == 1):
            nodes = [1,4,5,7,10]
            links = [1,4,6,9]
        else:
            nodes = [1,4,5,7,9]
            links = [1,4,6,8]
    elif(src == '1' and dst == '8'):
        if(lb_on[0] == 1 and lb_on[1] == 1):
            nodes = [2,4,5,7,10]
            links = [2,4,6,9]
        else:
            nodes = [2,4,5,7,9]
            links = [2,4,6,8]
    elif(src == '2' and dst == '8'):
        nodes = [3,4,5,7,9]
        links = [3,4,6,8]
    result = {'nodes':nodes,'links':links}
    print result
    return  json.dumps(result)

@app.route('/flow', methods = ['GET','POST'])
def flow():
    count = 0
    lb_on = [0,0]
    lb_file = open('lb.txt')
    lines = lb_file.readlines()
    for line in lines:
        line = line.strip('\n')
        if(count == 0):
            if(line == '1'):
                lb_on[0] = 1
        else:
            if(line == '1'):
                lb_on[1] = 1
    lb_file.close()
    src = request.form['src'] #
    dst = request.form['dst'] #
    src_fin = str(int(src)+1)
    num = getTraffic(src_fin)
    result = {'flow':num}
    print result
    return json.dumps(result)

@app.route('/fee', methods = ['GET','POST'])
def fee():
    bill_file = open('bill.txt')
    lines = bill_file.readlines()
    for line in lines:
        switch = line
    print switch
    bill_file.close()
    result = getBill(switch)
    print 'switch'
    print switch
    return json.dumps(result)

@app.route('/module_state', methods = ['GET','POST'])
def module_state():
    module = request.form['module'] #Firewall Balance Billing
    state = request.form['state'] # 1 0
    if(module == 'Firewall' and state == '1'):
        os.system('python ~/merge/app/whitewall.py 10.0.0.1 2 1')
        os.system('python ~/merge/app/whitewall.py 10.0.0.2 2 1')
        os.system('python ~/merge/app/whitewall.py 10.0.0.3 2 1')
    elif(module == 'Firewall' and state == '0'):
        os.system('python ~/merge/app/whitewall.py 10.0.0.1 2 0')
        os.system('python ~/merge/app/whitewall.py 10.0.0.2 2 0')
        os.system('python ~/merge/app/whitewall.py 10.0.0.3 2 0')
    elif(module == 'Balance' and state == '1'):
        os.system('python ~/merge/app/lb_base.py 1')
        lb_file = open('./lb.txt','w')
        lb_file.write('1\n')
        lb_file.write('0')
        lb_file.close()
    elif(module == 'Balance' and state == '0'):
        os.system('python ~/merge/app/lb_base.py 0')
        lb_file = open('./lb.txt','w')
        lb_file.write('0\n')
        lb_file.write('0')
        print "hello"
        lb_file.close()
    elif(module == 'Billing' and state == '1'):
        bill_file = open('bill.txt','w')
        bill_file.write('2')
        bill_file.close()
        os.system('python ~/merge/app/billing.py 10.0.0.1 2 1')
        os.system('python ~/merge/app/billing.py 10.0.0.2 2 1')
    elif(module == 'Billing' and state == '0'):
        os.system('python ~/merge/app/billing.py 10.0.0.1 2 0')
        os.system('python ~/merge/app/billing.py 10.0.0.2 2 0')
    else:
        return 'no'
    return 'no'

@app.route('/modules', methods = ['GET','POST'])
def route():
    os.system('python ~/merge/app/clear.py')
    boxes = [0,0,0]
    module = []
    data = request.form #string array
    for i in range(len(data)):
        modules = data.getlist('module['+str(i)+']')
        module.append(modules)
    for i in range(len(module)):
        if(module[i][0] == 'Firewall'):
            boxes[2] = 1
        elif(module[i][0] == 'Balance'):
            boxes[1] = 1
        else:
            boxes[0] = 1
    pga_file = open('../app/module.txt','w')
    print "there"
    pga_file.write(str(boxes[0]))
    pga_file.write('\n')
    pga_file.write(str(boxes[1]))
    pga_file.write('\n')
    pga_file.write(str(boxes[2]))
    pga_file.close()
    print "hello"
    os.system('java -jar ~/merge/app/PGA.jar')
    os.system('python ~/merge/app/merge.py')
    result = getGraph()
    print result
    return json.dumps(result) #{nodes:[{type:node,name:Stu},{type:not_node,name:FW}]
            #links:[{source:Stu,target:WN}]}

if __name__ == '__main__':
	app.run(debug=True)
