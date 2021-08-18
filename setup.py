from setuptools import setup

with open("README.md", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="pastecord",
    version="1.0.0",
    description="Api wrapper for pastecord.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thesadru/pastecord",
    author="thesadru",
    author_email="thesadru@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    keywords="api, wrapper, pastecord",
    py_modules=["pastecord"],
    python_requires=">=3.6",
    install_requires=["requests"],
    project_urls={
        "Bug Reports": "https://github.com/thesadru/pastecord/issues",
        "Source": "https://github.com/thesadru/pastecord/",
    },
)
