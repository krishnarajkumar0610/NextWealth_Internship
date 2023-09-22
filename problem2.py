sentence = input("Enter a line :")

splited_words= sentence.split(" ")
final_string=""
for i in range(len(splited_words)):
    if i % 2 == 0:
        word=splited_words[i]
        for j in range(len(word)):
            let_acssi=ord(word[j])
            let_acssi+=2            
            final_string=final_string+chr(let_acssi)
        final_string+=" "
    elif i % 2 !=0:
        word=splited_words[i]
        word=word[::-1]
        for j in range(len(word)):
            let_acssi=ord(word[j])
            let_acssi+=2
            final_string=final_string+chr(let_acssi)
        final_string+=" "
        
print(final_string)


# Output

# Enter a line :I am the King
# K oc vjg ipkM 