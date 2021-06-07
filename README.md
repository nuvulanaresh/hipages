This Apache Spark build pipeline processes data of user activity from one of a website. To execute the pipeline below steps are needed
Download Docker Image jupyter/pyspark-notebook. 
docker run -p 8888:8888 jupyter/pyspark-notebook
docker container ls
This command will show you all the running containers. Find the CONTAINER ID of the container running the jupyter/pyspark-notebook image and use it to connect to the bash shell inside the container:
docker exec -it <container_id> bash
Now you should be connected to a bash prompt inside of the container


Steps 
Clone git repo or download the zip file 
Repo: https://github.com/nuvulanaresh/hipages.git
With Docker installed as a prerequisite, run the below command

docker run -p 8888:8888 jupyter/pyspark-notebook
In another tab please run the below command
docker ps (Will list the actively running containers with container id. In below command d9a9805c40af is container id)
Copy the python file and json source data to the container from host machine
docker cp hipages/hipages_user_activity_analysis.py d9a9805c40af:/home/jovyan/work
docker cp source_event_data.json d9a9805c40af:/home/jovyan/work
