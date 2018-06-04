from setuptools import setup

setup(
    name="marcFieldsLookup",
    author="Tyler Danstrom",
    author_email="tdanstrom@uchicago.edu",
    version="1.0.0",
    license="LGPL3.0",
    description="A pythonic library to allow exploring and browsing MARC21 schema",
    keywords="python3.6 iiif-presentation manifests marc",
    #include_page_data=True,
    package_data = {
        'marclookup': ['marc-schema.json']
    },
    packages=['marclookup'],
    classifiers=[
        "License :: OSI Approved :: GNU Library or Lesser " +
        "General Public License (LGPL)",
        "Development Status :: 5 - Alpha/Prototype",
        "Intended Audience :: Education",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires = [
        'configobj',
        'appdirs',
    ]
)