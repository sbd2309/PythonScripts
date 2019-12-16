def piglatin(word):
    result=word[0] in 'aeiou'
    if result==True:
        
        new_word=word+"ay"
        
    else:
        
        new_word=word[1:]+word[0]+"ay"
    return new_word    
piglatin("apple") 
