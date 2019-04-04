from setuptools import setup
setup(
    name='ask_meagain',
    packages=['ask_meagain'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_bootstrap',
        'flask-wtf',
    ],
)

