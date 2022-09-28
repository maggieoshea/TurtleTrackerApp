#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#Copy and paste a line of data as the lineString variable value
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

#Use the split command to parse the items in lineString into a list object
lineData = lineString.split(    ) 

#Assign variables to specific items in the list
record_id = lineData[0] #ARGOS tracking record ID
obs_date = lineData[2] #Observation Date
obs_lc = lineData[4] #Observation Location Class
obs_lat = lineData[6] #Observation latitude 
obs_lon = lineData[7] #Observation Longitude 

#print information to the use
print(f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

#%%


### Task 3 ####
#Create a variable pointing to the data file
file_name="Data/raw/Sara.txt"

#Create a file object from the file 
file_object = open(file_name, "r")

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Pretend we read one line of data from the file
lineString = line_list[100]

#Split the string into a list of data items
lineData = lineString.split(    )

#Extract items in list into variables 
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData [7]

#Print the location of sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon: {obs_lon} on {obs_date}")

#%%
