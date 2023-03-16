from setuptools import setup,find_packages
from typing import List


HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this func will reuturn the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.read().split("\n")

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="suriya",
    author_email="suriya.gsp1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)