def checkMagazine(magazine, note):
    magazine.sort();
    note.sort();
    for word in note:
        if word not in magazine:
            print("No")
            return
        else:
            magazine.remove(word);
    print("Yes")
