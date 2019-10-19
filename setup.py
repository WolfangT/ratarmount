#!/usr/bin/env python3

from setuptools import setup

setup(
    name="ratarmount",
    version="1.0",
    description="Random Access Read-Only Tar Mount (Ratarmount)",
    author="Maximilian K.",
    author_email="https://github.com/mxmlnkn",
    py_modules=['ratarmount'],
    install_requires=[
        "fusepy",
        "lz4",
        "msgpack",
        "simplejson",
        "pyyaml",
        "ujson",
        "cbor",
        "python-rapidjson",
    ],
    entry_points={"console_scripts": ["ratarmount=ratarmount:cli"]},
)
