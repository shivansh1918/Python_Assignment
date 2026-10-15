# data="shivansh vashishth"
# count_vowel=0
# for i in data:
#     if i in "aeiouAEIOU":
#         print(i)
#         count_vowel+=1

# print("vowels:",count_vowel)
data="shivansh vashishth"
i=0
count=0
while i<len(data):
    if data[i] in "aeiou":
        count+=1
    i+=1
print("vowel:",count)