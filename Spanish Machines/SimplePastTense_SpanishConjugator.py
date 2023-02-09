print("\n\n\n")
print("-------------------------------")
print("Spanish Conjugation Calculator!")
print("")
print("--Preterite Tense--")
print("(Simple Past Tense)")
print("-------------------------------")

word = input("Enter a word:")

ar = "ar"
er = "er"
ir = "ir"

print("-------------------------------")

if ar in word:
    lineOneA = "yo ----------- e     "
    lineOneB = "nosotros ----------- amos"
    lineTwoA = "tu ----------- aste  "
    lineTwoB = "vosotros ----------- asteis"
    lineThreeA = "el,ella, Ud. - o     "
    lineThreeB = "ellos, ellas, Uds. - aron"

    print("--Ending in AR ----------------")
    print("-------------------------------")
    print(lineOneA + lineOneB)
    print(lineTwoA + lineTwoB)
    print(lineThreeA + lineThreeB)

    conjugations = ["yo", "tu", "el, ella, Ud.",
        "nosotros", "vosotros", "ellos, ellas, Uds."]
    conjugatedWord = word

    for x in conjugations:
        match x:
            case 'yo':
                conjugatedWord = word.replace(ar, 'e')
                lineOneA = lineOneA.replace('e', conjugatedWord)
            case 'tu':
                conjugatedWord = word.replace(ar, 'aste')
                lineTwoA = lineTwoA.replace('aste', conjugatedWord)
            case 'el, ella, Ud.':
                conjugatedWord = word.replace(ar, 'o')
                lineThreeA = lineThreeA.replace('o', conjugatedWord)
            case 'nosotros':
                conjugatedWord = word.replace(ar, 'amos')
                lineOneB = lineOneB.replace('amos', conjugatedWord)
            case 'vosotros':
                conjugatedWord = word.replace(ar, 'asteis')
                lineTwoB = lineTwoB.replace('asteis', conjugatedWord)
            case 'ellos, ellas, Uds.':
                conjugatedWord = word.replace(ar, 'aron')
                lineThreeB = lineThreeB.replace('aron', conjugatedWord)

    print("-------------------------------")
    print("-------------------------------")
    print(lineOneA + lineOneB)
    print(lineTwoA + lineTwoB)
    print(lineThreeA + lineThreeB)
    

if er in word:
    lineOneA   = "yo ----------- i     "
    lineOneB   = "nosotros ----------- imos"
    lineTwoA   = "tu ----------- iste  "
    lineTwoB   = "vosotros ----------- isteis"
    lineThreeA = "el,ella, Ud. - io    "
    lineThreeB = "ellos, ellas, Uds. - ieron"

    print("--Ending in ER ----------------")
    print("-------------------------------")
    print(lineOneA + lineOneB)
    print(lineTwoA + lineTwoB)
    print(lineThreeA + lineThreeB)

    conjugations = ["yo", "tu", "el, ella, Ud.",
        "nosotros", "vosotros", "ellos, ellas, Uds."]
    conjugatedWord = word

    for x in conjugations:
        match x:
            case 'yo':
                conjugatedWord = word.replace(er, 'i')
                lineOneA = lineOneA.replace('i', conjugatedWord)
            case 'tu':
                conjugatedWord = word.replace(er, 'iste')
                lineTwoA = lineTwoA.replace('iste', conjugatedWord)
            case 'el, ella, Ud.':
                conjugatedWord = word.replace(er, 'io')
                lineThreeA = lineThreeA.replace('io', conjugatedWord)
            case 'nosotros':
                conjugatedWord = word.replace(er, 'imos')
                lineOneB = lineOneB.replace('imos', conjugatedWord)
            case 'vosotros':
                conjugatedWord = word.replace(er, 'isteis')
                lineTwoB = lineTwoB.replace('isteis', conjugatedWord)
            case 'ellos, ellas, Uds.':
                conjugatedWord = word.replace(er, 'ieron')
                lineThreeB = lineThreeB.replace('ieron', conjugatedWord)
    print("-------------------------------")
    print("-------------------------------")
    print(lineOneA + lineOneB)
    print(lineTwoA + lineTwoB)
    print(lineThreeA + lineThreeB)

if ir in word:
    lineOneA   = "yo ----------- i     "
    lineOneB   = "nosotros ----------- imos"
    lineTwoA   = "tu ----------- iste  "
    lineTwoB   = "vosotros ----------- isteis"
    lineThreeA = "el,ella, Ud. - io    "
    lineThreeB = "ellos, ellas, Uds. - ieron"

    print("--Ending in IR ----------------")
    print("-------------------------------")
    print(lineOneA + lineOneB)
    print(lineTwoA + lineTwoB)
    print(lineThreeA + lineThreeB)

    conjugations = ["yo", "tu", "el, ella, Ud.",
        "nosotros", "vosotros", "ellos, ellas, Uds."]
    conjugatedWord = word

    for x in conjugations:
        match x:
            case 'yo':
                conjugatedWord = word.replace(ir, 'i')
                lineOneA = lineOneA.replace('i', conjugatedWord)
            case 'tu':
                conjugatedWord = word.replace(ir, 'iste')
                lineTwoA = lineTwoA.replace('iste', conjugatedWord)
            case 'el, ella, Ud.':
                conjugatedWord = word.replace(ir, 'io')
                lineThreeA = lineThreeA.replace('io', conjugatedWord)
            case 'nosotros':
                conjugatedWord = word.replace(ir, 'imos')
                lineOneB = lineOneB.replace('imos', conjugatedWord)
            case 'vosotros':
                conjugatedWord = word.replace(ir, 'isteis')
                lineTwoB = lineTwoB.replace('isteis', conjugatedWord)
            case 'ellos, ellas, Uds.':
                conjugatedWord = word.replace(ir, 'ieron')
                lineThreeB = lineThreeB.replace('ieron', conjugatedWord)
    print("-------------------------------")
    print("-------------------------------")
    print(lineOneA + lineOneB)
    print(lineTwoA + lineTwoB)
    print(lineThreeA + lineThreeB)