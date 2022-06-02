str1 = "sos"
str2 = "oss"
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
    print("valid")
else:
    print("invalid")



