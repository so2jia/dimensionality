"""Copyright 2018.

Authors: Christiane Ahlheim, Sebastian Bobadilla-Suarez, Kurt Braunlich,
Giles Greenway, & Olivia Guest.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup

setup(
    name='FuncionalDimensionality',
    version='1.0.0',
    description='Estimate functional dimensionality for FMRI data',
    license='GPLv3',
    author='Christiane Ahlheim, Sebastian Bobadilla-Suarez, Kurt Braunlich,'
    'Giles Greenway, & Olivia Guest',
    author_email='b.love@ucl.ac.uk',
    packages=['funcdim'],
    install_requires=['nibabel', 'numpy', 'scipy', 'hdf5storage', 'six']
)
