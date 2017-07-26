from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='diffslcpy',
    version='0.1',
    description='DiffSLc implementation in Python.',
    long_description=readme(),
    url='https://github.com/divyamistry/diffslc-py',
    author='Divya Mistry',
    author_email='divyam@iastate.edu',
    license='MIT',
    packages=['diffslcpy'],
    install_requires=['networkx', 'numpy', 'scipy'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['diffslcpy-cl=diffslcpy.command_line:main']
    },
    zip_safe=False
)
