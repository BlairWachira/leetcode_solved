def addDigits(num):
  while num>9:
    sum_of=0
    for i in str(num):
      sums=int(i)
      sum_of+=sums
    num=sum_of
  return sum_of

result=addDigits(23456)
print(result)