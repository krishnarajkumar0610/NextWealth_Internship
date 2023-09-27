# Problem 1:
# Read a passage from a file. (If you don't know how to handle files in Python, you can hardcode a long passage)
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servernt. 
# The king shot a deer. The king went to the forest again the next day.

#['the','king','shot','a','dear.','the','king','went','to','the','forest','again','the','next','day']

sentence = input("enter the sentence :")    # asking the user to give sentence

splited_words= sentence.lower()     # converting it into lower case
    
splited_words=splited_words.split(" ")      # spliting it 

word="the"    # storeing 'the' in first word variablee
middle_letter="a"   # storing 'a' in middle word 
check_sentence=[]   # declaring the emply list 
count=0     # declaring the count varibale

def check(words,middle_letter):
    for i in range(1,len(words)-1):  
        if words[i]==middle_letter: # if contains then return  true
            return True
    return False    # not contain a return false

i=0 # initializing a 

for i in range(i,len(splited_words)):   # to traverse the list
    if splited_words[i] == word:
        check_sentence.append(splited_words[i])
        for j in range(i+1,len(splited_words)):
            check_sentence.append(splited_words[j])
            if splited_words[j] == word:
                if not check(check_sentence,middle_letter):
                    count = count + 1
                    check_sentence.clear()  # []
                else:
                    check_sentence.clear()
                i=j
                break
             
print(count)


# OUTPUT

# enter the sentence :The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day
# 7