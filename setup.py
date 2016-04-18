from setuptools import setup

setup(name='alglbraic',
      version='0.1.1',
      description='Tools for doing algebra in GLSL',
      url='http://wondering.xyz/alglbraic',
      author='micahscopes',
      author_email='fitchmicah@gmail.com',
      license='MIT',
      packages=['alglbraic','alglbraic.fragments'],
      package_data={'alglbraic': ['fragments/*.frag']},
      install_requires=['sympy','galgebra'],
      dependency_links=['http://github.com/brombo/galgebra/tarball/master#egg=galgebra'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
