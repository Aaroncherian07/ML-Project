from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function opens the requirements and returns as a list
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #Whenever we do readlines and read the requirement file whenever we read the file the lines via the readlines command it will add the /n as well so we need to replace that with blank 
        requirements=[req.replace('\n','') for req in requirements]
        
        if HYPHEN_E_DOT in requirements: #-e . is used to trigger the 
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements
               
    
setup(
name='ML-Project',
version='0.0.1',
author='Aaron Cherian',
author_email='aaroncherian99@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') 
)