try:
    from setuptools import setup
    setup  # quiet "redefinition of unused ..." warning from pyflakes
    # arguments that distutils doesn't understand
    setuptools_kwargs = {
        'install_requires': [
            "github3.py >= 0.7.0",
        ],
        'zip_safe': False,
    }
except ImportError:
    from distutils.core import setup
    setuptools_kwargs = {}

setup(
    name='GfmPreview',
    version='0.1.0',
    author='Leo Ju',
    author_email='mr.simple@gmail.com',
    packages=['gfm_preview'],
    scripts=['bin/gfm-preview'],
    url='http://pypi.python.org/pypi/GfmPreview/',
    license='LICENSE.txt',
    description='GitHub flavored markdown preview',
    long_description=open('README.md').read(),
    **setuptools_kwargs
)
