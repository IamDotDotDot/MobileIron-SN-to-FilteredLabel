print("This program will extract any iOS serial numbers from unwanted characters and format it for filtered labels.\nFor the most accurate results, do not insert Serial Numbers next to non-serial number \ncharacters without a space or separating dilemeter.\n")
okayish = input('Paste jumbled text here: ')
nonduplicates = []

#removes punctuation and replaces with a space
punc = '''!()-[]{};:'="\,<>./?@#$%^&*_~'''
for e in okayish:
    if e in punc:
        okayish = okayish.replace(e, " ")

#splits all text groups separated by a space into items in a list
okayishwords = okayish.split()

#finds SN that are not separated by spaces
findnospacesn = [e for e in okayishwords if len(e) % 12 == 0 and e.isupper()]

#converts list item to string
thisis = "".join(findnospacesn)
pain = ' '.join(thisis[i:i+12] for i in range(0, len(thisis), 12))
bro = pain.split()

#copies all the words that are all uppercase and have 12 characters to a new list
resultwords = [e for e in okayishwords if len(e) == 12 and e.isupper()]

#removes duplicates - new list
[nonduplicates.append(x) for x in resultwords if x not in nonduplicates]
[nonduplicates.append(x) for x in bro if x not in nonduplicates]

#adds syntax to output
for i in range(len(nonduplicates)):
    nonduplicates[i] = '  OR"common.SerialNumber" =  "'+nonduplicates[i]+'"'

#converts list item to string
result = ''.join(nonduplicates)

print("\n------------------------RESULTS BELOW--------------------------------\n")

#formatting syntax
fclean1 = result[4:]
fclean2 = "("+fclean1+') AND "common.retired" = false'

#output + troubleshooter for more than 2000 characters
t1 = len(fclean2)
count = 0
if len(fclean2) >= 2000:
    while t1 >= 2000:
        t1 -= 43
        count += 1
    print('''
    
            ERROR
    
    ''')
    print("   MobileIron queries (filters) can only support 2000 or less characters. The result is " + str(len(fclean2)) + " characters long.")
    print("   Each serial number adds 43 characters to the total. Remove " + str(count) + " serial numbers from the input to get a result fewer than 2000 characters.")
else:
    print(fclean2)

input("\nHit \"Enter\" to close: ")