from setuptools import setup, find_packages

setup(
    # naziv komponente prilikom instaliranja
    name="coree",
    # verzija komponente
    version="0.1",
    # Distribucija svih paketa koji se nalaze u `.` direktorijumu.
    # Moguce je izabrate samo neke pakete i dati ih u vidu liste.
    packages=find_packages(),
    # Paketi rs, rs.uns i rs.uns.ftn su zajednicki za vise distribucija
    # (npr. Core, FakultetPrikazObican, FakultetPrikazSlozen, ...).
    # Da bismo izbegli clashing i omogucili deljenje potpaketa i modula
    # ovih paketa na vise distribucija, potrebno je definisati namespace-ove.
    # Takodje, `__init__.py` moduli ova tri paketa moraju sadrzati poziv
    # declare_namespace() funkcije.
    # Vise informacija mozete videti ovde:
    # https://github.com/vladaindjic/SPC-exchange-students/blob/master/ComponentsSimple/Core/setup.py
    namespace_packages=['core'],
    # Sta ova distribucija (komponenta) nudi ostalim komponentama na koriscenje.
    # Na ovaj nacin radimo export FakultetPrikazBase i FakultetUcitavanjeBase
    # apstraktnih servisa.
    provides=['core.services', 'models'],
    # Koje su ulazne tacke u nasu komponentu?
    # Ova komponenta se korista kao skripta iz konzole (terminala),
    # the pripada grupi `console_scripts`.
    # Ovoj komponenti dodeljujemo alias `sluzba_main` kojim mozemo pozvati
    # rs.uns.ftn.studentska.sluzba.console_main:main funckije iz CLI-a
    # upotrebno alias (tj. $ sluzba_main)
    # entry_points={
    #     'core_entry_point':
    #         ['core_alias=core:main'],
    # },
    # Da li je u redu da se nasa komponente spakuje u zip arhivu.
    zip_safe=True
)
