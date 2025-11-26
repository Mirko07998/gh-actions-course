from setuptools import setup, find_packages

setup(
    name='HelloWorld',
    version='0.1',
    packages=find_packages(),
    description='A simple HelloWorld module',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/helloworld',
    install_requires=[
        # Add any package dependencies here if needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)