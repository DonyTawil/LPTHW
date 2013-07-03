try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



config = {
    'description':  'First project',#ex46
    'author':  'Dony',#Dony
    'url':  '',#N/A
    'download_url':  '',#N/A
    "author_email":  "donytawil@gmail.com",#donytawil@gmail.com
    'versio':  '3.1',
    'install_requires': ['nose'],
    'packages': ['skeleton\quiz46','skeleton\\tests'],
    'scripts':  ['skeleton\\bin\hey\hey.py'],    
    'name':  'quiz46'
}
#entry_points={'console_scripts':['hey = hey:main']}
setup(**config)
setup(entry_points={'console_scripts':['dudeco = hey:say_hi']})        
