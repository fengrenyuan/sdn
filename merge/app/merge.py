#!/usr/bin/python
import os
import sys
import time

count = 0
srcs = []
dsts = []
edges = []
graph = open('/home/controller/merge/app/graph.txt')
lines = graph.readlines()
for line in lines:
    line = line.strip('\n\r')
    if(count == 0):
        line = line.rstrip(' ')
        node = line.split(' ')
        for i in range(len(node)):
            srcs.append(node[i])
        count += 1
    elif(count == 1):
        line = line.rstrip(' ')
        node = line.split(' ')
        for i in range(len(node)):
            dsts.append(node[i])
        count += 1
    else:
        node = line.split(',')
        if(node[1] == ''):
            src = node[0]
            dst = node[3]
            if(node[2] != ''):
                node[2] = node[2].rstrip(' ')
            mb = node[2].split(' ')
            edges.append([src,mb,dst])
        else:
            src = node[0]
            dst = node[3]
            if(node[2] != ''):
                node[2] = node[2].rstrip(' ')
            mb = node[2].split(' ')
            node[1] = node[1].rstrip(' ')
            port = node[1].split(' ')
            edges.append([src,port,mb,dst])
graph.close()
print srcs
print dsts
print edges
route = '/home/controller/merge/app/'

for i in range(len(edges)):
	if(len(edges[i]) == 3):
		if(edges[i][0] == 'SA'):
			for j in range(len(edges[i][1])):
				if(edges[i][1][j] == 'FW'):
					os.system('python '+route+'whitewall.py 10.0.0.1 '+str(j+1)+' 1')
					os.system('python '+route+'whitewall.py 10.0.0.2 '+str(j+1)+' 1')
		                elif(edges[i][1][j] == 'LB'):
                    			os.system('python lb_base.py 1')
                    			lb_file = open('../web/lb.txt','w')
                    			lb_file.write('1\n')
                    			lb_file.write('0')
                    			lb_file.close()
                		else:
                    			bill_file = open('../web/bill.txt','w')
                    			bill_file.write('4')
                    			bill_file.close()
                    			os.system('python '+route+'billing.py 10.0.0.1 4 1')
                    			os.system('python '+route+'billing.py 10.0.0.2 4 1')
        	elif(edges[i][0] == 'TB'):
        		for j in range(len(edges[i][1])):
        	        	if(edges[i][1][j] == 'FW'):
                    			os.system('python '+route+'whitewall.py 10.0.0.3 '+str(j+1)+' 1')
                		elif(edges[i][1][j] == 'LB'):
                    			os.system('python ./lb_base.py 1')
                    			lb_file = open('../web/lb.txt','w')
                    			lb_file.write('1\n')
                    			lb_file.write('0')
                    			lb_file.close()
                		else:
                    			bill_file = open('../web/bill.txt','w')
                    			bill_file.write('4')
                    			bill_file.close()
                    			os.system('python '+route+'billing.py 10.0.0.3 4 1')
        	elif(edges[i][0] == 'Stu'):
        		for j in range(len(edges[i][1])):
                		if(edges[i][1][j] == 'FW'):
                	    		os.system('python '+route+'whitewall.py 10.0.0.1 '+str(j+1)+' 1')
                	    		os.system('python '+route+'whitewall.py 10.0.0.2 '+str(j+1)+' 1')
                		elif(edges[i][1][j] == 'LB'):
                	    		os.system('python ./lb_base.py 1')
                	    		lb_file = open('../web/lb.txt','w')
                	    		lb_file.write('1\n')
                	    		lb_file.write('0')
                	    		lb_file.close()
                		else:
                	    		bill_file = open('../web/bill.txt','w')
                	    		bill_file.write('4')
                	    		bill_file.close()
                	    		os.system('python '+route+'billing.py 10.0.0.1 4 1')
                	    		os.system('python '+route+'billing.py 10.0.0.2 4 1')
        	else:
        		for j in range(len(edges[i][1])):
                		if(edges[i][1][j] == 'FW'):
                	    		os.system('python '+route+'whitewall.py 10.0.0.3 '+str(j+1)+' 1')
                		elif(edges[i][1][j] == 'LB'):
                	    		os.system('python ./lb_base.py 1')
                	    		lb_file = open('../web/lb.txt','w')
                	    		lb_file.write('1\n')
                	    		lb_file.write('0')
                	    		lb_file.close()
				else:
					os.system('python '+route+'billing.py 10.0.0.3 4 1')
	else:
        	all_ports = ["22","23","80","5900"]
        	for j in range(len(edges[i][1])):
			all_ports.remove(edges[i][1][j])

        	if(edges[i][0] == 'SA' and edges[i][3] == 'WN'):
			for k in range(len(all_ports)):
				os.system('python '+route+'port.py 10.0.0.1 10.0.0.5 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.2 10.0.0.5 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.1 10.0.0.6 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.1 10.0.0.6 '+all_ports[k]+' 1')
		elif(edges[i][0] == 'SA' and edges[i][3] == 'DN'):
			for k in range(len(all_ports)):
				os.system('python '+route+'port.py 10.0.0.1 10.0.0.4 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.2 10.0.0.4 '+all_ports[k]+' 1')
		elif(edges[i][0] == 'TB' and edges[i][3] == 'WN'):
			for k in range(len(all_ports)):
				os.system('python '+route+'port.py 10.0.0.3 10.0.0.5 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.3 10.0.0.6 '+all_ports[k]+' 1')
		elif(edges[i][0] == 'TB' and edges[i][3] == 'DN'):
			for k in range(len(all_ports)):
				os.system('python '+route+'port.py 10.0.0.3 10.0.0.4 '+all_ports[k]+' 1')
		elif(edges[i][0] == 'Stu' and edges[i][3] == 'Web'):
			for k in range(len(all_ports)):
				os.system('python '+route+'port.py 10.0.0.1 10.0.0.5 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.2 10.0.0.5 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.1 10.0.0.6 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.1 10.0.0.6 '+all_ports[k]+' 1')
		elif(edges[i][0] == 'Stu' and edges[i][3] == 'DB'):
			for k in range(len(all_ports)):
				os.system('python '+route+'port.py 10.0.0.1 10.0.0.4 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.2 10.0.0.4 '+all_ports[k]+' 1')
		elif(edges[i][0] == 'Teac' and edges[i][3] == 'Web'):
			for k in range(len(all_ports)):
				os.system('python '+route+'port.py 10.0.0.3 10.0.0.5 '+all_ports[k]+' 1')
				os.system('python '+route+'port.py 10.0.0.3 10.0.0.6 '+all_ports[k]+' 1')
		else:
			for k in range(len(all_ports)):
				os.system('python '+route+'port.py 10.0.0.3 10.0.0.4 '+all_ports[k]+' 1')

		if(edges[i][0] == 'SA'):
			for j in range(len(edges[i][2])):
				if(edges[i][2][j] == 'FW'):
					os.system('python '+route+'whitewall.py 10.0.0.1 '+str(j+1)+' 1')
					os.system('python '+route+'whitewall.py 10.0.0.2 '+str(j+1)+' 1')
				elif(edges[i][2][j] == 'LB'):
					os.system('python ./lb_base.py 1')
                    			lb_file = open('../web/lb.txt','w')
                    			lb_file.write('1\n')
                    			lb_file.write('0')
                    			lb_file.close()
				else:
                    			bill_file = open('../web/bill.txt','w')
                    			bill_file.write('4')
                    			bill_file.close()
					os.system('python '+route+'billing.py 10.0.0.1 4 1')
					os.system('python '+route+'billing.py 10.0.0.2 4 1')
		elif(edges[i][0] == 'TB'):
			for j in range(len(edges[i][2])):
				if(edges[i][2][j] == 'FW'):
					os.system('python '+route+'whitewall.py 10.0.0.3 '+str(j+1)+' 1')
				elif(edges[i][2][j] == 'LB'):
                    			os.system('python ./lb_base.py 1')
                    			lb_file = open('../web/lb.txt','w')
                    			lb_file.write('1\n')
                    			lb_file.write('0')
                    			lb_file.close()
				else:
                    			bill_file = open('../web/bill.txt','w')
                    			bill_file.write('4')
                    			bill_file.close()
					os.system('python '+route+'billing.py 10.0.0.3 4 1')
		elif(edges[i][0] == 'Stu'):
			for j in range(len(edges[i][2])):
				if(edges[i][2][j] == 'FW'):
					os.system('python '+route+'whitewall.py 10.0.0.1 '+str(j+1)+' 1')
					os.system('python '+route+'whitewall.py 10.0.0.2 '+str(j+1)+' 1')
				elif(edges[i][2][j] == 'LB'):
                    			os.system('python ./lb_base.py 1')
                    			lb_file = open('../web/lb.txt','w')
                    			lb_file.write('1\n')
                    			lb_file.write('0')
                    			lb_file.close()
				else:
                    			bill_file = open('../web/bill.txt','w')
                    			bill_file.write('4')
                    			bill_file.close()
					os.system('python '+route+'billing.py 10.0.0.1 4 1')
					os.system('python '+route+'billing.py 10.0.0.2 4 1')
		else:
			for j in range(len(edges[i][2])):
				if(edges[i][2][j] == 'FW'):
					os.system('python '+route+'whitewall.py 10.0.0.3 '+str(j+1)+' 1')
				elif(edges[i][2][j] == 'LB'):
                    			os.system('python ./lb_base.py 1')
                    			lb_file = open('../web/lb.txt','w')
                    			lb_file.write('1\n')
                    			lb_file.write('0')
                    			lb_file.close()
				else:
                    			bill_file = open('../web/bill.txt','w')
                    			bill_file.write('4')
                    			bill_file.close()
					os.system('python '+route+'billing.py 10.0.0.3 4 1')
