from setuptools import find_packages,setup
from typing import List

hypenedot="-e ."
def get_requirements(filr_path:str)->List[str]:
    requirements=[]
    with open(filr_path) as file:
        requirements=file.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        if hypenedot in requirements:
            requirements.remove(hypenedot)
        return requirements

setup(
    name="DaimondPrice",
    version="0.0.1",
    author="Karthikeyan",
    author_email="2300030323cseh@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)