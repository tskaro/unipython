from projects.try_except.tskaromodules import divide, square

while True:
    print('lets divide:')
    result, status = divide(int(input("Type number 1:")), int(input("Type number 2:")))
    if status == True:
        print(result)
        break
    elif status == False:
        print(result)

while True:
    print('lets square:')
    result, status = square(int(input("Type number 1:")), int(input("Type number 2:")))
    if status == True:
        print(result)
        break
    elif status == False:
        print(result)
