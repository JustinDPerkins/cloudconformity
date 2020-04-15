import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="conformity", # Replace with your own username
    version="0.0.1",
    author="Justin Perkins",
    author_email="justin_perkins@trendmicro.com",
    description="Cloud Conformity template scanner tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    packages=["TemplateScanner"],
    include_package_data=True,
    install_requires=["os","sys","argparse","requests","json"],
    entry_point={
        "console_scripts": [
            "conformity=TemplateScanner.scanner.py",
        ]
    }
)