import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clrppy",
    version="0.0.1",
    author="s0rmayz",
    author_email="2430545310@qq.com",
    description="More Simple Printing With Color",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/s0rmayz/clrppy",
    project_urls={
        "Github Page": "https://github.com/s0rmayz/clrppy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
