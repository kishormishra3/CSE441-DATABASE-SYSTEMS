import sqlparse
import sys
import itertools
def check(y):
    for i in y:
        if("max" in i or "MAX" in i):
            return True
        if("min" in i or "MIN" in i):
            return True
        if("sum" in i or "SUM" in i):
            return True
        if("avg" in i or "AVG" in i):
            return True
        if("distinct" in i or "DISTINCT" in i):
            return True
    return False
def compute(y,z,op1,op2,ff,tab,save):
    try:
        x=""
        pp=""
        ss=0
        for i in tab:
            for j in range(1,len(i)):
                if(y[0]==i[j]):
                    y[0]=i[0]+"."+y[0]
                if(y[1]==i[j]):
                    x=i[0]+"."+y[1]
                if(z[0]==i[j]):
                    z[0]=i[0]+"."+z[0]
                if(z[1]==i[j]):
                    pp=i[0]+"."+z[1]   
        if (x == "" and pp == "") and (len(y[1].split("."))<2 and len(z[1].split("."))<2):
            ss=1
            x=y[1]
            pp=z[1]
            x=int(x)
            pp=int(pp)
        elif x == "" and len(y[1].split("."))<2:
            ss=2
            x=y[1]
            x=int(x)
            if(pp != ""):
                z[1]=pp
        elif pp =="" and len(z[1].split("."))<2:
            ss=3
            pp=z[1]
            pp=int(pp)
            if(x!= ""):
                y[1]=x
        elif len(y[1].split("."))<2 and len(z[1].split("."))<2:
            if(pp!=""):
                z[1]=pp
            if(x!=""):
                y[1]=x
        ff=ff.split(",")
        d2={}
        ma=0
        for i in ff:
            d2[i]=ma
            ma=ma+1
        save2=[]
        for i in range(len(save)):
            save2.append([])
        if(op1 ==">=" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">=" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">=" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">=" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">=" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <=x and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= x and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <=x and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <=save[d2[y[1]]][i] and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= x and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <=x and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= x and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<=x and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<=save[d2[y[1]]][i] and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<= x and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<= save[d2[y[1]]][i] and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<=x and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<=save[d2[y[1]]][i] and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<= x and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<= save[d2[y[1]]][i] and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <x and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <save[d2[y[1]]][i] and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<x and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<save[d2[y[1]]][i] and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]< x and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]< save[d2[y[1]]][i] and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<x and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<save[d2[y[1]]][i] and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]< x and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]< save[d2[y[1]]][i] and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>x and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>save[d2[y[1]]][i] and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]> save[d2[y[1]]][i] and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>x and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>save[d2[y[1]]][i] and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]> x and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]> save[d2[y[1]]][i] and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] and save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] and save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] ==x and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] ==save[d2[y[1]]][i] and save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] and save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] and save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] and save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==x and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==save[d2[y[1]]][i] and save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]== x and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]== save[d2[y[1]]][i] and save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==x and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==save[d2[y[1]]][i] and save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]== x and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==save[d2[y[1]]][i] and save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        return save2
    except:
        print("Error")
        sys.exit()

