from setuptools import setup
import io, re, os

def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

version = find_version('m2m', '__init__.py')

setup(name='m2m',
      version=version,
      description='Module for simple interaction with the OOI M2M system',
      long_description='README.md',
      url='https://github.com/tjcrone/m2m',
      author='Tim Crone',
      author_email='tjcrone@gmail.com',
      license='MIT',
      packages=['m2m'])
