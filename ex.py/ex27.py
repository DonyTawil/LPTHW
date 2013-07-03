a=(True and True) #True
b=(False and True) #false
c=(1==1 and 2==1) #false
d=("test"=="test")#true
e=(1 == 1 or 2 !=1 )#true
f=(True and 1 == 1)#true
g=(False and 0 != 0)#false
h=(True or 1 == 1)#true
i=("test" == "testing")#false
j=(1 !=0 and 2==1)#false
k=("test" != "testing")#true
l=("test" == 1)#0
m=(not (True and False))#1
n=(not (1 == 1 and 0 !=1))#0
o=(not (10 == 1 or 1000 == 1000))#0
p=(not (1 != 10 or 3 == 4))#false
q=(not ("testing" == "testing" and "Zed" == "cool guy"))#1
r=(1 == 1 and not ("testing" == 1 or 1==0))#1
s=(("chunky" == "bacon") and not (3==4 or 3==3))#0
t=(3==3 and not ("testing" == "testing" or "Python"=="fun"))#0
print(a,'\n', b,'\n', c,'\n',d,'\n',e,'\n',f,'\n',g,'\n',h,'\n',i,'\n',j,'\n',k,'\n',l,'\n',m,'\n',n,'\n',o,'\n',p,'\n',q,'\n',r,'\n',s,'\n',t)
