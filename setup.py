from setuptools import setup, find_packages

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),    
    # https://stackoverflow.com/a/53069528
    # https://stackoverflow.com/a/3277511
    install_requires=tuple(open('requirements.txt', 'r')),
)
