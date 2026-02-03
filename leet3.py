def fun():
  nums=[1,15,6,3]
  element_sum=0
  digit_sum=0
  for i in nums:
      element_sum+=i
      for d in str(i):
          digit_sum+=int(d)
  output=element_sum-digit_sum
  return output

print(fun())