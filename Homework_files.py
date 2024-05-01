def myFunc(x):
    return len(x)
with open('1.txt', 'r', encoding='utf-8') as f:
    list_text1 = []
    for i in f:
        # print(i.strip())
        list_text1.append(i.strip())
    list_text1.append('1.txt')
print(list_text1)
with open('2.txt', 'r', encoding='utf-8') as f:
    list_text2 = []
    for i in f:
        # print(i.strip())
        list_text2.append(i.strip())
    list_text2.append('2.txt')
print(list_text2)
with open('3.txt', 'r', encoding='utf-8') as f:
    list_text3 = []
    for i in f:
        # print(i.strip())
        list_text3.append(i.strip())
    list_text3.append('3.txt')
print(list_text3)
text_123 = [list_text1, list_text2, list_text3]
text_123.sort(key=myFunc)
# print(whole_text)
with open('123.txt', 'w', encoding='utf-8') as f:
    for j in text_123:
        f.write(j[-1])
        f.write('\n')
        f.write(str(len(j)-1))
        f.write('\n')
        for k in range(len(j)-1):
            f.write(j[k])
            f.write('\n')

