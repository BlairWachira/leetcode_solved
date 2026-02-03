hours=[0,1,2,3,4]
sucess=[]
def fun():
  target=2
  for i in range(5):
    if i >= target:
      sucess.append(i)
    else:
      continue
fun()
print(len(sucess))
