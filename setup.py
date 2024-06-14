from setuptools import setup, find_packages

setup(
    name='atlas',
    version='0.1',
    description='An interface for Swiss Ephemeris',
    packages=find_packages(include=['atlas*']),
    package_data={'atlas': ['eph/*', 'static/*/*', 'config/*']},
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