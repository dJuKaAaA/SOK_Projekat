# Projekat iz SOK-a - TIM 8

## Studenti

| Indeks | Ime i prezime |
| ------ | ------ |
| SV35/2020 | Miloš Stojanović |
| SV76/2020 | Miloš Stanojlović |
| SV77/2020 | Ivan Martić |
| SV79/2020 | Ivan Đukanović |

## Potrebne biblioteke

Za korišćenje programa potrebno je instalirati Django biblioteku.
Django biblioteka se može instalirati sledećom komandom:
```
pip install django
```

Nakon instalacije Django biblioteke, potrebno je instalirati core deo aplikacije. To se može učiniti pozicioniranjem u Core folder i pokretanjem sledeće komande:
```
python setup.py install
```

## Plugin-i

Postoje dva izvorišna plugin-a i dva vizualizaciona plugin-a. 

Prvi izvorišni plugin za izvor koristi File System računara.
Drugi izvorišni plugin za izvor koristi Twitter Followers API.
Prvi vizualizacioni plugin prikazuje čvorove grafa u jednostavnom prikazu gde se vidi samo identifikator čvora.
Drugi vizualizacioni plugin prikazuje čvorove grafa u složenijem prikazu gde se vide podaci koje čvor sadrži.

## Instalacija plugin-a

Izabrani plugin se može se instalirati pozicioniranjem u folder u kome se nalazi setup.py skripta za instaliranje plugin-a i pokretanjem sledeće komande:
```
python setup.py install
```

| Plugin | Ime foldera |
| ------ | ------ |
| File System parser | file_system_parser |
| Twitter Followers API plugin | twitter_api_parser |
| Simple Visualizator | simple_view_plugin |
| Complex Visualizator | complex_view_plugin |

## Skripte za automatizaciju

Ukoliko su svi plugin-i instalirani, pokretanjem skripte clean.sh će se obrisati svi folderi koji su kreirani pri instalaciji plugin-a i svi plugin-i će biti obrisani iz virtuelnog okruženja. Skripta se pokreće na sledeći način:
```
clean.sh
```

Pokretanjem skripte reset.sh će se desiti isto što i pokretanjem clean.sh skripte s tim da će se na kraju svi plugin-i instalirati. Skripta se pokreće na sledeći način:
```
reset.sh
```

Pokretanje Django servera se vrši pokretanjem run.sh skripte. Skripta se pokreće na sledeći način:
```
run.sh
```

