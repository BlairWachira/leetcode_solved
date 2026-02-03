def fun():
  accounts=[[2,8,7],[7,1,3],[1,9,5]]
  sum_account=[]
  for i in accounts:
    sum_account.append(sum(i))
  return max(sum_account)

print(fun())
