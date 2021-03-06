from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "matplotlib",
    "numpy",
    "pandas",
    "tensorflow==2.3.0",
    "tensorflow-probability==0.11.0",
    "scikit-image",
    "sep",
]

setup(
    name="debvader",
    version="0.0.81191",
    author="Bastien Arcelin",
    author_email="arcelin@apc.in2p3.fr",
    maintainer="Biswajit Biswas",
    maintainer_email="biswajit.biswas@apc.in2p3.fr",
    description="Galaxy deblender from variational autoencoders",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/BastienArcelin/debvader",
    include_package_data=True,
    packages=["debvader"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_data={"debvader": ["data/*"]},
)
