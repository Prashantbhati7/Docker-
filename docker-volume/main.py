
user_name = input("enter user name to store into the file or enter or proceed ")

if user_name != "":
    with open('./data/user_info.txt','a') as file :
        file.write(user_name + "\n")

show_names = input("do you want to see the names of the users in file ? [y/n]")

if show_names =='y':
    try:
        with open('./data/user_info.txt','r') as file :
            content = file.readlines()
    except Exception as e:
        print(e,type(e))
    else :
        for names in content :
            print(names.strip())    



#  Now you need to create a docker image and mount volume to the /myapp/data now anything written from anycontainer 
#  to data will be written into volume and it is shared withing all the containers 
#  now this volume is shared within the containers and written data is persistant even if container is killed 


#  commands 

# docker build -t myimage .
# docker run -it -v myvol:/myapp/data myimage 