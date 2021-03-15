
name_list=[]


while True:
    name = input("შეიყვანე სახელი: ")
    if name:
        name_list.append(name)
        print(f"სახელი {name} შეყვანილია {name_list.count(name)}_ჯერ.")
    elif name == "":
        print("მორჩა კინო")
        break
