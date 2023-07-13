import setuptools

with open("README.md","r") as file:
  description = file.read()

setuptools.setup(
     name="stud_crud",
    version="0.0.1",
    author="Jamie Omondi",
    author_email="cruiseomondi90@gmail.com",
    description="A python package for base classes",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamie-codez/stud_crud/",
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[]
)
