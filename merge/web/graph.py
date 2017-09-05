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
    judges = []
    graph = open('../app/graph.txt')
    lines = graph.readlines()
    for line in lines:
        line = line.strip('\n\r')
        if(count == 0):
            line = line.rstrip(' ')
            node = line.split(' ')
            for i in range(len(node)):
                srcs.append(node[i])
                if node[i] not in judges:
                    judges.append(node[i])
            count += 1
        elif(count == 1):
            line = line.rstrip(' ')
            node = line.split(' ')
            for i in range(len(node)):
                dsts.append(node[i])
                if node[i] not in judges:
                    judges.append(node[i])
            count += 1
        else:
            node = line.split(',')
            if(node[1] == ''):
                src = node[0]
                dst = node[3]
                if(node[2] != ''):
                    node[2] = node[2].rstrip(' ')
                mb = node[2].split(' ')
                for j in range(len(mb)):
                    if mb[j] not in boxes:
                        boxes.append(mb[j])
                    if mb[j] not in judges:
                        judges.append(mb[j])
                edges.append([src,mb,dst])
            else:
                src = node[0]
                dst = node[3]
                if(node[2] != ''):
                    node[2] = node[2].rstrip(' ')
                mb = node[2].split(' ')
                for j in range(len(mb)):
                    if mb[j] not in boxes:
                        boxes.append(mb[j])
                    if mb[j] not in boxes:
                        judges.append(mb[j])
                node[1] = node[1].rstrip(' ')
                port = node[1].split(' ')
                edges.append([src,mb,dst])
    graph.close()
    result = {'nodes':[],'links':[]}
    for i in range(len(srcs)):
        json_node = {'type':'node','name':srcs[i]}
        result['nodes'].append(json_node)
    for i in range(len(dsts)):
        json_node = {'type':'node','name':dsts[i]}
        result['nodes'].append(json_node)
    for i in range(len(boxes)):
        json_node = {'type':'box','name':boxes[i]}
        result['nodes'].append(json_node)

    print judges
    print 'hello'

    for i in range(len(edges)):
        print edges[i]
        print len(edges[i][1])
        if(len(edges[i][1]) == 0):
            json_link = {'source':judges.index(edges[i][0]),'target':judges.index(edges[i][2])}
        elif(len(edges[i][1]) == 1):
            json_link1 = {'source':judges.index(edges[i][0]),'target':judges.index(edges[i][1][0])}
            json_link2 = {'source':judges.index(edges[i][1][0]),'target':judges.index(edges[i][2])}
            result['links'].append(json_link1)
            result['links'].append(json_link2)
        elif(len(edges[i][1]) == 2):
            json_link1 = {'source':judges.index(edges[i][0]),'target':judges.index(edges[i][1][0])}
            json_link2 = {'source':judges.index(edges[i][1][0]),'target':judges.index(edges[i][1][1])}
            json_link3 = {'source':judges.index(edges[i][1][1]),'target':judges.index(edges[i][2])}
            result['links'].append(json_link1)
            result['links'].append(json_link2)
            result['links'].append(json_link3)
        else:
            json_link1 = {'source':judges.index(edges[i][0]),'target':judges.index(edges[i][1][0])}
            json_link2 = {'source':judges.index(edges[i][1][0]),'target':judges.index(edges[i][1][1])}
            json_link3 = {'source':judges.index(edges[i][1][1]),'target':judges.index(edges[i][1][2])}
            json_link4 = {'source':judges.index(edges[i][1][2]),'target':judges.index(edges[i][2])}
            result['links'].append(json_link1)
            result['links'].append(json_link2)
            result['links'].append(json_link3)
            result['links'].append(json_link4)
    return result
