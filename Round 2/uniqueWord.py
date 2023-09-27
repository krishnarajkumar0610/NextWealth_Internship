# Last spring, my tween was begging for more independence, starting with being allowed to walk home from school alone.
# The mile-plus walk involves crossing a few busy streets. I was hesitant; she doesn’t have a phone, 
# so she had no way to contact me if something went wrong. But we practiced a few times (with me trailing her a block behind)
# to be sure she was confident of the route and talked about what she would do in various scenarios.
# Then, we allowed her to do something that some parents in our


def check(word,words):
    if word in words:
        return True
    return False

sentence = input("Enter your sentence : ")  # asking input

sentence = sentence.split(" ")  # spliting it into list by spacing

final_list=[]

for i in range(len(sentence)):  # to traverse the list
    if not check(sentence[i],final_list):
        final_list.append(sentence[i])
    else:
        continue
print(f"Unique list : {final_list}")