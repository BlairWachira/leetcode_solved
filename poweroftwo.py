def fun(n):
  if n<=0:
    return False
  while n%2==0:
    n=n//2
  return n==1

print(fun(3))