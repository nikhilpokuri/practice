print(any([1==0,1<2,1>10]))#returns True if any of it is correct
print(all([1==1,1<2,1!=-10]))#returns True if all of it is correct
print(all([i>0 for i in [1,3,2,9,-10]]))
