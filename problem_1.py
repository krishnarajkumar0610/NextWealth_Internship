sentence = input("enter the sentence :")    # asking the user to give sentence

splited_words= sentence.lower()     # converting it into lower case
    
splited_words=splited_words.split(" ")      # spliting it 

first_word="the"    # storeing 'the' in first word variablee
middle_letter="a"   # storing 'a' in middle word 
last_word="the"     # storing 'the' in the last word variable
check_sentence=[]   # declaring the emply list 
count=0     # declaring the count varibale
def check(index,check_sentence , middle_letter):        # this method is to check wheather the sentence contains 'a' 
    for i in range(index,len(check_sentence)):
        return True # if it has 'a' then return True
    return False    # if not having 'a' then return False

for i in range(len(splited_words)):     # traversing the whole list 
    if splited_words[i] in first_word:  # if 'the' is in word
        check_sentence.append(splited_words[i]) # appending in string
        for j in range(i+1,len(splited_words)): # then checking another 'the'
            if splited_words[j] in last_word:   # if fined another 'the' in list 
                check_sentence.append(splited_words[j]) # appending it to string
                if not check(i,check_sentence,middle_letter):   # passing the llist and 'a' and index                    
                    count+=1       # if there is no a then count +1
            else:   
                check_sentence.append(splited_words[j])
                # append the word until it checks 'the'
    check_sentence=[]    # clearing the string again
    
print(count)


# OUTPUT

# enter the sentence :The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day
# 7