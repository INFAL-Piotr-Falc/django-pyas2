# -*- coding: utf-8 -*-
import os
from setuptools import find_packages, setup

root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root, 'README.rst')) as f:
    README = f.read()

install_requires = [
    'pyas2lib==1.4.4',
    'pyOpenSSL>=26.4.0,<27',
    'cryptography>=50.0.2,<51',
    'oscrypto @ git+https://github.com/wbond/oscrypto.git@d5f3437ed24257895ae1edd9e503cfb352e635a8',
    'django>=5.2.19,<5.3',
    'requests>=2.34.2,<3',
]

tests_require = [
    "pytest==9.0.2",
    "pytest-django==4.11.1",
    "pytest-mock==3.15.1",
    "django-environ==0.12.0",
]


setup(
    name='django-pyas2',
    version='1.2.3+infal.2',
    description='AS2 file transfer Server built on Python and Django.',
    license="GNU GPL v3.0",
    long_description=README,
    author='Abhishek Ram',
    author_email='abhishek8816@gmail.com',
    url='https://github.com/INFAL-Piotr-Falc/django-pyas2',
    packages=find_packages(exclude=['pyas2.tests', 'pyas2.tests.*']),
    python_requires='>=3.11,<3.12',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.11',
        "Topic :: Security :: Cryptography",
        "Topic :: Communications",
    ],
    install_requires=install_requires,
    extras_require={
        "tests": tests_require,
    },
)
