L = 'paaabbccccdaakkkkkl'
count = 1
result = ''
for i in range(len(L)):
    if i < len(L)-1 and L[i] == L[i+1]:
        count += 1
    else:
        result += (L[i] + str(count))
        count = 1

print(result)