try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Michal Sienkiewicz',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'mich.sienkiewicz@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex49'],
	'scripts': [],
	'name': 'ex49'
}

setup(**config)