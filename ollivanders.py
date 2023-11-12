print('I will healp you to know how many people enter the store and which wand they bought')
numofcustomers=0
elder=0
hawthorn=0
willow=0
holly=0
retry='yes'
while retry.lower()=='yes':
  print('Have a new customer enter to the stor yes/no')
  retry=input()
  if retry.lower()=='yes':
    numofcustomers+=1
    print('And what wand do it buy? 0.It didnt buy a wand 1.Elder Wand, 2. Hawthorn Wand, 3. Willow Wand, and 4. Holly Wand.')
    print('The response mut be in numbers')
    wand=input()
    if wand=='0':
      pass
    elif wand=='1':
      elder+=1
    elif wand=='2':
      hawthorn+=1
    elif wand=='3':
      willow+=1
    elif wand=='4':
      holly+=1

  elif retry.lower()=='no':
    break

  else:
    print('That is not a balid option, try again')
    retry=input()

print('The total number of people that enter the store is',numofcustomers)
print('Elder wands sold')
print(elder)
print('Hawthorn wands sold')
print(hawthorn)
print('Willow wands sold')
print(willow)
print('Holly wands sold')
print(holly)
