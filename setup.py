from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="office-powerpoint-mcp-server-fixed",
    version="2.0.4",
    author="GongRzhe",
    author_email="gongrzhe@gmail.com",
    description="Fixed MCP Server for PowerPoint manipulation using python-pptx - Consolidated Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GongRzhe/Office-PowerPoint-MCP-Server.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ppt_mcp_server=ppt_mcp_server:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json"],
    },
)
