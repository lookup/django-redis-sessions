import os
from setuptools import setup

from redis_sessions import __version__


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


packages = ['redis_sessions']

setup(
    name='django-redis-sessions',
    version=__version__,
    description="Redis Session Backend For Django",
    long_description=read("README.rst"),
    keywords='django, sessions, redis',
    author='Martin Rusev',
    author_email='martinrusev@live.com',
    url='http://github.com/martinrusev/django-redis-sessions',
    license='BSD',
    packages=packages,
    zip_safe=False,
    install_requires=['redis>=2.4.10'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
