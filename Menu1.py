def addstr(s,lst):
    


while True:
    strlst = input("Enter a new string (enter stop to quit): ").split(" ")
    strlst = strlst.lower()
    if strlst == 'stop':
        break
    
    for s in strlst:
        lst = addstr(s,lst)

    print(lst)