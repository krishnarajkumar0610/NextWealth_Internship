sentence = input("enter the sentence :")

splited_words= sentence.lower()

splited_words=splited_words.split(" ")

first_word="the"
middle_letter="a"
last_word="the"
check_sentence=[]
count=0
def check(index,check_sentence , middle_letter):    
    for i in range(index,len(check_sentence)):
        return True
    return False
for i in range(len(splited_words)):
    if splited_words[i] in first_word:
        check_sentence.append(splited_words[i])
        for j in range(i+1,len(splited_words)):
            if splited_words[j] in last_word:
                check_sentence.append(splited_words[j])
                if not check(i,check_sentence,middle_letter):
                    count+=1
            else:
                check_sentence.append(splited_words[j])
    check_sentence=[]
    
print(count)