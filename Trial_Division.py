import sys, time
start_time=time.time()



def Trial_Div(n):
  a=[]
  while( n%2 == 0 ):
    a.append(2)
    n = n//2
  f=3
  while( f*f <=n ):
    if n % f ==0:
      a.append(f)
      n=n//f
    else:
      f=f+2
  if n != 1:
    a.append(n)
  return(a)

Result=Trial_Div(int(sys.argv[1]))

print("Number: {}  Number of Divisors: {}  Divisors: {} Time: {}".format(int(sys.argv[1]),len(Result),Result,time.time()-start_time))