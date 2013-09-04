try:
    from setuptools import setup
    setup  # quiet "redefinition of unused ..." warning from pyflakes
    # arguments that distutils doesn't understand
    setuptools_kwargs = {
        'install_requires': [
            "Markdown",
        ],
        'zip_safe': False,
    }
except ImportError:
    from distutils.core import setup
    setuptools_kwargs = {}

setup(
    name='GfmPreview',
    version='0.2.0',
    author='Leo Ju',
    author_email='mr.simple@gmail.com',
    packages=['md_preview'],
    scripts=['bin/md-preview'],
    package_data={'md_preview': ['templates/*']},
    url='https://github.com/simple/md-preview',
    license='LICENSE.txt',
    description='Simple markdown preview from command line',
    long_description=open('README.md').read(),
    **setuptools_kwargs
)
