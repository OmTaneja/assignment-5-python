def word_count(list):
    counts = dict()
    for word in list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

c = int(input("Enter length of list :-  "))
b = []
for i in range(c):
    a = input("Enter list element :-  ")
    b.append(a)


print( word_count(b))