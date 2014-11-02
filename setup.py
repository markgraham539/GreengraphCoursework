from setuptools import setup, find_packages

setup(
    name = "Greengraph",
    version = "0.11",
    packages = find_packages(exclude=['*test']),
    scripts = ['Scripts/ggraph'],
    install_requires = ['argparse','matplotlib','numpy','pypng']
)