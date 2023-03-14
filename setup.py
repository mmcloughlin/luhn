from setuptools import setup
import re

module_file = open("luhn.py").read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", module_file))


def readme():
    return open("./README.rst").read()


setup(
    name="luhn",
    version=metadata["version"],
    description="Generate and verify Luhn check digits",
    long_description=readme(),
    url="https://github.com/mmcloughlin/luhn",
    author="Michael McLoughlin",
    author_email="mmcloughlin@gmail.com",
    license="MIT",
    py_modules=["luhn"],
    test_suite="nose.collector",
    tests_require=["nose"],
)
