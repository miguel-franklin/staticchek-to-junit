from setuptools import setup

setup(name='staticchek-to-junit',
      version='0.1',
      description='convert staticcheck files into junit xml. Read .check files from a specific folder and create juni-xml related files',
      url='',
      author='Miguel Franklin',
      author_email='miguel_mariano@atlantico.com.br',
      license='MIT',
      packages=['main'],
      install_requires=[
          'pathlib',
          'junit_xml_output',
          'pyinstaller'
      ],
      zip_safe=False)