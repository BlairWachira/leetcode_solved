def fun():
  hours=[0,1,2,3,4]
  target=2
  count=0
  for i in hours:
    if i >=target:
      count+=1
  return count

print(fun())
