''' Start a data analytics project'''

import pathlib


def create_project_directory(directory_name): # add type hints to parms
    """
    Create a project sub directory.
    :param directory_name: Name of the directory to be created, e.g. "test" 
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def create_annual_data_directories(directory_name: str, start_year: int, end_year: int):
    """ 
    Create a project sub-directory.
    :parm directory_name: Name to be created, e.g. "data"
    :param start: First year to be created, e.g. 2000
    :param end: Last year to be created, e.g. 2024
    """
    create_project_directory(directory_name)

    for year in range(start_year, end_year +1):
        print(year)
        year_directory = pathlib.Path(directory_name).joinpath(str(year))
        print(year_directory)
        print(f"Created{year_directory}")

def main():
    ''' Scaffold a project.'''
    create_project_directory('test') #name the parameter
    create_project_directory('docs') #name the parameter
    


if __name__ == '__main__':
    main ()
