from distutils.core import setup
from factory_manager.__init__ import __version__ as version

setup(
    name='factory_manager',
    version=version,
    packages=['factory_manager'],
    url='',
    license='',
    author='Ryan',
    author_email='',
    description='Factory - Manager abstract class', requires=['pandas', 'matplotlib']
)
