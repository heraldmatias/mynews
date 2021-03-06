import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "MyNews",
    version = "0.1.0",
    url = '',
    license = 'GPL V. 3',
    description = "MyNews",
    long_description = read('README.md'),

    author = 'Herald Olivares, Andres Herrada',
    author_email = 'heraldmatias.oz@gmail.com',

    packages = find_packages('src'),
    package_dir = {'': 'src'},

    install_requires = ['setuptools', 'coverage'],

    classifiers = [
        'Development Status :: 1 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Customers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Gallery Photography',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
