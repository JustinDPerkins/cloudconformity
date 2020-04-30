import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloudconformity", 
    version= "0.1.9",
    author="Justin Perkins",
    author_email="justin_perkins@trendmicro.com",
    description="Cloud Conformity template scanner tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JustinDPerkins/cloudconformity",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    packages=["TemplateScanner"],
    include_package_data=True,
    install_requires=['requests'],
    entry_points={
        "console_scripts": [
            "cloudconformity=TemplateScanner.scanner:main",
        ]
    }
)