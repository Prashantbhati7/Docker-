import pymysql


# pull mysql image from dockerhub 
# create table and set password while creating container from that image 
# docker pull mysql
# docker run -d --env MYSQL_ROOT_PASSWORD='root' --env MYSQL_DATABASE='userinfo' mysql 
# docker inspect <container-name>    // inspect the ip address of the container 

def create_connection():
    return pymysql.connect(
        host="172.17.0.2",  # now to connect with other container we need to give that container's ip address 
        user="root",
        password='root'                     # password and database of the container that contain mysql 
        ,database='userinfo'
        )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS names (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(255) NOT NULL
                   ) """ )
    connection.commit()
    cursor.close()

def insert_data(connection,name):
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
    connection = create_connection()
    create_table(connection)
    print("1: ADD a name ")
    print("2: show all names ")
    print("3 : quit ")
    while (True):
        choice = int(input("Enter your choice : "))

        if choice == 1:
            name = input("Enter the name : ")
            insert_data(connection,name)   
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