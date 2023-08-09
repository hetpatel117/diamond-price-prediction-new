from setuptools import  find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name='Diamond Price Prediction',
    author='Het Patel',
    version='0.0.1',
    author_email='hetn2002@gmail.com',
    install_package = get_requirements('requirements.txt'),
    packages=find_packages()
)