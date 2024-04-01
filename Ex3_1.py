def factors(num):
    '''returns a list of the factors of num''' 
    factorList = []
    for i in range(1,num+1):
        if num % i == 0: 
            factorList.append(i)
    return factorList


def gcf(num1, num2):
    l1 = factors(num1)
    l2 = factors(num2)

    gcf = max(set(l1) & set(l2))

    return gcf

print(gcf(60, 48))
