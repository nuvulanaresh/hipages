Introduction:
This Apache Spark build pipeline processes data of user activity from one of the highly visted websites. The source data consists of user activity on website and the most frequently visited places. 
Below steps detail the execution part of the pipeline

1.Download Docker image jupyter/pyspark-notebook. 
docker run -p 8888:8888 jupyter/pyspark-notebook (may take some time for image to download)

2.This command will show you all the running containers along with CONTAINER ID.
docker container ls
 
3. Use the CONTAINER ID to attach to the bash shell inside the container:
docker exec -it <CONTAINER_ID> bash
Now you should be connected to a bash prompt inside of the container like below

Example: Here d9a9805c40af is CONTAINER ID
$ docker exec -it d9a9805c40af bash
jovyan@d9a9805c40af:~$ pwd
/home/jovyan

4. In another command line session clone the git repo or download the zip file 

Repo: https://github.com/nuvulanaresh/hipages.git
With Docker installed as a prerequisite, run the below command

docker run -p 8888:8888 jupyter/pyspark-notebook
In another tab please run the below command
docker ps (Will list the actively running containers with container id. In below command d9a9805c40af is container id)
Copy the python file and json source data to the container from host machine
docker cp hipages/hipages_user_activity_analysis.py d9a9805c40af:/home/jovyan/work
docker cp source_event_data.json d9a9805c40af:/home/jovyan/work
