def countChar(s):
    characters = {}
    for i in s:
        if i not in characters:
            characters[i]=1
        else:
            characters[i]=characters[i]+1
    c=0
    for i in sorted(characters, key=characters.get, reverse=True):
        if(c<3):
            print(i+" "+str(characters[i]))
            c+=1
        else:
            break
