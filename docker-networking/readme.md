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