# README

I used Python 2.7.12 to write the coding challenge. 

I have implemented two approaches which they can be found in "detfraud.py" and "detfraud_rec.py".
In the first approach, "detfraud.py", under the criteria of desired features, the idea is implemented to finding friends of id1 and id2 and keep going forward until finding the first common friend. So, in this case, we will move from both sides to approach to the common friend.  

However, in the second approach, "detfraud_rec.py", in a recursive function, the id1 keeps unchanged and each time we pick out the friends of id2 and check whether they may have a common friend or not with each other. In this approach, a class is defined in order to pull out id1 and id2 from the batch-payment file and save them in the dictionary, and then with calling a recursive function we would able to find either trusted or unverified transactions.

I have put both python files in src directory and I have tried both of them with the insight_testsuit and both of them worked properly. However, the first approach which is "detfraud.py", was used in run.sh, mostly due to its speed. 

