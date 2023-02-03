from setuptools import setup, find_packages

setup(
    name="twp",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'twp_plugin':
            ['load_ta=twitter_api.twitter_api_parser:TwitterApiParser'],
    },
    zip_safe=True
)
