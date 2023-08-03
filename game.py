f=open('poem.txt','w')
f.write("hello word")
f.close()

f1=open("poem.txt")
t=f1.read()
if 'word' in t:
    print("yesss!")
else:
    print("nooo")

f1.close()