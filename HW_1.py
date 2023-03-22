###################################
#             Q1                  #
###################################

def my_func(x1, x2, x3):
    if type(x1) == int or type(x2) == int or type(x3) == int:
        print('Error: parameters should be float')
    elif type(x1) != float or type(x2) != float or type(x3) != float:
        print('None')
    elif x1 + x2 + x3 == 0.0:
        print('Not a number – denominator equals zero')
    else:
        print(float((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3))

my_func(-1.0, 'a' , 2.0)


###################################
#             Q2                  #
###################################

def revword(word:str):
    word = word[::-1].lower()
    return word

def countword():
    txt = open("C:\\Users\\YaelD\Desktop\\text.txt")
    dict = {}
    for line in txt:
        line = line.rstrip('\n').split()
        if len(line) == 1:
            word = line[0].lower()
            dict[word] = dict.get(word, 0) + 1
        for one_word in line:
            if one_word == word:
                continue
            rev_low_word = revword(one_word)
            dict[rev_low_word] = dict.get(rev_low_word, 0) + 1
    return dict[word]


print(countword())

