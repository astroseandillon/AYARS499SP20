#!/usr/bin/env python

'''
	fakedata.py
	Eric Ayars
	1/28/20

	Generates fake data that we'll pretend comes from a 
	Normal-Modes Apparatus. For Sean to test his program(s).
'''

from numpy import *
from random import random

N = 1000		# size of arrays
MaxTime = 100	# seconds
# Five random frequency components
w1 = random()
w2 = random()+0.2
w3 = random()+0.4
w4 = random()+0.6
w5 = random()+0.9

# Time array
t = arange(0,MaxTime, MaxTime/N)

# amplitude arrays
x1 =  random() * sin(w1*t + random()) + random() * sin(w2*t + random()) + random() * sin(w3*t + random()) + random() * sin(w4*t + random()) + random() * sin(w5*t + random()) 
x2 =  random() * sin(w1*t + random()) + random() * sin(w2*t + random()) + random() * sin(w3*t + random()) + random() * sin(w4*t + random()) + random() * sin(w5*t + random()) 
x3 =  random() * sin(w1*t + random()) + random() * sin(w2*t + random()) + random() * sin(w3*t + random()) + random() * sin(w4*t + random()) + random() * sin(w5*t + random()) 
x4 =  random() * sin(w1*t + random()) + random() * sin(w2*t + random()) + random() * sin(w3*t + random()) + random() * sin(w4*t + random()) + random() * sin(w5*t + random()) 
x5 =  random() * sin(w1*t + random()) + random() * sin(w2*t + random()) + random() * sin(w3*t + random()) + random() * sin(w4*t + random()) + random() * sin(w5*t + random())

# Save data
file = open("fakedata.txt", 'w')
file.write("# Fake data generated by fakedata.py\n")
file.write("# Time\tx1\tx2\tx3\tx4\tx5\n")

for j in range(N):
	file.write("%0.1f\t%0.3f\t%0.3f\t%0.3f\t%0.3f\t%0.3f\n" % (t[j],x1[j],x2[j],x3[j],x4[j],x5[j]))
file.close()