def compute1(y,z,op1,op2,ff,tab,save):
    try:
        x=""
        pp=""
        ss=0
        for i in tab:
            for j in range(1,len(i)):
                if(y[0]==i[j]):
                    y[0]=i[0]+"."+y[0]
                if(y[1]==i[j]):
                    x=i[0]+"."+y[1]
                if(z[0]==i[j]):
                    z[0]=i[0]+"."+z[0]
                if(z[1]==i[j]):
                    pp=i[0]+"."+z[1]   
        if (x == "" and pp == "") and (len(y[1].split("."))<2 and len(z[1].split("."))<2):
            ss=1
            x=y[1]
            pp=z[1]
            x=int(x)
            pp=int(pp)
        elif x == "" and len(y[1].split("."))<2:
            ss=2
            x=y[1]
            x=int(x)
            if(pp != ""):
                z[1]=pp
        elif pp =="" and len(z[1].split("."))<2:
            ss=3
            pp=z[1]
            pp=int(pp)
            if(x!= ""):
                y[1]=x
        elif len(y[1].split("."))<2 and len(z[1].split("."))<2:
            if(pp!=""):
                z[1]=pp
            if(x!=""):
                y[1]=x
        ff=ff.split(",")
        d2={}
        ma=0
        for i in ff:
            d2[i]=ma
            ma=ma+1
        save2=[]
        for i in range(len(save)):
            save2.append([])
        if(op1 ==">=" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">=" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">=" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">=" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">=" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=x or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>=save[d2[y[1]]][i] or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= x or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>= save[d2[y[1]]][i] or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <=x or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= x or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <=x or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <=save[d2[y[1]]][i] or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= x or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <=x or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= x or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <= save[d2[y[1]]][i] or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<=x or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<=save[d2[y[1]]][i] or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<= x or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<= save[d2[y[1]]][i] or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<=" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<=x or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<=save[d2[y[1]]][i] or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<= x or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<= save[d2[y[1]]][i] or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <x or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] <save[d2[y[1]]][i] or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < x or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] < save[d2[y[1]]][i] or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<x or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<save[d2[y[1]]][i] or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]< x or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]< save[d2[y[1]]][i] or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="<" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<x or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]<save[d2[y[1]]][i] or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]< x or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]< save[d2[y[1]]][i] or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > save[d2[y[1]]][i] or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>x or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>save[d2[y[1]]][i] or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] > x or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]> save[d2[y[1]]][i] or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 ==">" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>x or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]>save[d2[y[1]]][i] or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]> x or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]> save[d2[y[1]]][i] or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == ">="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] or save[d2[z[0]]][i] >=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] or save[d2[z[0]]][i] >= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == "<="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] ==x or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] ==save[d2[y[1]]][i] or save[d2[z[0]]][i] <=pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] or save[d2[z[0]]][i] <= save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == "<"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] or save[d2[z[0]]][i] <pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == x or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i] == save[d2[y[1]]][i] or save[d2[z[0]]][i] < save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == ">"):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==x or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==save[d2[y[1]]][i] or save[d2[z[0]]][i] > pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]== x or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]== save[d2[y[1]]][i] or save[d2[z[0]]][i] > save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        elif(op1 =="=" and op2 == "="):
            if(ss==1):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==x or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==3):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==save[d2[y[1]]][i] or save[d2[z[0]]][i] == pp):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==2):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]== x or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
            elif(ss==0):
                for i in range(min(len(save[d2[y[0]]]),len(save[d2[z[0]]]))):
                    if(save[d2[y[0]]][i]==save[d2[y[1]]][i] or save[d2[z[0]]][i] == save[d2[z[1]]][i]):
                        for j in range(len(save)):
                            save2[j].append(save[j][i])
        return save2
    except:
        print("Error")
        sys.exit()

