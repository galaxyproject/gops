try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup( name="galaxy_ops",
       version="1.0.0",
       packages=find_packages( 'lib' ),
       package_dir={ '': 'lib' },
       setup_requires=[],
       author="Dan Blankenberg, Galaxy Team",
       author_email="galaxy-dev@lists.galaxyproject.org",
       description="Galaxy operations.",
       url="http://galaxyproject.org",
       zip_safe=False,
       dependency_links=[] )
