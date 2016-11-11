import csv
import sys
## Reading the input arguments:
file_in = sys.argv[1]
file_strm = sys.argv[2]
file_out1 = sys.argv[3]
file_out2 = sys.argv[4]
file_out3 = sys.argv[5]
## Converting the batch_payment into a dictionary
with open(file_in, 'r') as f_in:
# setup csvreader:
    batch_reader = csv.DictReader(f_in,delimiter=',')
    summary_payment = {}
    for transaction in batch_reader:
        if transaction[' id1'] in summary_payment:
            summary_payment[transaction[' id1']].append(transaction[' id2'])
            summary_payment[transaction[' id1']] = list(set(summary_payment[transaction[' id1']]))
        else:
            summary_payment[transaction[' id1']] = [transaction[' id2']]
            ## repeating above for id2
        if transaction[' id2'] in summary_payment:
            summary_payment[transaction[' id2']].append(transaction[' id1'])
            summary_payment[transaction[' id2']] = list(set(summary_payment[transaction[' id2']]))
        else:
            summary_payment[transaction[' id2']] = [transaction[' id1']]
# Feature 1************* Reading the stream_payment file line by line for the first feature:
with open(file_strm, 'r') as strm, open(file_out1,'w') as f_out1:
    stream_reader = csv.DictReader(strm, delimiter= ',')
    ftr1_cnt=0
    for stream in stream_reader:
        if stream[' id1'] in summary_payment:
            fraud_status = "unverified"
            friends = summary_payment[stream[' id1']]
            if stream[' id2'] in friends:
                fraud_status = "trusted"
                ftr1_cnt+=1
        f_out1.write("%s\n" % fraud_status)
#Feature 2**************
with open(file_strm, 'r') as strm, open(file_out2,'w') as f_out2:
    stream_reader = csv.DictReader(strm, delimiter= ',')
    ftr2_cnt=0
    for stream in stream_reader:
        if stream[' id1'] in summary_payment and stream[' id2'] in summary_payment:
            curr_list_id1 = summary_payment[stream[' id1']]
            curr_list_id2 = summary_payment[stream[' id2']]
            curr_list_id1.append(stream[' id1'])
            curr_list_id2.append(stream[' id2'])
            intersected_list = list(set(curr_list_id1).intersection(curr_list_id2))
            if len(intersected_list) == 0:
                fraud_status = "unverified"
            else:
                fraud_status = "trusted"
                ftr2_cnt+=1
        f_out2.write("%s\n" % fraud_status)
print("ftr1:", ftr1_cnt, "ftr2:", ftr2_cnt)
#Feature 3***************
with open(file_strm, 'r') as strm, open(file_out3,'w') as f_out3:
    stream_reader = csv.DictReader(strm, delimiter= ',')
    ftr3_cnt = 0
    for stream in stream_reader:
        if stream[' id1'] in summary_payment and stream[' id2'] in summary_payment:
            curr_list_id1 = summary_payment[stream[' id1']]
            curr_list_id2 = summary_payment[stream[' id2']]
            curr_list_id1.append(stream[' id1'])
            curr_list_id2.append(stream[' id2'])
            friends_of_id1 = list(set(curr_list_id1))
            friends_of_id2 = list(set(curr_list_id2))
            n_id1 = len(curr_list_id1)-1
            exist = 0
            while n_id1>-1 and exist==0:
                friends_of_id1 = list(set(friends_of_id1+(summary_payment[curr_list_id1[n_id1]])))
                n_id1-=1
                intersected_list = list(set(friends_of_id1).intersection(friends_of_id2))
                if (len(intersected_list)>0):
                    exist = 1
            n_id2 = len(curr_list_id2)-1
            while n_id2>-1 and exist==0:
                friends_of_id2 = list(set(friends_of_id2+(summary_payment[curr_list_id2[n_id2]])))
                n_id2-=1
                intersected_list = list(set(friends_of_id2).intersection(friends_of_id1))
                if (len(intersected_list)>0):
                    exist = 1
            if exist == 0:
                fraud_status = "unverified"
            else:
                fraud_status = "trusted"
                ftr3_cnt+=1
        f_out3.write("%s\n" % fraud_status)
print("ftr1:", ftr1_cnt, "ftr2:", ftr2_cnt,"ftr3:", ftr3_cnt)
