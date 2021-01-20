def isPalindrome(s:str)->bool:
    k=[]
    for i in s:
        if i.isalnum()==True:
            k.append(i.lower())
    while len(k)>1:
        if k.pop(0) != k.pop():
            return False
    return True







str="A man, a plan, a canal: Panama"
print(isPalindrome(str))