try:
    f1=open("files/metadata.txt","r")
    table=[]
    s=f1.readline()
    while s:
        s=s.replace("\n","")
        if(s=="<begin_table>"):
            l=[]
            s=f1.readline()
            s=s.replace("\n","")
            l.append(s)
            s=f1.readline()
            s=s.replace("\n","")
            while s:
                l.append(s)
                s=f1.readline()
                s=s.replace("\n","")
                if(s=="<end_table>"):
                    break
            table.append(l)
        s=f1.readline()
    f1.close()
    raw=""
    raw=sys.argv[1]
    if(("max" in raw or "min" in raw or "sum" in raw or "avg" in raw) and "distinct" in raw):
        print("Error")
        sys.exit()
    raw.replace('"','')
    parsedQuery = sqlparse.parse(raw)[0].tokens
    queryType = sqlparse.sql.Statement(parsedQuery).get_type()
    ll=[]
    l = sqlparse.sql.IdentifierList(parsedQuery).get_identifiers()
    for i in l:
    	ll.append(str(i))
    cols=[]
    col=ll[1]
    tab=ll[3]
    tab=tab.split(",")
    for i in range(len(tab)):
        tab[i]=tab[i].replace(" ","")
    l=len(tab)
    file=list()
    for i in range(0,l):
        x=""
        x="files/"+tab[i]+".csv"
        file.append(open(x,"r"))
        x=0
        for j in range(len(table)):
            if(tab[i]==table[j][0]):
                x=j;
                break
        cols.append([x])
        for k in file[i]:
            k=k.replace("\n","")
            k=k.split(",")
            cols[i].append(k)
        for i in file:
            i.close()
    m=""
    p=""
    for i in cols:
        x=i[0]
        p=""
        p=p+str(table[x][0])
        for j in range(1,len(table[x])):
            m=m+p+"."+str(table[x][j])
            m=m+","
    m=m+"\n"
    lp=[]
    for i in cols:
        lp.append(i[1:])
    for element in itertools.product(*lp):
        for i in element:
            m+=str(i[:])
            m=m+","
        m=m[:len(m)-1]
        m=m+"\n"
    m=m[:len(m)-1]
    m=m.replace("[","")
    m=m.replace("]","")
    m=m.replace(" ","")
    m=m.replace("'","")
    ff=m.split("\n")
    d={}
    ma=0
    for kk in str(ff[0]).split(","):
       ma=ma+1
    ma=ma-1
    save=[]
    for i in range(ma):
        save.append([])
    for i in range(1,len(ff)):
        ma=0
        for k in ff[i].split(","):
            save[ma].append(int(k))
            ma=ma+1
    d1={}
    ma=0
    ff=str(ff[0])[0:len(str(ff[0]))-1]
    for kk in ff.split(","):
        d1[kk]=save[ma]
        ma=ma+1
    for i in range(len(table)):
        for j in range(len(tab)):
            if(tab[j]==table[i][0]):
                tab[j]=table[i]
    gg=ff
    d2={}
    ma=0
    for i in ff.split(","):
        d2[i]=ma
        ma=ma+1
    if len(ll)==5 and "where" not in ll[4]:
        y=col.split(",")
        if(y[0]=="*"):
            file=open("output.csv","w")
            file.write(m)
            file.close()
        elif check(y):
            b=False
            pp=True
            m=""
            mm=""
            for i in y:
                b=False
                pp=True
                m=""
                mm=""
                for k in i:
                    if(k=='('):
                        b=True
                        pp=False
                    elif k==')':
                        b=False
                    elif b:
                        m=m+k
                    if pp:
                        mm+=k
                for i in range(0,len(y)):
                    for j in ff.split(","):
                        pp=j.split(".")
                        if m == pp[1]:
                            m=j
                        elif m==j:
                            m=j
                if(mm=="max" or mm=="MAX"):
                    print(max(d1[m]))
                elif(mm=="min" or mm=="MIN"):
                    print(min(d1[m]))
                elif(mm=="sum" or mm=="SUM"):
                    print(sum(d1[m]))
                elif(mm=="avg" or mm=="AVG"):
                    print(sum(d1[m])/len(d1[m]))
                elif(mm=="distinct" or mm=="DISTINCT"):
                    print(set((d1[m])))
        else:
            for i in range(0,len(y)):
                for j in ff.split(","):
                    pp=j.split(".")
                    if y[i] == pp[1]:
                        y[i]=j
                    elif y[i]==j:
                        y[i]=j
            m=""
            for i in y:
                m=m+str(i)
                m=m+','
            m=m[:len(m)-1]
            m+="\n"
            save=[]
            for i in y:
                save.append(d1[i])
            for i in range(max([len(j) for j in save])):
                for k in range(0,len(save)):
                    try:
                        m=m+str(save[k][i])+","
                    except:
                        m+=","
                m=m[:len(m)-1]
                m+="\n"
            m=m[:len(m)-1]
            file=open("output.csv","w")
            file.write(m)
            file.close()
    elif len(ll)==5 and "where" in ll[4]:
        y=ll[4]
        pp=0
        y=y.replace(";","")
        y=y.replace("where ","")
        if("AND" in y):
            y=y.split("AND")  
            pp=1
        elif("OR" in y):
            y=y.split("OR")
            pp=2
        elif("and" in y):
            y=y.split("and")  
            pp=1
        elif("or" in y):
            y=y.split("or")
            pp=2
        else:
            pp=0
        x=0
        if(type(y)==str):
            if(">=" in y):
                y=y.split(">=")
                y[0]=y[0].replace(" ","")
                y[1]=y[1].replace(" ","")
                try:
                    x=""
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                x=i[0]+"."+y[1]
                    if x not in ff:
                        raise "Error"
                    x=0
                    x=int(y[1])
                    ff=ff.split(",")
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(len(save[d2[y[0]]])):
                        if(save[d2[y[0]]][i]>=x):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])
                except:
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                y[1]=i[0]+"."+y[1]
                    ff=ff.split(",")
                    d2={}
                    ma=0
                    for i in ff:
                        d2[i]=ma
                        ma=ma+1
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(min(len(save[d2[y[0]]]),len(save[d2[y[0]]]))):
                        if(save[d2[y[0]]][i]>=save[d2[y[1]]][i]):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])
            elif("<=" in y):
                y=y.split("<=")
                y[0]=y[0].replace(" ","")
                y[1]=y[1].replace(" ","")
                try:
                    x=""
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                x=i[0]+"."+y[1]
                    if x not in ff:
                        raise "Error"
                    x=0
                    x=int(y[1])
                    ff=ff.split(",")
                    d2={}
                    ma=0
                    for i in ff:
                        d2[i]=ma
                        ma=ma+1
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(len(save[d2[y[0]]])):
                        if(save[d2[y[0]]][i]<=x):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])
                except:
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                y[1]=i[0]+"."+y[1]
                    ff=ff.split(",")
                    d2={}
                    ma=0
                    for i in ff:
                        d2[i]=ma
                        ma=ma+1
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(min(len(save[d2[y[0]]]),len(save[d2[y[0]]]))):
                        if(save[d2[y[0]]][i]<=save[d2[y[1]]][i]):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])
            elif(">" in y):
                y=y.split(">")
                y[0]=y[0].replace(" ","")
                y[1]=y[1].replace(" ","")
                try:
                    x=""
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                x=i[0]+"."+y[1]
                    if x not in ff:
                        raise "Error"
                    x=0
                    x=int(y[1])
                    ff=ff.split(",")
                    d2={}
                    ma=0
                    for i in ff:
                        d2[i]=ma
                        ma=ma+1
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(len(save[d2[y[0]]])):
                        if(save[d2[y[0]]][i]>x):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])
                except:
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                y[1]=i[0]+"."+y[1]
                    ff=ff.split(",")
                    d2={}
                    ma=0
                    for i in ff:
                        d2[i]=ma
                        ma=ma+1
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(min(len(save[d2[y[0]]]),len(save[d2[y[1]]]))):
                        if(save[d2[y[0]]][i]>save[d2[y[1]]][i]):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])
            elif("<" in y):
                y=y.split("<")
                y[0]=y[0].replace(" ","")
                y[1]=y[1].replace(" ","")
                try:
                    x=""
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                x=i[0]+"."+y[1]
                    if x not in ff:
                        raise "Error"
                    x=0
                    x=int(y[1])
                    ff=ff.split(",")
                    d2={}
                    ma=0
                    for i in ff:
                        d2[i]=ma
                        ma=ma+1
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(len(save[d2[y[0]]])):
                        if(save[d2[y[0]]][i]<x):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])
                except:
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                y[1]=i[0]+"."+y[1]
                    ff=ff.split(",")
                    d2={}
                    ma=0
                    for i in ff:
                        d2[i]=ma
                        ma=ma+1
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(min(len(save[d2[y[0]]]),len(save[d2[y[0]]]))):
                        if(save[d2[y[0]]][i]<save[d2[y[1]]][i]):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])
            elif("=" in y):
                y=y.split("=")
                y[0]=y[0].replace(" ","")
                y[1]=y[1].replace(" ","")
                try:
                    x=""
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                x=i[0]+"."+y[1]
                    if x not in ff:
                        raise "Error"
                    x=0
                    x=int(y[1])
                    ff=ff.split(",")
                    d2={}
                    ma=0
                    for i in ff:
                        d2[i]=ma
                        ma=ma+1
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(len(save[d2[y[0]]])):
                        if(save[d2[y[0]]][i]==x):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])
                except:
                    for i in tab:
                        for j in range(1,len(i)):
                            if(y[0]==i[j]):
                                y[0]=i[0]+"."+y[0]
                            if(y[1]==i[j]):
                                y[1]=i[0]+"."+y[1]
                    ff=ff.split(",")
                    d2={}
                    ma=0
                    for i in ff:
                        d2[i]=ma
                        ma=ma+1
                    save2=[]
                    for i in range(len(save)):
                        save2.append([])
                    for i in range(min(len(save[d2[y[0]]]),len(save[d2[y[0]]]))):
                        if(save[d2[y[0]]][i]==save[d2[y[1]]][i]):
                            for j in range(len(save)):
                                save2[j].append(save[j][i])   
        elif(type(y)==list):
            if(pp==1):
                for i in range(len(y)):
                    y[i]=y[i].replace(" ","")
                a1,a2=[],[]
                save2=[]
                if(">=" in y[0] and ">=" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split(">=")
                    save2=compute(a1,a2,">=",">=",ff,tab,save)
                elif(">=" in y[0] and ">" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split(">")
                    save2=compute(a1,a2,">=",">",ff,tab,save)
                elif(">=" in y[0] and "<=" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split("<=")
                    save2=compute(a1,a2,">=","<=",ff,tab,save)
                elif(">=" in y[0] and "<" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split("<")
                    save2=compute(a1,a2,">=","<",ff,tab,save)
                elif(">=" in y[0] and "=" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split("=")
                    save2=compute(a1,a2,">=","=",ff,tab,save)
                elif("<=" in y[0] and ">=" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split(">=")
                    save2=compute(a1,a2,"<=",">=",ff,tab,save)
                elif("<=" in y[0] and ">" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split(">")
                    save2=compute(a1,a2,"<=",">",ff,tab,save)
                elif("<=" in y[0] and "<=" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split("<=")
                    save2=compute(a1,a2,"<=","<=",ff,tab,save)
                elif("<=" in y[0] and "<" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split("<")
                    save2=compute(a1,a2,"<=","<",ff,tab,save)
                elif("<=" in y[0] and "=" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split("=")
                    save2=compute(a1,a2,"<=","=",ff,tab,save)
                elif("<" in y[0] and ">=" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split(">=")
                    save2=compute(a1,a2,"<",">=",ff,tab,save)
                elif("<" in y[0] and ">" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split(">")
                    save2=compute(a1,a2,"<",">",ff,tab,save)
                elif("<" in y[0] and "<=" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split("<=")
                    save2=compute(a1,a2,"<","<=",ff,tab,save)
                elif("<" in y[0] and "<" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split("<")
                    save2=compute(a1,a2,"<","<",ff,tab,save)
                elif("<" in y[0] and "=" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split("=")
                    save2=compute(a1,a2,"<","=",ff,tab,save)
                elif(">" in y[0] and ">=" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split(">=")
                    save2=compute(a1,a2,">",">=",ff,tab,save)
                elif(">" in y[0] and ">" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split(">")
                    save2=compute(a1,a2,">",">",ff,tab,save)
                elif(">" in y[0] and "<=" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split("<=")
                    save2=compute(a1,a2,">","<=",ff,tab,save)
                elif(">" in y[0] and "<" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split("<")
                    save2=compute(a1,a2,">","<",ff,tab,save)
                elif(">" in y[0] and "=" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split("=")
                    save2=compute(a1,a2,">","=",ff,tab,save)
                elif("=" in y[0] and ">=" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split(">=")
                    save2=compute(a1,a2,"=",">=",ff,tab,save)
                elif("=" in y[0] and ">" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split(">")
                    save2=compute(a1,a2,"=",">",ff,tab,save)
                elif("=" in y[0] and "<=" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split("<=")
                    save2=compute(a1,a2,"=","<=",ff,tab,save)
                elif("=" in y[0] and "<" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split("<")
                    save2=compute(a1,a2,"=","<",ff,tab,save)
                elif("=" in y[0] and "=" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split("=")
                    save2=compute(a1,a2,"=","=",ff,tab,save)
            elif(pp==2):
                for i in range(len(y)):
                    y[i]=y[i].replace(" ","")
                a1,a2=[],[]
                save2=[]
                if(">=" in y[0] and ">=" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split(">=")
                    save2=compute1(a1,a2,">=",">=",ff,tab,save)
                elif(">=" in y[0] and ">" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split(">")
                    save2=compute1(a1,a2,">=",">",ff,tab,save)
                elif(">=" in y[0] and "<=" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split("<=")
                    save2=compute1(a1,a2,">=","<=",ff,tab,save)
                elif(">=" in y[0] and "<" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split("<")
                    save2=compute1(a1,a2,">=","<",ff,tab,save)
                elif(">=" in y[0] and "=" in y[1]):
                    a1=y[0].split(">=")
                    a2=y[1].split("=")
                    save2=compute1(a1,a2,">=","=",ff,tab,save)
                elif("<=" in y[0] and ">=" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split(">=")
                    save2=compute1(a1,a2,"<=",">=",ff,tab,save)
                elif("<=" in y[0] and ">" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split(">")
                    save2=compute1(a1,a2,"<=",">",ff,tab,save)
                elif("<=" in y[0] and "<=" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split("<=")
                    save2=compute1(a1,a2,"<=","<=",ff,tab,save)
                elif("<=" in y[0] and "<" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split("<")
                    save2=compute1(a1,a2,"<=","<",ff,tab,save)
                elif("<=" in y[0] and "=" in y[1]):
                    a1=y[0].split("<=")
                    a2=y[1].split("=")
                    save2=compute1(a1,a2,"<=","=",ff,tab,save)
                elif("<" in y[0] and ">=" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split(">=")
                    save2=compute1(a1,a2,"<",">=",ff,tab,save)
                elif("<" in y[0] and ">" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split(">")
                    save2=compute1(a1,a2,"<",">",ff,tab,save)
                elif("<" in y[0] and "<=" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split("<=")
                    save2=compute1(a1,a2,"<","<=",ff,tab,save)
                elif("<" in y[0] and "<" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split("<")
                    save2=compute1(a1,a2,"<","<",ff,tab,save)
                elif("<" in y[0] and "=" in y[1]):
                    a1=y[0].split("<")
                    a2=y[1].split("=")
                    save2=compute1(a1,a2,"<","=",ff,tab,save)
                elif(">" in y[0] and ">=" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split(">=")
                    save2=compute1(a1,a2,">",">=",ff,tab,save)
                elif(">" in y[0] and ">" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split(">")
                    save2=compute1(a1,a2,">",">",ff,tab,save)
                elif(">" in y[0] and "<=" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split("<=")
                    save2=compute1(a1,a2,">","<=",ff,tab,save)
                elif(">" in y[0] and "<" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split("<")
                    save2=compute1(a1,a2,">","<",ff,tab,save)
                elif(">" in y[0] and "=" in y[1]):
                    a1=y[0].split(">")
                    a2=y[1].split("=")
                    save2=compute1(a1,a2,">","=",ff,tab,save)
                elif("=" in y[0] and ">=" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split(">=")
                    save2=compute1(a1,a2,"=",">=",ff,tab,save)
                elif("=" in y[0] and ">" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split(">")
                    save2=compute1(a1,a2,"=",">",ff,tab,save)
                elif("=" in y[0] and "<=" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split("<=")
                    save2=compute1(a1,a2,"=","<=",ff,tab,save)
                elif("=" in y[0] and "<" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split("<")
                    save2=compute1(a1,a2,"=","<",ff,tab,save)
                elif("=" in y[0] and "=" in y[1]):
                    a1=y[0].split("=")
                    a2=y[1].split("=")
                    save2=compute1(a1,a2,"=","=",ff,tab,save)
        y=col.split(",")
        save3=[]
        for i in range(0,len(y)):
                for j in gg.split(","):
                    pp=j.split(".")
                    if y[i] == pp[1]:
                        y[i]=j
                    elif y[i]==j:
                        y[i]=j
        m=""
        if(len(y)==1 and y[0]=='*'):
            for i in tab:
                for j in range(1,len(i)):
                    m=m+i[0]+"."+i[j]+","
            m=m[:len(m)-1]
            m=m+"\n"
        else:
            for i in y:
                save3.append(save2[d2[i]])
            for i in y:
                m=m+i+","
            m=m[:len(m)-1]
            m=m+"\n"
            save2=save3
        for i in range(max([len(j) for j in save2])):
            for k in range(0,len(save2)):
                try:
                    m=m+str(save2[k][i])+","
                except:
                    m+=","
            m=m[:len(m)-1]
            m+="\n"
        m=m[:len(m)-1]
        file=open("output.csv","w")
        file.write(m)
        file.close()
except:
    print("Wrong answer")           
            
            
            
            
            
            
            
            
            
            