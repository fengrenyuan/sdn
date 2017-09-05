#!/usr/bin/python
import os
import sys
import time

def getGraph():
    count = 0
    links = []
    nodes = []
    graph = open('../app/graph.txt')
    lines = graph.readlines()
    for line in lines:
        link = []
        line = line.strip('\n\r')
        if(count == 0):
            count += 1
        elif(count == 1):
            count += 1
        else:
            node = line.split(',')
            link.append(node[0])
            if(node[2] != ''):
                node[2] = node[2].rstrip(' ')
                mb = node[2].split(' ')
                for j in range(len(mb)):
                    link.append(mb[j])
            link.append(node[3])
            links.append(link)
    print links
    graph.close()
    result = {'nodes':[],'links':[]}
    for i in range(len(links)):
        node_src = {'type':'node','name':links[i][0]}
        node_dst = {'type':'node','name':links[i][len(links[i])-1]}
        if node_src not in result['nodes']:
            result['nodes'].append(node_src)
            nodes.append(links[i][0])
        for j in range(len(links[i])):
            if(j > 0 and j < (len(links[i])-1)):
                result['nodes'].append({'type':'box','name':links[i][j]})
                nodes.append(links[i][j])
        if node_dst not in result['nodes']:
            result['nodes'].append({'type':'node','name':links[i][len(links[i])-1]})
            nodes.append(links[i][len(links[i])-1])

    base_num = 0
    print nodes
    judges_src = []
    judges_dst = []
    for i in range(len(links)):
        for j in range(len(links[i])-1):
            if(j == 0):
                if(links[i][j] not in judges_src):
                    judges_src.append(links[i][j])
                    result['links'].append({'source':nodes.index(links[i][j]),'target':base_num+j+1})
                else:
                    base_num -= 1
                    result['links'].append({'source':nodes.index(links[i][j]),'target':base_num+j+1})
            elif(j == (len(links[i])-2)):
                if(links[i][j] not in judges_dst):
                    judges_dst.append(links[i][j])
                    result['links'].append({'source':base_num+j,'target':nodes.index(links[i][j+1])})
                else:
                    result['links'].append({'source':base_num+j,'target':nodes.index(links[i][j+1])})
                    base_num -= 1
            else:
                result['links'].append({'source':base_num+j,'target':base_num+j+1})
        base_num += len(links[i])
    return result
