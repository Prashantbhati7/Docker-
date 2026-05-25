# Without volumes, containers are basically temporary sandboxes.

## The Core Problem
    Suppose you run:
        docker run ubuntu
    Inside container:
        echo "hello" > test.txt
    Now stop and remove container:
        docker rm container_id

    Your file is gone.
    Why?
    Because container filesystem is temporary.

    ## Now Imagine:
        - PostgreSQL container
        - MySQL container
        - MongoDB container
    If container dies and all data disappears:
    your database becomes useless.

    So Docker needed persistent storage.
    That is what volumes solve.

## What is a Docker Volume?

    persistent storage managed by Docker outside container filesystem.
    Meaning:
        -  data survives container deletion
        - multiple containers can use it
        - isolated from container lifecycle
    
    # Without volume:

        Container storage
            ↓
        Container deleted
            ↓
        Data deleted


    # With volume:

        Container
            ↓
        Volume (outside container)
            ↓
        Container deleted
            ↓
        Data still exists


## Types of Docker Storage

    | Type       | Purpose                           |
    | ---------- | --------------------------------- |
    | Volume     | Docker-managed persistent storage |
    | Bind Mount | sync local folder with container  |
    | tmpfs      | temporary RAM storage             |

## First Volume Example
    Create volume:
        docker volume create my-volume
    Check volumes:
        docker volume ls
    Inspect volume:
        docker volume inspect my-volume
    
## Mount Volume Into Container 
    Run container:
        docker run -it -v my-volume:/app ubuntu bash
    Meaning:
        my-volume → mounted at /app inside container

    Now inside container:
        cd /app
        echo "hello" > test.txt
        Exit container.
    
## Run Another Container Using Same Volume
    docker run -it -v my-volume:/app ubuntu bash
        Now:
            cat /app/test.txt
        You'll still see:
            hello
        Even though previous container died.
        That's persistence.
## Why Volumes Matter So Much
    This is how databases work in Docker.
    Example:
        docker run -v postgres-data:/var/lib/postgresql/data postgres
        Database files stored in volume.
    Now:
        container can crash
        container can be recreated
        but data survives.

## Bind Mounts

    Suppose your local project:
        my-app/
        ├── app.js

    You want:
        edit locally
        container instantly sees changes
        
    Use bind mount:
        docker run -v $(pwd):/app node:20
    Meaning:
        Current local folder ↔ /app inside container
        Now both are synced.

## Real Development Workflow
Without bind mount:
    edit code
        ↓
    rebuild image
        ↓
    rerun container
    Very slow.
    With bind mount:
    edit code locally
        ↓
    container sees instantly
This is how modern dev setup works.

## Docker now also supports explicit syntax:
        --mount type=bind,...
    and:
        --mount type=volume,...
    This is cleaner and less ambiguous.

    Example:
    # Bind
        docker run --mount type=bind,source=$(pwd),target=/app ubuntu
    # Volume
        docker run --mount type=volume,source=my-volume,target=/app ubuntu

## Some Important Points 
    When you do:
        -v my_vol:/data

    Docker only persists:
        whatever exists inside /data
        NOT the whole container filesystem.

   ## What Actually Happens
    Remember container filesystem structure:
        Container Filesystem
        ├── /bin
        ├── /etc
        ├── /usr
        ├── /app
        ├── /data
        └── ...
    When you mount:
        -v my_vol:/data
    Docker says:
        "Replace /data inside container with external persistent storage."
        Only that path becomes persistent.