import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        mystr = s.lower()
        
        
        mystr  = ''.join(mystr.split())
        mystr = ''.join(ch for ch in mystr if ch not in string.punctuation)
        reversd ='' 

        for i in range(len(mystr)-1,-1,-1):
            if mystr[i] in string.punctuation:
                continue
            reversd += mystr[i] 
        print(reversd)
        for j in range (len(reversd)):
            if mystr[j] == reversd[j]:
                print(mystr[j],reversd[j])
                continue
            else:
                return False
                
        return True

        