List = [12,37,5,42,8,3]
even=[]
odd=[]
while len(List)>0:
    List=List.pop()
    if (List % 2==0):
        even.append(List)
    else:
        odd.append(List)
        
