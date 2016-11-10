import csv
import numpy as np
import pandas as pd
import sys
# Reading the input arguments:
file_in = sys.argv[1]
file_strm = sys.argv[2]
file_out1 = sys.argv[3]
file_out2 = sys.argv[4]
file_out3 = sys.argv[5]

# Define a Class Called SummaryPayment:       
class SummaryPayment:
    file_in =''
    def __init__(self,file_in):
        self.file_in = file_in
    def summary(self):

        with open(self.file_in, 'r') as f_in:
            batch_reader = csv.DictReader(f_in,delimiter=',')
            payment = {}
            
            for transaction in batch_reader:
                if transaction[' id1'] in payment:
                    payment[transaction[' id1']].append(transaction[' id2'])
                    payment[transaction[' id1']] = list(set(payment[transaction[' id1']]))
                else:
                    payment[transaction[' id1']] = [transaction[' id2']]
                if transaction[' id2'] in payment:
                     payment[transaction[' id2']].append(transaction[' id1'])
                     payment[transaction[' id2']] = list(set(payment[transaction[' id2']]))
                else:
                     payment[transaction[' id2']] = [transaction[' id1']]
            
            return(payment)
# Define a recursive function Verify():
def Verify(id1,id2,d,summary_payment,visited_ids):
    status = "unverified"
    friends = summary_payment[id2]
    list_id2 = friends
    list_id1 = summary_payment[id1]
    list_id1.append(id1)
    list_id2.append(id2)
    intersected_list = list(set(list_id1).intersection(list_id2))    
    if d == 1:
        if id1 in friends:
            status = "trusted"
    elif d == 2:
                    
        if len(intersected_list)!=0:
            status = "trusted"  
    else:
        if id1 in friends or len(intersected_list)!=0:
            status = "trusted"
        
        new_friends = [id for id in set(friends) if id is not visited_ids.append(id2)] ####[item for item in temp1 if item not in temp2]
        l = len(new_friends)-1
        while l>-1 and status == "unverified":
            status = Verify(id1,new_friends[l],d-1, summary_payment,visited_ids)
            visited_ids.append(new_friends[l])
            l-=1
    return(status)        
summary_payment = SummaryPayment(file_in)
outFile = summary_payment.summary()
        
with open(file_strm, 'r') as strm, open(file_out3,'w') as f_out3:
    stream_reader = csv.DictReader(strm, delimiter= ',')
    cnt_verify = 0
    for stream in stream_reader:
        if stream[' id1']  in outFile and stream[' id2'] in outFile :
            fraud_status = Verify( stream[' id1'], stream[' id2'], 4, outFile,list())
            if fraud_status == "trusted":
                cnt_verify+=1
            f_out3.write("%s\n" % fraud_status)
    print(cnt_verify)