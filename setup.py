from setuptools import setup

setup(
    name='mistplotter',
    version='0.1.0',    
    description='plotting for mistery',
    url='https://github.com/kjmcc01/mistplotting',
    author='KJ McConnell',
    author_email='kj.mcconnell@yale.edu',
    packages=['mistplotting'],
    install_requires=['matplotlib',
                      'numpy',
                      'streamlit',
                      'mistery'                     
                      ],
)