from setuptools import setup, find_packages

setup(
    name="svp",
    version="0.1",
    packages=find_packages(),
    # Grupa za pothranjivanje fakulteta.
    # `ucitavanje_kod` je alias za klasu FakultetUcitavanjeKod
    entry_points={
        'svp_plugin':
            ['simple_visualize=svp.make_simple_view:SimpleVisualizator'],
    },
    zip_safe=True
)
