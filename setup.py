import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Minecraft World Info",
    version="0.0.1",
    author="Skyr",
    author_email="skirlaxxx@gmail.com",
    description="Get player and world data in Minecraft single-player",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Skirlax/Minecraft-World-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 license",
        "Operating System :: OS Independent",
    ],
)