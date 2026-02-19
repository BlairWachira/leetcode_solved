def fun():
  n=5
  row=0
  while n>=row:
    n-=row
    row+=1
  return row-1

print(fun())