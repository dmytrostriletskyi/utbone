"""
Setup.
"""
from setuptools import find_packages, setup


setup(
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Bones for faster testing.",
    entry_points={
        "console_scripts": [
            "utbone = utbone.utbone:utbone",
        ]
    },
    install_requires=[
        "flake8>=3.4.1",
        "pep8>=1.7.0",
        "pyCLI>=2.0.3",
        "pylint>=1.7.2",
    ],
    license="MIT",
    name="utbone",
    packages=find_packages(),
    version="0.1.0",
)
