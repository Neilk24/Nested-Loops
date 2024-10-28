string=input("Please choose a word: ")
character=input("Please choose a charcter: ")

i=0
count=0

while(i<len(string)):
    if (string[i]==character):
        count=count+1
    i=i+1

print("The charcter", character,"has appeared in the word", string,"", count,"times")