real=0
fake=0



print('Give me your number of reading')
readings=int(input())
for i in range(0,readings):
  print('ok,give the number',i+1)
  temperature=int(input())
  if temperature>=10 and temperature<=40:
    real+=1
  if temperature<10 or temperature>40:
    fake+=1
rate=fake/readings
print('There is a failing rate of',rate,'%')
