def is_anagram(x):
    y = 0
    for i in x[0]:
        y = x[1].find(i) 
        if y == -1 :
            return False
        else :
            return True
is_anagram(["listen","silent"])