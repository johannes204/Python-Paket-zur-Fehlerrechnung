from setuptools import setup, find_packages

setup(
    name="fehlerrechnung",
    version="0.4",
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    description="Vereinfachung Fehlerrechnung mit Latex",
    author="Johannes Simonetto",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)