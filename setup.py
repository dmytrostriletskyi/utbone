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
    description="Bones for faster unit testing.",
    entry_points={
        "console_scripts": [
            "utbone = utbone.utbone:utbone",
        ]
    },
    install_requires=[
        "pyCLI>=2.0.3",
    ],
    license="MIT",
    name="utbone",
    packages=find_packages(),
    version="0.1.0",
)
