try:
	from setuptools import setup
except ImportError
	from distutils.core import setup

config = [
	'description': 'My Project',
	'author': 'Tuyen Dang',
	'url': 'URL to get it at.',
	'download_url': 'where to download it.',
	'author_email': 'your email',
	'version': '0.1',
	'install_requires': ['nose'],
	'package': ['NAME'],
	'scripts': [],
	'name': 'projectname'
]

setup(**config)
