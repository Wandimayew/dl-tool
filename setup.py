from setuptools import setup

setup(
    name="dl-tool",
    version="1.0.0",
    packages=["dl"],
    entry_points={
        "console_scripts": [
            "dl=dl.cli:main"
        ]
    },
    install_requires=[
        "yt-dlp"
    ]
)