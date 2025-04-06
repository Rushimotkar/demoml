from setuptools import find_packages,setup
from typing import List




def get_requirement(file_path:str)-> list[str]:
    '''this function will return the list of requirements'''
    requirements = []
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
   
        if "-e ." in requirements:
            requirements.remove("-e .")

setup(
    
    name="mlproject",
    version="0.0.1",
    author="rushikesh",
    author_email="rushikeshmotkar14@gmail.com",
    packages=find_packages(),
    install_requires=["pandas","numpy","seaborn","matplotlib","scikit-learn","flask","flask-restful","flask-cors","joblib","tensorflow"],
    install_requires=get_requirement('requirement.txt'), 
    
)