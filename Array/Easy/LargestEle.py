list = [23,54,75,66,98,12]

Largest =  float('-inf')

for x in list:
    if x > Largest:
        Largest = max(x,Largest)

print(Largest)