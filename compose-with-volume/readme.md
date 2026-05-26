# Important observations 

## 1 when we create a volume and share create mutiple images that uses the same volume the volume is shared among all the containers of all the images 
    suppose a container of image 1 writes something to a file will persist even after container is killed and can be read by container of image 2 for image 1 untill the volume is not destroyed 
    so even if the images are build freshly if the volume exists already will persists and mouted to the container 

    here in this example we created a volume my-volume and created several container isloated form each other and we saw that the containers are sharing that same mounted my-volume all were writing to that my-volume's file and also reading from it only 
    