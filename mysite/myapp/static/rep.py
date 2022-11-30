with open("GLTFLoader.js","r") as f:
    text = f.read()
    #print(text)
    #print(type(text))

with open("termes.txt","r") as g:
    terms = g.read()
    K = terms[1:-1].split(",")
    
L=['AnimationClip']
for words in K[1:]:
    L+=[words[2:]]
print(L)

for word in L:
    text = text.replace(" "+word," THREE."+word)

with open("GLTFLoader2.js",'w') as q:
    q.write(text)