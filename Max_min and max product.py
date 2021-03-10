#max_min Composition module:
r=eval(input("number of terms in first fuzzy set"))
s=eval(input("Number of terms in second Fuzzy set"))
t=eval(input("number of terms in third fuzzy set"))

#first matrix
l=[]
k=[]
for i in range(0,r):
  for j in range(0,s):
    l.append(eval(input()))
  k.append(l)
  l=[]
print(k)

#second matrix
l=[]
p=[]
for i in range(0,s):
  for j in range(0,t):
    l.append(eval(input()))
  p.append(l)
  l=[]
print(p)

#transpose
d=[]
l=[]
for i in range(0,s):
  for j in range(0,t):
    l.append(p[j][i])
  d.append(l)
  l=[]
print(d)

#max_min composition
dummy=[]
final_result=[]
final_res=[]
for i in range(0,r):
  for j in range(0,t):
    x=k[i]
    y=d[j]
    for n in range(0,len(x)):
      dummy.append(min(x[n],y[n]))
    maa=max(dummy)
    dummy=[]
    final_res.append(maa)
  final_result.append(final_res)
  final_res=[]
print(final_result)

#max product composition
pdummy=[]
pfinal_result=[]
pfinal_res=[]
for i in range(0,r):
  for j in range(0,t):
    x=k[i]
    y=d[j]
    for n in range(0,len(x)):
      pdummy.append(round(x[n]*y[n],2))
    pmaa=max(pdummy)
    pdummy=[]
    pfinal_res.append(pmaa)
  pfinal_result.append(pfinal_res)
  pfinal_res=[]
print(pfinal_result)
