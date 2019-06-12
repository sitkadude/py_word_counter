# Prompt for file to run in program.
fname = input('Enter File: ')
try:
    handle = open(fname)
except:
    print('File', fname, 'cannot be found.')
    quit()

# Creates dictionary.
di = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

# Finding the most common word
largest_count = -1
word = None
for k,v in di.items():
    if v > largest_count:
        largest_count = v
        word = k

print('Largest Word:', word)
print('Word Count:', largest_count)