def add_name():
   name = input("enter name to store into volume")
   with open('./data/user_info.txt','a') as file :
        file.write(name + "\n")

def show_names():
    try:
        with open('./data/user_info.txt','r') as file :
            content = file.readlines()
    except Exception as e:
        print(e,type(e))
    else :
        for names in content :
            print(names.strip())    


def main():
    print("1: ADD a name ")
    print("2: show all names ")
    print("3 : quit ")
    while (True):
        choice = int(input("Enter your choice : "))

        if choice == 1:
            add_name()
        elif choice == 2:
            show_names()
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

            