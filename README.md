# `Iuliia`
> Transliterate Cyrillic → Latin in every possible way

Transliteration means representing Cyrillic data (mainly names and geographic locations) with Latin letters. It is used for international passports, visas, green cards, driving licenses, mail and goods delivery etc.

`Iuliia` makes transliteration as easy as:

```python
>>> import iuliia
>>> iuliia.translate("Юлия Щеглова", schema=iuliia.WIKIPEDIA)
'Yuliya Shcheglova'
```

## Why use `Iuliia`

- 19 transliteration schemas (rule sets), including all main international and Russian standards.
- Correctly implements not only the base mapping, but all the special rules for letter combinations and word endings (AFAIK, Iuliia is the only library which does so).
- Simple API and zero third-party dependencies.

Supports actual schemas:

- ALA-LC (coming soon)
- BGN/PCGN (coming soon)
- BS 2979:1958 (coming soon)
- GOST R 52290-2004 (coming soon)
- GOST R 7.0.34-2014 (coming soon)
- ICAO DOC 9303 (coming soon)
- ISO 9:1995 (aka GOST 7.79-2000, coming soon)
- UNGEGN 1987 V/18 (coming soon)
- Scientific (coming soon)
- Telegram (coming soon)
- Wikipedia (`iuliia.WIKIPEDIA`)
- Yandex.Maps (`iuliia.YANDEX_MAPS`)
- Yandex.Money (`iuliia.YANDEX_MONEY`)

And deprecated ones (coming soon):

- GOST 16876-71
- GOST R 52535.1-2006
- ISO/R 9:1954
- ISO/R 9:1968
- MVD 310-1997
- MVD 782-2000

For schema details and other information, see <https://dangry.ru/iuliia> (in Russian).

## Installation

```sh
pip install iuliia
```

## Usage

API:

```python
import iuliia

# list all supported schemas
for schema_name in iuliia.Schemas.names():
    print(schema_name)

# transliterate using specified schema
source = "Юлия Щеглова"
iuliia.translate(source, schema=iuliia.ICAO_DOC_9303)
# "Iuliia Shcheglova"

# or pick schema by name
schema = iuliia.Schemas.get('wikipedia')
iuliia.translate(source, schema)
# "Yuliya Shcheglova"
```

Command line:

```sh
$ iuliia icao_doc_9303 "Юлия Щеглова"
Iuliia Shcheglova
```

## Development setup

```sh
$ pip install black coverage flake8 pylint pytest tox
$ tox
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Make sure to add or update tests as appropriate.

Use [Black](https://black.readthedocs.io/en/stable/) for code formatting and [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) for commit messages.

## [Changelog](CHANGELOG.md)

## License

[MIT](https://choosealicense.com/licenses/mit/)