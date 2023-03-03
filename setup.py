from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
]

setup(
    name='Newspaperify',
    version='1.0',
    description='An application that gets your top spotify tracks and turns them into a newspaper based off Receiptify',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)