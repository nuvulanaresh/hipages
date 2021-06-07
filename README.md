**Introduction:**
This Apache Spark build pipeline processes data of user activity from one of the highly visted websites. The source data consists of user activity on website and the most frequently visited places. 

**Prerequisite** : 
Docker installed

Below steps explain how to execute the Python data pipeline.  

1.Open a new command line session, download and run Docker image jupyter/pyspark-notebook.  
docker run -p 8888:8888 jupyter/pyspark-notebook (may take some time for image to download)

2.In another new command line session, clone the git repo or download the zip file. 
https://github.com/nuvulanaresh/hipages.git

3.Copy the source_event_data.json and the build python file from the git repo to the docker container. 
docker cp hipages/hipages_user_activity_analysis.py d9a9805c40af:/home/jovyan/work
docker cp source_event_data.json d9a9805c40af:/home/jovyan/work

4.Below command will show you all the running containers with CONTAINER ID.  
docker container ls
 
5.Use the CONTAINER ID to attach to the bash shell inside the container. 
docker exec -it <CONTAINER_ID> bash

6.Now you should be connected to a bash prompt inside of the container like below. 
Example: Here d9a9805c40af is CONTAINER ID. 
$ docker exec -it d9a9805c40af bash
jovyan@d9a9805c40af:~$ pwd
/home/jovyan

7.Go to below directory in the container. 
cd /home/jovyan/work

8.Execute below command to trigger the data pipeline. 
/usr/local/spark/bin/spark-submit hipages_user_activity_analysis.py

9.Once the pipeline is completed. You will see two folders created @ /home/jovyan/work. 
10.Directories user activity and hrly_granular_activity have the required csv datasets as requested in the requirements. 
