print("Spanish Conjugation Calculator!")
print("")
print("--Preterite Tense--")
print("(Simple Past Tense)")

word = input("Enter a word:")

ar = "ar"
er = "er"
ir = "ir"


if ar in word:
    print("yo ----------- e     nosotros ----------- amos")
    print("tu ----------- aste  vosotros ----------- asteis")
    print("el,ella, Ud. - o     ellos, ellas, Uds. - aron")
    selectedItem = input("Select one from the following:")
    if selectedItem == "yo":
        conjugatedWord = word.replace(ar, 'e')
        print(conjugatedWord)

    if selectedItem == "tu":
        conjugatedWord = word.replace(ar, 'aste')
        print(conjugatedWord)

    if selectedItem == "el" or "ella" or "Ud.":
        conjugatedWord = word.replace(ar, 'o')
        print(conjugatedWord)
        
    if selectedItem == "nosotros":
        conjugatedWord = word.replace(ar, 'amos')
        print(conjugatedWord)
    if selectedItem == "vosotros":
        conjugatedWord = word.replace(ar, 'asteis')
        print(conjugatedWord)
    if selectedItem == "ellos" or "ellas" or "Uds.":
        conjugatedWord = word.replace(ar, 'aron')
        print(conjugatedWord)
    