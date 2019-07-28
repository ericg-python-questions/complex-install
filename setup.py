from setuptools import setup, find_packages

requirements = [
    'cffi'
]

setup_requirements = [
    'cffi'
]

setup(
    name = 'complex_install',
    packages = find_packages( include = [ 'complex_install' ] ),
    install_requires = requirements,
    setup_requires = setup_requirements,
    cffi_modules = [ "hello_world/build_hello_world.py:ffibuilder" ]
)