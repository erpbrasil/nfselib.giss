#!/usr/bin/env python
import io
from os.path import dirname, join

from setuptools import find_namespace_packages, setup


def read(*names):
    with io.open(join(dirname(__file__), *names), encoding="utf8") as fh:
        return fh.read()


setup(
    name="nfselib.giss",
    version="0.1.0",
    license="MIT",
    description="Bindings xsdata do webservice de NFS-e do GissOnline (versao 2, ABRASF 2.04 com IBS/CBS)",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    author="KMEE",
    author_email="mileo@kmee.com.br",
    url="https://github.com/erpbrasil/nfselib.giss",
    packages=find_namespace_packages(include=["nfselib.*"]),
    namespace_packages=["nfselib"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial :: Accounting",
    ],
    keywords=["NFS-e", "GissOnline", "ABRASF", "xsdata"],
    python_requires=">=3.10",
    install_requires=["xsdata>=24.1"],
)
