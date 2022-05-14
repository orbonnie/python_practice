from textblob import TextBlob
from art import text2art
import pyttsx3

print(text2art('Ministry of Work'))
engine = pyttsx3.init()
engine.say('''Hello employee 123. We hope you had a great day of work.
 Its time to submit your employee wellness statement''')
engine.runAndWait()

print('Enter your employee wellness statement: ')
phrase = input("> ")
blob = TextBlob(phrase)
while blob.sentiment.polarity < 0.5:
  engine.say('''We need you to be more positive. Please try again.
  We know how much you like working here.''')
  engine.runAndWait()

  print('More positivity please: ')
  phrase = input("> ")
  blob = TextBlob(phrase)

engine.say('Thank you! We appreciate you too!')
engine.runAndWait()
print('We appreciate you too!')