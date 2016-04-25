guess_me=7
start=1
while start<=7:
    start+=1
    if start<guess_me:
        print("too low")
    elif start==guess_me:
        print("found it")
    else:
        print("oops")
        break
