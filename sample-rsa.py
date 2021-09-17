def base256toint(L):
    total = 0
    L.reverse()
    for i in range(len(L)):
        total = total + L[i]* (256**i)
    return total


def stringtoint(s):
    base256 = [ord(c) for c in s]
    M = base256toint(base256)
    return M

def baseexpansion(n,b):
    q = n
    digit_list= []
    while q !=0:
        digit_list.append(q % b)
        q = q // b
    digit_list.reverse()
    return digit_list

def inttostring(M):
    L = baseexpansion(M,256)
    message = ''
    for digit in L:
        message = message + chr(digit)
    return message
