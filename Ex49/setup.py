try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':  'ex49',#ex46
    'author':  'My Name',#Dony
    'url':  '',#N/A
    'download_url':  '',#N/A
    "author_email":  "My email.",#donytawil@gmail.com
    'versio':  '3.1',
    'install_requires': ['nose'],
    'packages': ['ex49'],
    'scripts':  [],
    'name':  'ex49'
}

setup(**config)            
