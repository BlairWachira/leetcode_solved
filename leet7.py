def fun():
  num=[3,4,5]
  if num[0]==num[1]==num[2]:
    return "equilateral"
  elif num[0]==num[1] or num[1]==num[2] or num[0]==num[2]:
    return "isosceles"
  else:
    return "scalene"
  
print(fun())