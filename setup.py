from __init__ import __version__
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup,find_packages

setup(
    name="dominiontabs",
    version=__version__,
    scripts=["dominion_tabs.py"],
    packages=find_packages(),
    install_requires=["reportlab>=2.5",
                      "PIL>=1.1.7"],
    package_data = {
        '' : ['*.txt','*.png']
        },
    author="Sumpfork",
    author_email="sumpfork@mailmight.net",
    description="Tab Divider Generation for the Dominion Card Game"
    )

