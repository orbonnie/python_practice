tweet = input('Enter your tweet: ')

if len(tweet) == 140 :
  print('Your tweet is exactly 140 chars')

elif len(tweet) < 140 :
  print(f'Your {len(tweet)} char tweet will work!')

else :
  print(f'Your {len(tweet)} char tweet is {len(tweet) - 140} chars over the limit')