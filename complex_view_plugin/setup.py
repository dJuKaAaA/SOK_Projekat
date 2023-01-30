from setuptools import setup, find_packages

setup(
    name="cvp",
    version="0.1",
    packages=find_packages(),
    # Grupa za pothranjivanje fakulteta.
    # `ucitavanje_kod` je alias za klasu FakultetUcitavanjeKod
    entry_points={
        'cvp_plugin':
            ['complex_visualize=cvp.make_complex_view:ComplexVisualizator'],
    },
    zip_safe=True
)
