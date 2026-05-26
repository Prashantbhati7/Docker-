import pymysql

def create_connetion():
    return pymysql.connect(
        host='mysql-container',
        user='root',
        password='root',
        database='userinfo'
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS names (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(255) NOT NULL
                   ) """ )
    connection.commit()
    cursor.close()  

def insert_name(connection,name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO names (name) VALUES (%s)",(name,))
    connection.commit()
    cursor.close()  

def fetch_all_names(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM names")
    names = cursor.fetchall()
    cursor.close()
    return names

def main():
    connection = create_connetion()
    create_table(connection)    
    print("1: ADD a name ")
    print("2: show all names ")
    print("3 : quit ")
    while (True):
        choice = int(input("Enter your choice : "))

        if choice == 1:
            name = input("Enter the name : ")
            insert_name(connection,name)   
            print(f"{name} added successfully")
        elif choice == 2:
            names = fetch_all_names(connection)
            for name in names:
                print(name[0])
        elif choice == 3:
            break
        else:
            print("Invalid choice")

    connection.close()

if __name__ == "__main__":
    main()
