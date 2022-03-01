from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="discordpy-antispam",
    version="1.0.2",
    description="An efficient and simple anti-spam system made for your discord bots.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['SpamFilter'],
    url="https://github.com/DorianAarno/SpamFilter",
    author="Aarno Dorian",
    author_email="aarnodorian56@gmail.com",
    download_url = "https://github.com/DorianAarno/SpamFilter/archive/refs/tags/v1.0.2.tar.gz",
    license = "MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
      install_requires=[
          'nltk'
      ]
)
