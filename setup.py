from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="ui_theme",
    version="0.0.1",
    description="Custom UI theme and interface enhancements.",
    author="Darshana Patil",
    author_email="darshanap01@brainmine.ai",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
