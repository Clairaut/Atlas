from setuptools import setup, find_packages
import glob

setup(
    name='atlas',
    version='0.1.0',
    description='An interface for Swiss Ephemeris',
    packages=find_packages(include=['atlas*']),
    package_data={'atlas': ['eph/*', 'static/*/*']},
    include_package_data=True,
    py_modules=['atlas', 'chart', 'cli', 'topo', 'eph', 'cyclical', 'console', 'aspects'],
    entry_points={
        'console_scripts': [
            'atlas = atlas.cli:main'
        ],
    },
    install_requires=[
        
    ],
)