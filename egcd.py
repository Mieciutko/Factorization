import numbers
import sys, time
start_time=time.time()


def Euklides(a,b):
    Q=[]
    a0=a
    b0=b
    t0=0
    t=1
    s0=1
    s=0
    q=a0//b0
    Q.append(q)
    r=a0-q*b0
    while (r>0):
        tmp=t0-q*t
        t0=t
        t=tmp
        tmp=s0-q*s
        s0=s
        s=tmp
        a0=b0
        b0=r
        q=a0//b0
        Q.append(q)
        r=a0-q*b0
    r=b0
    return (r,s,t)

f=True 
while(f):
  try:
    a=int(input("a =  "))
    b=int(input("b = "))
    f=False
    result=Euklides(a,b)
  except ValueError:
    print("Invalid parameter!")
    f=True

print("GCD({},{}) = {} = {}*{} + {}*{} \n Time: {}".format(a,b,result[0],result[1],a,result[2],b,time.time()-start_time))
