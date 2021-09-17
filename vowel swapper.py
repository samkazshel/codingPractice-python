def vowel_swapper(string):

    # ==============
    # Your code here
    swap_dic= {'a':'4', 'e':'3','i':'!','o':'000','u':'|_|' }

    for char in string:
        if char in swap_dic.keys():
            string= string.replace(char,swap_dic[char])
    
    return string

        

    # ==============

print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console