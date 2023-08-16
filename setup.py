import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ ="0.0.0"

REPO_NAME = 'cnnClassifier'
AUTHOR_USER_NAME = "sunil giri"
SRC_REPO = 'Chicken-disease-classifier--Using-MLOPS-DVC-Pipeline'
AUTHOR_EMAIL = "seungiri841@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Chicken Disease Classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"))