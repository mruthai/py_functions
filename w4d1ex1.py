
#exercise 1


words = ['this' , 'is', 'a', 'sentence', '.']

def reverse(words):
   
    left = 0 
    right = len(words) - 1 
    
    while left <= right:   
        
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
        
    rev_str = [i[9::-1] for i in words]
    return rev_str


print(reverse(['this' , 'is', 'a', 'sentence', '.']))
print(words)
# this isn't in place if we print 