from setuptools import setup, find_packages

setup(
    name="core",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=2.1'],
    package_data={'d3_primeri': ['static/*.css', 'static/*.js', 'templates/*.html']},
    zip_safe=False
)
