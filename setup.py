from setuptools import setup, find_packages
import os

try:
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "High-performance log analysis and visualization toolkit"

setup(
    name="snap-analog",
    version="2.1.0",
    author="Batuhan Erkoc",
    author_email="batuhan.erkoc@example.com",
    description="High-performance log analysis and visualization toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/batuhannerkoc/snap-analog",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snap-analog=src.cli:main",
        ],
    },
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "matplotlib>=3.6.0",
        "seaborn>=0.12.0",
        "psutil>=5.9.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Logging",
        "Topic :: Utilities",
    ],
)
