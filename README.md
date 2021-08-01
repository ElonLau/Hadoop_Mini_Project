# Hadoop_Mini_Project

In this project, you will utilize data from an automobile tracking platform that tracks the history of
important incidents after the initial sale of a new vehicle. Such incidents include subsequent
private sales, repairs, and accident reports. The platform provides a good reference for
second-hand buyers to understand the vehicles they are interested in.
In this project, you will receive a dataset with a history report of various vehicles. Your goal is to
write a MapReduce program to produce a report of the total number of accidents per make and
year of the car.

# How to Reproduce
 
- follow these instructions to: https://www.youtube.com/watch?v=735yx2Eak48&ab_channel=BinodSumanAcademy 
    <br/>
1. install Oracle VM VirtualBox
2. install HortonWorks Data Platform (HDP) on Hortonworks Sandbox
3. setup accounts to use HDP on VirtualBox

- HDFS interface - http://127.0.0.1:8080/#/login
    <br/>
1. login and go to Files View
2. create a folder for this project
3. in the project folder:
4. create an input folder and upload data.csv there
5. create an empty output folder
<br/>

- Sandbox command line - http://127.0.0.1:4200/

<br/>
1. login and create a project folder with the same name as above
2. add the 4 python and 1 sh files here
3. create an input folder and add the data.csv file there
4. create an empty output folder
5. run the sh file ($ sh automobile-mr.sh)
6. check the output folder in the HDFS interface and see the 2 output subfolders are created
