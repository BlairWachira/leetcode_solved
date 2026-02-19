def fun():
  count=0
  for num in range(1,10000000+1):
    if '0' not in str(num) and '1' not in str(num):
      continue
    else:
      count+=1
  return count

print(fun())

