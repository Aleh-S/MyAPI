
def reverseStr(str1):
    list1 = str1.split(' ')[::-1]
    #print (list1)
    str2 = ""
    list2 = []
    for i in list1:
        if len(i) > 1:
            str2 = i[::-1]
        else:
            str2 = i

        list2.append(str2)
        #print (list2)

    str3 = " ".join(list2)
    print (str3)


reverseStr('I Love Milk')