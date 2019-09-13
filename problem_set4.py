#filename: problem_set4.py

import string

#problem 1
def p1():
    lis = ['a', 'b', 'c']
    elis = [6, 9, 3]
    return {lis[i]:elis[i] for i in range(len(lis))}
#print(p1())

#problem 2
def p2():
    return sum(list(p1().values()))/len(p1())
# print(p2())

#problem 3
def p3():
    dic = {'a1':12, 'a2':30, 'b1':23, 'b2':45, 'c1':18, 'c2':25}
    alp = string.ascii_lowercase
    adic = {}
    for let in alp:
        count = 0
        total = 0
        for key in dic:
            if not key.startswith(let):
                continue
            count += 1
            total += dic[key]
            adic.update({let:round(total/count)})
    return adic
print(p3())

        
    
        
    

            

        