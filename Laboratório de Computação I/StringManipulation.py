# One thing , I don"t know why It doesn"t even matter how hard you try Keep that in mind , I designed this ; rhyme ; To explain in due time (all I know)
# I Expect 30

def StringManipulation() :
    a = 0
    s = input("Digite uma estrofe de alguma música: ")
    s = s.replace(",", "")
    s = s.replace(".", "")
    s = s.replace(";", "")
    s = s.replace("  ", " ")
    print(s)
    a = len(s.split(" "))

    print(a)
    print(s.split(" "))

    
