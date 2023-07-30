from setuptools import find_packages,setup
import os


e_dot='-e .'
def get_requirements(file_path: str):
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if '-e .' in requirements:
            requirements.remove(e_dot)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='sasendra',
    author_email='sasendrav9@gmail.com',
    packages=find_packages()
    
)
