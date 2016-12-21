from setuptools import setup, find_packages


setup(
    name='crawler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4'
    ],
    entry_points='''
        [console_scripts]
        crawler=crawler.main:run
    ''',
)
