from setuptools import setup, find_packages

setup(
    name="fsp",
    version="0.1",
    packages=find_packages(),
    # Grupa za pothranjivanje fakulteta.
    # `ucitavanje_kod` je alias za klasu FakultetUcitavanjeKod
    entry_points={
        'fsp_plugin':
            ['load_fs=file_system.file_system_parser:FileSystemParser'],
    },
    zip_safe=True
)
