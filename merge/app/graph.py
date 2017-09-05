#!/usr/bin/python
import os
import sys
import time

def getGraph():
    count = 0
    srcs = []
    dsts = []
    edges = []
    boxes = []
    graph = open('../app/graph.txt')
    lines = graph.readlines()
    for line in lines:
        line = line.strip('\n')
        if(count == 0):
            node = line.split(',')
            for i in range(len(node)):
                srcs.append(node[i])
            count += 1
        elif(count == 1):
            node = line.split(',')
            for i in range(len(node)):
                dsts.append(node[i])
            count += 1
        else:
            node = line.split(',')
            if(len(node) == 3):
                src = node[0]
                dst = node[2]
                mb = node[1].split(' ')
                for j in range(len(mb)):
                    if mb[j] not in boxes:
                        boxes.append(mb[j])
                edges.append([src,mb,dst])
            else:
                src = node[0]
                dst = node[3]
                mb = node[2].split(' ')
                if mb[j] not in boxes:
                    boxes.append(mb[j])
                port = node[1].split(' ')
                edges.append([src,mb,dst])
    graph.close()
    result = {'nodes':[],'links':[]}
    for i in range(len(srcs)):
        json_node = {'type':'node','name':srcs[i]}
        result['node'].append(json_node)
    for i in range(len(dsts)):
        json_node = {'type':'node','name':dsts[i]}
        result['node'].append(json_node)
    for i in range(len(boxes)):
        json_node = {'type':'box','name':boxes[i]}
        result['node'].append(json_node)

    for i in range(len(edges)):
        if(len(edges[i][1]) == 1):
            json_link1 = {'source':edges[i][0],'target':edges[i][1][0]}
            json_link2 = {'source':edges[i][1][0],'target':edges[i][2]}
            result['links'].append(json_link1)
            result['links'].append(json_link2)
        elif(len(edges[1]) == 2):
            json_link1 = {'source':edges[i][0],'target':edges[i][1][0]}
            json_link2 = {'source':edges[i][1][0],'target':edges[i][1][1]}
            json_link3 = {'source':edges[i][1][1],'target':edges[i][2]}
            result['links'].append(json_link1)
            result['links'].append(json_link2)
            result['links'].append(json_link3)
        else:
            json_link1 = {'source':edges[i][0],'target':edges[i][1][0]}
            json_link2 = {'source':edges[i][1][0],'target':edges[i][1][1]}
            json_link3 = {'source':edges[i][1][1],'target':edges[i][1][2]}
            json_link4 = {'source':edges[i][1][2],'target':edges[i][2]}
            result['links'].append(json_link1)
            result['links'].append(json_link2)
            result['links'].append(json_link3)
            result['links'].append(json_link4)
    return result
