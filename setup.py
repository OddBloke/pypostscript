import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pypostscript',
    version='0.1.7',
    author='Mark Henwood',
    author_email='mark@mcbh.co.uk',
    description='Create PostScript page (including barcodes) using Python objects',
    license='MIT',
    keywords='postscript printing barcode',
    url='http://pypi.python.org/pypi/pypostscript',
    packages=['pypostscript'],
    package_data={'pypostscript': ['parts_dir/*']},
    provides=['pypostscript'],
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Topic :: Utilities'
    ]
)
