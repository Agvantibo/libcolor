import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libcolor-agvantibo", # Replace with your own username
    version="0.0.1",
    author="Savchenko Dmitriy",
    author_email="d.savchenko@sch-int.ru",
    description="A light toolkit to manage Tk colors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Agvantibo//libcolor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL V3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
