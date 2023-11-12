print('Hi, I am Alexa, and I can detect if you have said my name more than once, try me')
text=input()
words = text.split()


alexacount = words.count('Alexa')

if alexacount == 1:
    print("You have said my name once")
elif alexacount > 1:
    print("You mentioned Alexa more than once!")
else:
    print("You didnt mention me in the text")
