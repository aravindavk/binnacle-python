from setuptools import setup

from binnacle.version import VERSION

setup(
    name="binnacle",
    version=VERSION,
    packages=["binnacle"],
    install_requires=['requests', 'termcolor'],
    author="Aravinda VK",
    author_email="vkaravinda7@gmail.com",
    description="Imperative tests/infra automation tool",
    license="MIT",
    keywords="infra,tests,automation",
    url="https://github.com/aravindavk/binnacle-python",
    long_description="""
    Imperative tests and infra automation tool.
    """,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only"
    ],
)
