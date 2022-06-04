str1 = input("Enter first word:")
str2 = input("Enter second word:")
dict1 = {}
dict2 = {}
for element in str1:
    if element not in dict1:
        dict1[element] = 1
    else:
        dict1[element] = dict1[element] + 1
for element in str2:
    if element not in dict2:
        dict2[element] = 1
    else:
        dict2[element] = dict2[element] + 1

if dict1 == dict2:
    print("you entered valid ANAGRAM")
else:
    print("its NOT a pair of anagram")


