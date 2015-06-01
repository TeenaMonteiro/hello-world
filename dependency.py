from setuptools import setup

setup(
    name = "HelloWorld",
    version = "1.0",
    install_requires = ['MySQL-python==1.2.3','django==1.5'],
    
    # metadata for upload to PyPI
    author = "Teena Monteiro",
    author_email = "teena.mon11@gmail.com",
    description = "This is HelloWorld Package"
    
)
