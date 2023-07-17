org_string = 'eNGINEER devOps is hArSh'
print("Original String: ", org_string)
reverse_string = org_string.split()[::-1]
swapped_list = []
for i in reverse_string:
    for c in i:
        if(ord(c) >= 97 and ord(c) <= 122):
            i = i.replace(c, chr(ord(c) - 32))
        elif(ord(c) >=65 and ord(c) <=90):
            i = i.replace(c, chr(ord(c) + 32))
    swapped_list.append(i)
swapped_list = " ".join(swapped_list)
print("Reversed String: ", swapped_list)