from setuptools import setup

def readme():
    f = open('README.md','r')
    text = f.read()
    f.close()
    return text

setup(name='dhm',
      version='1.0',
      description='Tool for creating heatmaps, where rows and columns are organized by hierarchical clusters'
                  ' as seen in https://github.com/themantalope/pydendroheatmap, which is based on'
                  'http://code.activestate.com/recipes/578175-hierarchical-clustering-heatmap-python/',
      url='https://github.com/kaniblu/dhm/',
      author='Kang Min Yoo',
      author_email='kaniblurous@gmail.com',
      license='MIT',
      packages=['ydendroheatmap'],
      setup_requires=['numpy',
                      'scipy',
                      'colour',
            'matplotlib',],
      install_requires = [],
      long_description=readme(),
      classifiers=['Topic :: Scientific/Engineering :: Visualization'],
      include_package_data=True)