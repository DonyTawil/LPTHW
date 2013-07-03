try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':  'ex48',
    'author':  'dony',#Dony
    'url':  '',#N/A
    'download_url':  '',#N/A
    "author_email":  "donytawil@gmail.com",#donytawil@gmail.com
    'versio':  '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts':  [],
    'name':  'ex48'
}

setup(**config)            
