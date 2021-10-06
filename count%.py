#you have a football field that  is 92 meter long and
#48.8 meter wide, find out the area 
x="atacagatagctagctagcgatagctagctgatcgatcg"
def ncbi(x):
    
    length=0
    for i in x:
        length+=1
        if(i==length):
            length=i;
    word=0
    g=0
    a=0
    t=0
    c=0
    for word in x:
        if word == "g":
            g+=1
        if word =="a":
            a+=1
        if word =="c":
            c+=1
        if word =="t":
            t+=1
   
    gc=0
    at=0
    for i in x:
        if i =="g" or i== "c":
            gc+=1
        if i=="a" or i=="t":
            at+=1
    GC=(gc)*100/(a+t+c+g)
    AT=100-(GC)
    result=(length,g,a,c,t,gc,at,AT,GC)
    print(result)


