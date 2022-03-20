str1 = 'О сколько нам открытий чудных готовит просвященья дух'
lst1 = str1.split()
print(lst1)
lst2 = []
for word in lst1:
    if len(word) < 5:
        lst2.append(word)
    else:
        word1 = ''.join([word[-i-1] for i in range(len(word))])
        lst2.append(word1)
str2 = ' '.join(lst2)
print(str2)

