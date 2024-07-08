# Task-3:Task of Generate Random password for user 

import string
import random
s1=string.ascii_uppercase
s2=string.ascii_lowercase
s3=string.digits
s4=string.punctuation
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s)
try:
   passlen=int(input("Enter Length Of Password : "))
   print("".join(s[ :passlen]))
except :
   print("Please Enter Any Integer Number")   