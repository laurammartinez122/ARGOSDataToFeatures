##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2020
## Author: laura.martinez@duke.edu (for ENV859)
##---------------------------------------------------------------------

#%% Import packages
import arcpy, sys, os

#%% Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

#%% Construct a while loop to iterate through all lines in the datafile
# Open the ARGOS data file for reading
inputFileObj = open(inputFile,'r')

# Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()

# Start the while loop
while lineString:
    
    # Set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString):
        
        # Parse the line into a list
        lineData = lineString.split()
        
        # Extract attributes from the datum header line
        tagID = lineData[0]
        
        # Extract location info from the next line
        line2String = inputFileObj.readline()
        
        # Parse the line into a list
        line2Data = line2String.split()
        
        # Extract the date we need to variables
        obsLat = line2Data[2]
        obsLon= line2Data[5]
        
        # Print results to see how we're doing
        print (tagID,"Lat:"+obsLat,"Long:"+obsLon)
        
    # Move to the next line so the while loop progresses
    lineString = inputFileObj.readline()

#%% Challenge
# Open the ARGOS data file for reading
inputFileObj2 = open(inputFile,'r')

# Get the first line of data, so we can use a while loop
lineString2 = inputFileObj2.readline()

# Start the while loop
while lineString2:
    
    # Set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString2):
        
        # Parse the line into a list
        lineData2 = lineString2.split()
        
        # Extract attributes from the datum header line
        tagID = lineData2[0]
        
        # Extract location info from the next line
        line2String2 = inputFileObj2.readline()
        
        # Parse the line into a list
        line2Data2 = line2String2.split()
        
        # Extract the date we need to variables
        obsLat = line2Data2[2]
        obsLon= line2Data2[5]
        date = line2Data2[1]
        time = line2Data2[2]
        location = line2Data2[3]
        
        # Print results to see how we're doing
        print (tagID,"Lat:"+obsLat,"Long:"+obsLon + "Date:"+date, "Time:"+time, "Location Class:"+location)
        
    # Move to the next line so the while loop progresses
    lineString = inputFileObj.readline()
    
#Close the file object
inputFileObj.close()