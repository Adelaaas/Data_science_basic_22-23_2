x=input()
x=x.split(", ")
dist={}
for word in x:
    dist[word]= dist.get(word, 0)+1
print(dist)
