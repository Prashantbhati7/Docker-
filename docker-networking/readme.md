# Important Foundation: Containers Are Isolated

## A container is NOT just:
        "a process"
    It has isolated:
        filesystem
        process tree
        network stack
    That last one matters here.

    Each container gets:
        its own IP
        its own ports
        its own network namespace
    Meaning:
    Inside container:   
        localhost
    refers to THAT container only.

    Not:
        your laptop
        another container
    
    Container gets its own:
        interfaces
        routing table
        ports
        localhost
    So two containers can both run:
        port 3000
    without conflict.
    Because each has separate network namespace.

## we can create network of containers and container's in that network can communicate and connect with each other 

## commands 

docker create network <network-name>
docker run -d <container1-name> --network <network-name>
docker run -d <container2-name> --network <network-name>

now these containers can communicate with each other
