import os

from setuptools import setup


setup(
    name='swiss',
    version='0.0.1',
    author='Dylan Stephano-Shachter',
    author_email='dstephanoshachter@gmail.com',
    description=('Swiss tournament software'),
    license='GPLv3',
    url='https://github.com/dstathis/swiss',
    packages=['swiss'],
    long_description=open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
    ).read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 1 - Planning',
    ]
)
