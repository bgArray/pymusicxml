# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymusicxml",
    version="0.0.1",
    author="bgArray",
    author_email="TriM-Organization@hotmail.com \n"
                 "474037765@qq.com",
    description="给Python的musicxml的解析库。\n"
    "A musicxml parser for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZhugeLiangandBaguaArray/pymusicxml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: Chinese (Simplified)",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
