a = [10,20,30,20,10,50,60,40,80,50,40]

lesser = 1
a.sort()
for i in range(len(a)-lesser):
    if a[i+1] == a[i]:
        a.remove(a[i])
        lesser += 1
       
