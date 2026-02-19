def fun():
  n=20
  while n>=1:
    count=0
    for i in str(n):
      digit=int(i)
      count+=digit**2
    if count==n:
      break
    n=count
  
  
  return count

print(fun())

