from setuptools import setup, find_packages

setup(
    name = "Greengraph",
    version = "0.11",
    packages = find_packages(exclude=['*Test']),
    scripts = ['Scripts/ggraph'],
    install_requires = ['argparse','matplotlib','numpy','pypng']
)