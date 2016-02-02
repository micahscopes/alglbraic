from setuptools import setup

setup(name='alglbraic',
      version='0.1',
      description='Tools for doing algebra in GLSL',
      url='http://wondering.xyz/alglbraic',
      author='micahscopes',
      author_email='fitchmicah@gmail.com',
      license='MIT',
      packages=['alglbraic'],
      package_data={'alglbraic': ['fragments/*.frag']},
      install_requires=['sympy']
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
