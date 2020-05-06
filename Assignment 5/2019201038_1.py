#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:12:02 2020

@author: kishor
"""
import sys
disk_variable={}
t_var={}
memory_variable={}
tran_len={}
tran={}
i=0
t_no=""
order=list()
done={}
start_t={}
temp_v={}
output_file=open("2019201038_1.txt","w")
def print_(m):
    temp=""
    var_=None
    if m=='m':
        var_=memory_variable
    else:
        var_=disk_variable
    for i in sorted(var_):
        temp=temp+i+" "+str(var_[i])+" "
    temp=temp[:-1]
    temp+="\n"
    output_file.write(temp)
def undo(number,x):
    t_no=order[number]
    start=None
    end=None
    inst=tran[t_no]
    start=start_t[t_no]
    end=start_t[t_no]+x
    start_t[t_no]+=x
    if end >= tran_len[t_no]:
        end=tran_len[t_no]
        done[t_no]=True
    inst=inst[start:end]
    if start==0:
        output_file.write("<START "+t_no+">"+"\n")
        print_('m')
        print_('d')
    for i in inst:
        i=i.replace(" ","")
        m=i.split("(")
        if m[0]=='READ':
            var=i[i.find("(")+1:i.find(",")]
            temp_var=i[i.find(",")+1:i.find(")")]
            if var in temp_v:
                t_var[temp_var]=memory_variable[var]
                temp_v[var]=temp_var
            else:
                temp_v[var]=temp_var
                t_var[temp_var]=disk_variable[var]
                memory_variable[var]=t_var[temp_var]
        elif m[0]=='WRITE':
            var=i[i.find("(")+1:i.find(",")]
            temp_var=i[i.find(",")+1:i.find(")")]
            output_file.write("<"+t_no+", "+var+", "+str(memory_variable[var])+">\n")
            memory_variable[var]=t_var[temp_var]
            print_('m')
            print_('d')
        elif m[0]=='OUTPUT':
             var=i[i.find("(")+1:i.find(")")]
             disk_variable[var]=memory_variable[var]
        else:
            i=i.split(":=")
            if('*' in i[1]):
                n_1=i[1][0:i[1].find('*')]
                n_2=i[1][i[1].find('*')+1:]
                t_var[i[0]]=t_var[n_1]*int(n_2)
            elif '/' in i[1]:
                n_1=i[1][0:i[1].find('/')]
                n_2=i[1][i[1].find('/')+1:]
                t_var[i[0]]=t_var[n_1]/int(n_2)
            elif '-' in i[1]:
                n_1=i[1][0:i[1].find('-')]
                n_2=i[1][i[1].find('-')+1:]
                t_var[i[0]]=t_var[n_1]-int(n_2)
            elif '+' in i[1]:
                n_1=i[1][0:i[1].find('+')]
                n_2=i[1][i[1].find('+')+1:]
                t_var[i[0]]=t_var[n_1]+int(n_2)
    if done[t_no]==True:
        output_file.write("<COMMIT "+t_no+">\n")
        print_('m')
        print_('d')
x=int(sys.argv[2])
file=open(sys.argv[1])
s=file.readline()
while(s):
    m=s.split('(')
    if i==0:
        s=s.split()
        for j in range(len(s)):
            if j%2==0:
                disk_variable[s[j]]=int(s[j+1])
    elif not s.strip():
        t_no=None
    elif s.split()[0][0]=='T':
        s=s.split()
        tran_len[s[0]]=int(s[1])
        t_no=s[0]
        order.append(s[0])
        tran[t_no]=list()
    elif m[0]=='READ':
        tran[t_no].append(s[:-1])
    elif m[0]=='WRITE':
        tran[t_no].append(s[:-1])
    elif m[0]=='OUTPUT':
        tran[t_no].append(s[:-1])
    else:
        tran[t_no].append(s[:-1])
    i+=1
    s=file.readline()
file.close()
for i in tran.keys():
    done[i]=False
    start_t[i]=0
number=-1
iters=False
p=100
while p:
    number=(number+1)%len(order)
    if done[order[number]] != True:
        undo(number,x)
    for i in done.values():
        if i == False:
            iters=True
            break
    if iters==False:
        break
    iters=False
    if False in done.values():
        continue
    p=0
output_file.close()
