This Apache Spark build pipeline processes data of user activity from one of a website. To execute the pipeline below steps are needed
Download Docker Image jupyter/pyspark-notebook. 
docker run -p 8888:8888 jupyter/pyspark-notebook
docker container ls
This command will show you all the running containers. Find the CONTAINER ID of the container running the jupyter/pyspark-notebook image and use it to connect to the bash shell inside the container:
docker exec -it <container_id> bash
Now you should be connected to a bash prompt inside of the container
