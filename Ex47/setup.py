try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':  'Ex47',#ex46
    'author':  'Dony',#Dony
    'url':  'URL to get it at.',#N/A
    'download_url':  'Where to download it.',#N/A
    "author_email":  "donytawil@gmail.com",
    'versio':  '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts':  [],
    'name':  'ex47'
}

setup(**config)            
