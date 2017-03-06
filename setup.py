from setuptools import setup

setup(
    name='abcalc',
    packages=['abcalc'],
    version='1.0.1',
    description='AB split test calculator',
    author='Ivan Miniailenko',
    author_email='discrete.west@gmail.com',
    url='https://github.com/diswest/abcalc',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',

    ],
    keywords=['statistics', 'ab', 'split', 'test', 'calculator'],
)
