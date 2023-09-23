sentence = input("Enter a line :")  # asking the user to give a sentence

splited_words= sentence.split(" ")  # spliting it and stored in another variable
final_string="" # declaring the another string
for i in range(len(splited_words)): # this loop for traverse the list
    if i % 2 == 0:  # if i % 2 is 0 then it is even
        word=splited_words[i]   # storing the word in word variable
        for j in range(len(word)):  # traversing into the word 
            let_acssi=ord(word[j])  # converting characters into numbers
            let_acssi+=2            # adding +2 with it 
            final_string=final_string+chr(let_acssi)    # strong in final string with number convert into char
        final_string+=" "   # adding space to it
        
    elif i % 2 !=0:     # if i % 2 not equal to 0
        word=splited_words[i]   # storing word in word varibale
        word=word[::-1] # reversing the word
        for j in range(len(word)):  # traversing into the word
            let_acssi=ord(word[j])  # converting evry chars into numbers
            let_acssi+=2    # adding + 2 with every chars
            final_string=final_string+chr(let_acssi)     # strong in final string with number convert into char
        final_string+=" "   # adding space to it
        
print(final_string) # displaing the final string


# Output

# Enter a line :I am the King
# K oc vjg ipkM 