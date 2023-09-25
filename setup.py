from setuptools import setup, find_packages

setup(
    name='pyxel-typing',
    version='0.0.2',
    packages=find_packages(),
    package_data={'PyxelTyping': ['pkg/*', "pkg/data/*"]},
    install_requires=[
        'pyxel-app',
    ],
    entry_points={
        "console_scripts":[
            "pyxel-typing=PyxelTyping.entry:run",
        ],
    },    
    author="naoyashi",
    author_email="n.koba0427@gmail.com",
    description="simple typing app",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/n-koba0427/PyxelTyping",
    classifiers=[
        # "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Japanese",
    ],
)