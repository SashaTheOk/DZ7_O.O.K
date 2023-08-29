from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1.00',
      description='Clean Folder',
      author='Kovalenko O.O.',
      author_email='nomail@nomail.com',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.main:start']}
      )