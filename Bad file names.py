fname = input('Enter the name of the file')
fname()
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()  # É possível usar esse "Quit" para parar a iteration

count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
