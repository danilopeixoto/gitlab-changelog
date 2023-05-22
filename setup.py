'''
Python setup script.
'''

import os
from distutils.util import convert_path
from typing import Dict

from setuptools import find_packages, setup  # type: ignore


def get_package_info(name: str) -> Dict[str, str]:
    '''
    Get package description information.

    Parameters:
        name (str): Main package name.
    Returns:
        Dict[str, str]: A dictionary containing package information.
    '''

    with open(
        convert_path(os.path.join(name, 'package.py')),
        encoding='utf-8'
    ) as file:
        package_dict: Dict[str, str] = {}
        exec(file.read(), package_dict)  # pylint: disable=W0122

        return package_dict


def parse_long_description() -> str:
    '''
    Get package long description.

    Returns:
        str: A string representing package long description.
    '''

    with open(convert_path('README.md'), encoding='utf-8') as file:
        return file.read()


PACKAGE_NAME = 'gitlab-changelog-tool'
PACKAGE_PATH = PACKAGE_NAME.replace('-', '_')

package_info = get_package_info(PACKAGE_PATH)

setup(
    name=PACKAGE_NAME,
    version=package_info['__version__'],
    description=package_info['__description__'],
    long_description=parse_long_description(),
    long_description_content_type='text/markdown',
    author=package_info['__author__'],
    license=package_info['__license__'],
    url='https://github.com/danilopeixoto/gitlab-changelog-tool',
    download_url='https://pypi.org/project/gitlab-changelog-tool',
    project_urls={
        'Code': 'https://github.com/danilopeixoto/gitlab-changelog-tool',
        'Issue tracker': 'https://github.com/danilopeixoto/gitlab-changelog-tool/issues'
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: BSD License'
    ],
    python_requires='>=3.8.0',
    install_requires=[
        'click>=8.1.0',
        'jinja2>=3.1.0',
        'semver>=3.0.0',
        'python-dateutil>=2.8.0',
        'python-gitlab>=3.14.0'
    ],
    extras_require={
        'development': [
            'setuptools>=58.2.0',
            'wheel>=0.37.0',
            'autopep8>=1.6.0',
            'isort>=5.10.0',
            'mypy>=0.9.0',
            'pylint>=2.12.0',
            'pytest>=6.2.0',
            'pytest-cov>=3.0.0',
            'twine>=3.7.0',
            'bump2version>=1.0.0'
        ]
    },
    entry_points={
        'console_scripts': [
            f'{PACKAGE_NAME} = {PACKAGE_PATH}.__main__:cli'
        ]
    },
    packages=find_packages(),
    zip_safe=False
)
