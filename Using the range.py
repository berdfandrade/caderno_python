print(range(4))
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends)))

friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
    print('Happy New Year:', friend)

print('==================================')

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)
