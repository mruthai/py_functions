# Create a function that counts how many distinct words are in the string below, 
# then outputs a dictionary with the words as the key and the value as the amount
#  of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
comp = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

# what do we know about the parameters?
# the parameter is a 1 string of words
# What are the constraints?
# we are constrained to placing the words into a dictionary

    
# print(word_count'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'))

def dbwrd(comp):
    case = {}
    wrd = list(comp.split(","))
    wrd = "".join(wrd)
    wrd = list(wrd.split("."))
    wrd = "".join(wrd).lower()
    wrd = list(wrd.split(" "))
    for wr in wrd:
        if wr in case.keys():
            case[wr] += 1
        else:
            case[wr] = 1


    return case
    


print(dbwrd(comp))













