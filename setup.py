from setuptools import setup

#py_modules is the module we want to use for this package.
#install_requires is the external depedency that our package depends on
#entry_points provide some additional metadata to our pacakage and also serves as
#an entry point to the package.
#A egg folder is created when we install this package locally.
#To install the local package, run "pip install --editable ."

setup(
    name="dice-CLI",
    version='1.0',
    packages=['cli', 'cli.commands'],
    # packages=['cli', 'cli.commands'],
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'dice = cli.cli:cli'
        ]
    }
)
