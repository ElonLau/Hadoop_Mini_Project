# Hadoop_Mini_Project

In this project, you will utilize data from an automobile tracking platform that tracks the history of
important incidents after the initial sale of a new vehicle. Such incidents include subsequent
private sales, repairs, and accident reports. The platform provides a good reference for
second-hand buyers to understand the vehicles they are interested in.
In this project, you will receive a dataset with a history report of various vehicles. Your goal is to
write a MapReduce program to produce a report of the total number of accidents per make and
year of the car.

# How to Reproduce
https://www.youtube.com/watch?v=735yx2Eak48&ab_channel=BinodSumanAcademy - follow these instructions to:
install Oracle VM VirtualBox
install HortonWorks Data Platform (HDP) on Hortonworks Sandbox
setup accounts to use HDP on VirtualBox
HDFS interface - http://127.0.0.1:8080/#/login
login and go to Files View
create a folder for this project
in the project folder:
create an input folder and upload data.csv there
create an empty output folder
Sandbox command line - http://127.0.0.1:4200/
login and create a project folder with the same name as above
add the 4 python and 1 sh files here
create an input folder and add the data.csv file there
create an empty output folder
run the sh file ($ sh automobile-mr.sh)
check the output folder in the HDFS interface and see the 2 output subfolders are created
