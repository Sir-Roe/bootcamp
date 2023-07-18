"is2 Thi1s T4est 3a"

def order(sentence):

    words =list(range(1,len(sentence.split())+1))
    for word in sentence.split():
        for c in word:
            if c.isnumeric():
                words[(int(c)-1)]= word
                print(words)
                
    

    return ' '.join(words)

print(order("4of Fo1r pe6ople g3ood th5e the2"))
#sentence = "4of Fo1r pe6ople g3ood th5e the2"

