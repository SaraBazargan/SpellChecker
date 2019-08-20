import codecs, re

fp1 = open('data.txt', 'r', encoding = 'utf8')
txt = fp1.readlines()
list1 = []
list2 = []
for line in txt:
    text = re.findall('[\200c&ا-ي&گ&پ&ژ&چ&ی&آ&ک]+', line)
    list2.append(text)
    for word in text:
        for char in word:
            list1.append(char)
        list1.append('_')
print(len(list1))
fp1.close()



fp3 = open('normal_data.txt', 'w', encoding = 'utf8')
for i in list2:
    for word in i:
        fp3.write(word+' ')
    fp3.write('\n')
    


fp4 = open('with_error_data.txt', 'r', encoding = 'utf8')
txt2 = fp4.readlines()
list3 = []
for line in txt2:
    text2 = re.findall('[\200c&ا-ي&گ&پ&ژ&چ&ی&آ&ک]+', line)
    for word in text2:
        for char in word:
            list3.append(char)
        list3.append('_')
print(len(list3))
fp4.close()

fp2 = open('data_data.txt', 'w', encoding = 'utf8')
for i in range(len(list3)):
    fp2.write(list1[i]+' '+list3[i]+'\n')
fp2.close()
fp3.close()
