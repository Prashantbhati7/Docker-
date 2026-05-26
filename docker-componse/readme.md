## A config file to make your task of managing and running containers easy.
        Get rid of repetitive commands
        All the services inside the config file, share same network commands:
    docker-compose up/down
    -d detach mode
    -v to remove networks/volumes upon stop
    --build to again build image and run

## need for docker compose ? 
    when you want to create multiple container in order to run an application for example in docker networking we connect multiple container with each other example our code use mysql database now we need to create a container for our app image and one my mysql 

    -- another example suppose we are using redis container mongoose container and our app is using both of them , then you neet to create each container seperately , so instead of creating contianers sepaerately we can up multiple containers in one go using docker-compose file 


# Format of the docker-compose file 

services:
	<some-name>:
		image:’<image-name>:<versioin>’
		environment:
			- <variable1> : “<value-of-env1>”
			- <variable2> : “<value-of-env2>”
		container_name:”<container-name>”


