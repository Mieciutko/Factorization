import sys,time
start_time=time.time()

def Div(n,k):
  if n % k == 0:
    return True
  else:
    return False

inc=[4,2,4,2,4,6,2,6]
factors=[]

def Wheel(n):
  while Div(n,2):
    factors.append(2)
    n//=2
  while Div(n,3):
    factors.append(3)
    n//=3
  while Div(n,5):
    factors.append(5)
    n//=5

  k=7
  i=0
  while (k*k <= n):
    if Div(n,k):
      factors.append(k)
      n//=k
    else:
      k+=inc[i]
      if i < 7:
        i+=1
      else:
        i=1
  if n > 1:
    factors.append(n)
  return factors

Result=Wheel(int(sys.argv[1]))
print("Number: {}  Number of Divisors: {}  Divisors: {} Time: {}".format(int(sys.argv[1]),len(Result),Result,time.time()-start_time))