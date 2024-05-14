#Project Start 
#Week 2 Project
'''This module provides functions for creating a series of project folders.'''

#Import dependencies
import math
import statistics
import pathlib
import time
import os
import mindycruzutils


#Define functions for folder creation

    #Item Range
def create_folders_for_range(start_year, end_year):
    for year in range(start_year, end_year + 1):
        folder_name = str (year)
        pathlib.Path(folder_name).mkdir(exist_ok=True)

    #Item List
def create_folders_from_list(folder_list):
    for folder_name in folder_list:
        pathlib.Path(folder_name).mkdir(exist_ok=True)

    #Comprehension
def create_prefixed_folders(folder_list, prefix):
    for folder_name in folder_list:
        if prefix:
            folder_path = f"{prefix}-{folder_name}"
        else:
            folder_path = folder_name
        pathlib.Path(folder_path).mkdir(exist_ok=True)

    #While Loop
def create_folders_periodically(duration):
    start_time = time.time()
    counter= 0
    while time.time() - start_time <= duration:
        counter += 1
        folder_name=  f"folder_{counter}"
        pathlib.Path(folder_name).mkdir(exist_ok=True)
        time.sleep(duration)

#Define Main Function

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {mindycruzutils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2003, end_year=2019)

    # Call function 2 to create folders given a list
    folder_names = ['Postive-data', 'Negative-data', 'Neutral']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['Postive', 'Negative', 'Neutral']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    demographic = [
      "Age", 
      "Sex", 
      "income Level", 
      "Location", 
      "Education Level", 
      "Homeownership", 
      "Race"
    ]
    create_folders_from_list(demographic, to_lowercase=True, remove_spaces=True)

#Execution
if __name__ == '__main__':
    main()
