from setuptools import setup

setup(name='glbraic',
      version='0.1',
      description='python tools for doing algebra in GLSL',
      url='http://wondering.xyz/aglebraic',
      author='micahscopes',
      author_email='fitchmicah@gmail.com',
      license='MIT',
      packages=['glbraic'],
      package_data={'glbraic': ['fragments/*.frag']}
      zip_safe=False)
