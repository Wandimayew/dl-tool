from setuptools import setup, find_packages

setup(
    name="dl-tool",
    version="1.0.0",
    author="Wandi",
    description="Fast terminal video downloader with IDM-style UI",
    packages=find_packages(),
    install_requires=[
        "yt-dlp"
    ],
    entry_points={
        "console_scripts": [
            "dl=dl.cli:main"
        ]
    },
    python_requires=">=3.8",
)