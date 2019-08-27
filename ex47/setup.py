try:
	from setuptools import setup
except ImportError
	from distutils.core import setup

config = [
	'description': 'Exercise 47'
	'author': 'Tuyen Dang',
	'url': 'URL to get it at.',
	'download_url': 'where to download it.',
	'author_email': 'your email',
	'version': '0.1',
	'install_requires': ['nose'],
	'package': ['ex47'],
	'scripts': [],
	'name': 'projectname'
]

setup(**config)
