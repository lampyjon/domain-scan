"""
setup module for domain-scan
Based on:
- https://packaging.python.org/distributing/
- https://github.com/pypa/sampleproject/blob/master/setup.py
"""

from setuptools import setup

setup(
    name='domain-scan',

    # Versions should comply with PEP440
    version="0.0.1",
    description='Scan websites for HTTPS deployment best practices',

    # NCATS "homepage"
    url='https://18f.gsa.gov',
    # The project's main homepage
    download_url='https://github.com/18F/domain-scan',

    # Author details
    author='18f@gsa.gov',
    author_email='ncats@hq.dhs.gov',

    license='License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='https best practices',

    packages=['domain-scan'],

    install_requires=[
	'ipython',
	'requests',

	# Used by all local and Lambda-based code.
	'strict-rfc3339',

	# To support a11y scanner:
	'pyyaml'

	# Ubuntu 14.04 has an old version of six
	'six>=1.6',

	# To support pshtt scanner (and to stay fresh):
        'pshtt==0.4.0-dev',
	
	# To support sslyze scanner:
	'sslyze',
	'cryptography',

	# To support censys gatherer:
	'censys'

	# For Lambda support (only used locally):
	'boto3'
      ],

    dependency_links=[
      'git+ssh://git@github.com/dhs-ncats/pshtt/tarball/master#egg=pshtt-0.4.0-dev',
    ]

    extras_require={
        # 'dev': ['check-manifest'],
     #   'test': [
      #      'tox',
       #     'pytest'
       # ],
    },

    # Conveniently allows one to run the CLI tool as `domain-scan`
    entry_points={
        'console_scripts': [
            'domain_scan = scan:main',
        ]
    }
)
