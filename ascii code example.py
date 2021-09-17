character = raw_input('Input a printable character: ')
acharacter = ord(character)
bits = ''
mask = 1
for i in range(7):
    if(acharacter & pow(2,i) == 0):
        bits = '0' + bits
    else: 
        bits = '1' + bits
    mask <<= 1
print 'The character %c has a decimal ascii code of %d\n and a 7 bit binary code of %s' % (character,acharacter,bits)
