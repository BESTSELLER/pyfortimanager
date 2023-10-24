from setuptools import setup, find_packages


setup(
    name="pyfortimanager",
    version="1.0.0",
    description="Python API client library for Fortinet's FortiManager.",
    license="Apache2",
    author="Rasmus Thing",
    author_email="rasmus.thing@bestseller.com",
    url="https://github.com/BESTSELLER/pyfortimanager",
    python_requires=">=3.8, <4",
    install_requires=[
        "requests>=2.20.0,<3.0"
    ],
    zip_safe=False,
    keywords=[
        "fortinet",
        "fortimanager"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ]
)