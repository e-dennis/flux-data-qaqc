import io, re
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("fluxdataqaqc/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \'(.*?)\'", f.read()).group(1)

requires = [
    'bokeh',
    'numpy>=1.15',
    'pandas',
    'refet',
    'xlrd>=1.2.0'
]

tests_require = ['pytest']

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3.7',
    'Environment :: Console',
    'Development Status :: 4 - Beta',
    'Topic :: Scientific/Engineering',
    'Intended Audience :: Science/Research'
]

setup(
    name='fluxdataqaqc',
    description='Tools for QA/QC of eddy covariance station data',
    long_description=readme,
    author='John Volk and Christian Dunkerly',
    author_email='jmvolk@unr.edu',
    license='Apache',
    version=version,
    url='https://github.com/Open-ET/flux-data-qaqc',
    platforms=['Windows','Linux','Mac OS X'],
    classifiers=classifiers,
    packages=['fluxdataqaqc'],
    install_requires=requires,
    tests_require=tests_require,
    package_data={'fluxdataqaqc': ['examples/*'],
        '': ['environment.yml'],
        'fluxdataqaqc': ['FLUXNET_metadata.xlsx']},
    include_package_data=True,
)
