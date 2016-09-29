#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015-2016 Kevin Deldycke <kevin@deldycke.com>
#                         and contributors.
# All Rights Reserved.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

import io
import re
from os import path

from setuptools import find_packages, setup

MODULE_NAME = 'chessboard'

DEPENDENCIES = [
    'click >= 5.0',
    'click_log',
    'bprofile',
    'numpy',
    'pandas',
    'seaborn',
    'py-cpuinfo',
]

EXTRA_DEPENDENCIES = {
    # Extra dependencies are made available through the
    # `$ pip install .[keyword]` command.
    'docs': [
        'sphinx >= 1.4',
        'sphinx_rtd_theme'],
    'tests': [
        'nose',
        'coverage',
        'pycodestyle >= 2.1.0.dev0',
        'pylint'],
    'develop': [
        'isort',
        'wheel',
        'setuptools >= 24.2.1',
        'bumpversion'],
}


def read_file(*relative_path_elements):
    """ Return content of a file relative to this ``setup.py``. """
    file_path = path.join(path.dirname(__file__), *relative_path_elements)
    return io.open(file_path, encoding='utf8').read().strip()


# Cache fetched version.
_version = None  # noqa
def version():
    """ Extracts version from the ``__init__.py`` file at the module's root.
    """
    global _version
    if _version:
        return _version
    init_file = read_file(MODULE_NAME, '__init__.py')
    matches = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', init_file, re.M)
    if not matches:
        raise RuntimeError("Unable to find version string in __init__.py .")
    _version = matches.group(1)  # noqa
    return _version


def latest_changes():
    """ Extract part of changelog pertaining to version. """
    lines = []
    for line in read_file('CHANGES.rst').splitlines():
        if line.startswith('-------'):
            if len(lines) > 1:
                lines = lines[:-1]
                break
        if lines:
            lines.append(line)
        elif line.startswith("`{} (".format(version())):
            lines.append(line)
    if not lines:
        raise RuntimeError(
            "Unable to find changelog for the {} release.".format(version()))
    return "\n".join(lines).strip()


def long_description():
    """ Collates project README and latest changes. """
    return "{}\n\n\nChanges for v{}".format(
        read_file('README.rst'), latest_changes())


setup(
    name=MODULE_NAME,
    version=version(),
    description="CLI to solve combinatoric chess puzzles.",
    long_description=long_description(),
    keywords=['chess', 'puzzle', 'CLI', 'solver'],

    author='Kevin Deldycke',
    author_email='kevin@deldycke.com',
    url='https://github.com/kdeldycke/chessboard',
    license='GPLv2+',

    packages=find_packages(),
    # https://www.python.org/dev/peps/pep-0345/#version-specifiers
    python_requires='>= 2.7, != 3.0, != 3.1, != 3.2',
    install_requires=DEPENDENCIES,
    tests_require=DEPENDENCIES + EXTRA_DEPENDENCIES['tests'],
    extras_require=EXTRA_DEPENDENCIES,
    dependency_links=[
        # XXX Waiting for pycodestyle 2.1.0 release.
        'git+https://github.com/PyCQA/pycodestyle.git'
        '@dc08dadd84369185f3c19782fd727dbf5029a056'
        '#egg=pycodestyle-2.1.0.dev0',
    ],
    test_suite='{}.tests'.format(MODULE_NAME),

    classifiers=[
        # See: https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: '
        'GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        # List of python versions and their support status:
        # https://en.wikipedia.org/wiki/CPython#Version_history
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Education',
        'Topic :: Games/Entertainment :: Board Games',
    ],

    entry_points={
        'console_scripts': [
            'chessboard={}.cli:cli'.format(MODULE_NAME),
        ],
    }
)
