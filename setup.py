from setuptools import setup, find_packages

setup(
    name='leetcode-py',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest==7.4.3',
    ],
    entry_points={
    },
    author='İsmail Özsaygı',
    author_email='devozsaygi@gmail.com',
    description='Python solutions for some of the LeetCode problems.',
    license='MIT',
)