"""Setup for the lazyimport package."""

import setuptools
import versioneer


TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov',
    # non-testing packagesrequired by tests, not by the package
    'strct',
    # to be able to run `python setup.py checkdocs`
    'collective.checkdocs', 'pygments',
]


with open('README.rst') as f:
    README = f.read()

setuptools.setup(
    author="Shay Palachy",
    author_email="shaypal5@gmail.com",
    license='GNU3',
    name='lazyimport',
    description="lazyimport lets you import python modules lazily.",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    long_description=README,
    url='https://github.com/shaypal5/lazyimport',
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require={
        'test': TEST_REQUIRES
    },
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
