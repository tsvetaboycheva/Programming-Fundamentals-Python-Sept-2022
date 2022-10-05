string = input()
while string != "End":
    if string=="SoftUni":
        pass
    else:
        text=""
        for i in string:
            text+=(i*2)
        print(text)
    string = input()
