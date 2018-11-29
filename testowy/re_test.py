import re
s = open('test.txt', 'r') 
i = re.search(r'jest.*druga', s).group()
print(i)


#To jest Released i represated , a to jest druga czesc ktorej nie chcemy wyswietlic
