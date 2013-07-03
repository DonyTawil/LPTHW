try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':  'My Project',#ex46
    'author':  'My Name',#Dony
    'url':  'URL to get it at.',#N/A
    'download_url':  'Where to download it.',#N/A
    "author_email":  "My email.",#donytawil@gmail.com
    'versio':  '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts':  [],
    'name':  'projectname'
}

setup(**config)            
