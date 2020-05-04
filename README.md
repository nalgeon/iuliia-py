# `Iuliia`

> Transliterate Cyrillic → Latin in every possible way

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![Code Quality][quality-image]][quality-url]

Transliteration means representing Cyrillic data (mainly names and geographic locations) with Latin letters. It is used for international passports, visas, green cards, driving licenses, mail and goods delivery etc.

`Iuliia` makes transliteration as easy as:

```python
>>> import iuliia
>>> iuliia.translate("Юлия Щеглова", schema=iuliia.WIKIPEDIA)
'Yuliya Shcheglova'
```

## Why use `Iuliia`

-   [20 transliteration schemas](https://github.com/nalgeon/iuliia/blob/master/README.md#supported-schemas) (rule sets), including all main international and Russian standards.
-   Correctly implements not only the base mapping, but all the special rules for letter combinations and word endings (AFAIK, Iuliia is the only library which does so).
-   Simple API and zero third-party dependencies.

For schema details and other information, see <https://dangry.ru/iuliia> (in Russian).

[Issues and limitations](https://github.com/nalgeon/iuliia/blob/master/README.md#issues-and-limitations)

## Installation

```sh
pip install iuliia
```

## Usage

List all supported schemas:

```python
>>> import iuliia
>>> import iuliia
>>> for name, schema in iuliia.Schemas.items():
...     print("{0:<20}{1}".format(name, schema.description))
...
ala_lc              ALA-LC transliteration schema.
ala_lc_alt          ALA-LC transliteration schema.
bgn_pcgn            BGN/PCGN transliteration schema
bgn_pcgn_alt        BGN/PCGN transliteration schema
bs_2979             British Standard 2979:1958 transliteration schema
bs_2979_alt         British Standard 2979:1958 transliteration schema
gost_16876          GOST 16876-71 (aka GOST 1983) transliteration schema
gost_16876_alt      GOST 16876-71 (aka GOST 1983) transliteration schema
gost_52290          GOST R 52290-2004 transliteration schema
gost_52535          GOST R 52535.1-2006 transliteration schema
gost_7034           GOST R 7.0.34-2014 transliteration schema
gost_779            GOST 7.79-2000 (aka ISO 9:1995) transliteration schema
gost_779_alt        GOST 7.79-2000 (aka ISO 9:1995) transliteration schema
icao_doc_9303       ICAO DOC 9303 transliteration schema
iso_9_1954          ISO/R 9:1954 transliteration schema
iso_9_1968          ISO/R 9:1968 transliteration schema
iso_9_1968_alt      ISO/R 9:1968 transliteration schema
mosmetro            Moscow Metro map transliteration schema
mvd_310             MVD 310-1997 transliteration schema
mvd_310_fr          MVD 310-1997 transliteration schema
mvd_782             MVD 782-2000 transliteration schema
scientific          Scientific transliteration schema
telegram            Telegram transliteration schema
ungegn_1987         UNGEGN 1987 V/18 transliteration schema
wikipedia           Wikipedia transliteration schema
yandex_maps         Yandex.Maps transliteration schema
yandex_money        Yandex.Money transliteration schema
```

Transliterate using specified schema:

```python
>>> source = "Юлия Щеглова"
>>> iuliia.translate(source, schema=iuliia.ICAO_DOC_9303)
'Iuliia Shcheglova'
```

Or pick schema by name

```python
>>> schema = iuliia.Schemas.get("wikipedia")
>>> iuliia.translate(source, schema)
'Yuliya Shcheglova'
```

Command line:

```sh
$ iuliia icao_doc_9303 "Юлия Щеглова"
Iuliia Shcheglova
```

## Development setup

```sh
$ make update-schemas
$ pip install black coverage flake8 mccabe mypy pylint pytest tox
$ tox
```

Development tasks (`make ...`):

```
changelog   Generate changelog
coverage    Run tests with coverage
lint        Lint and static-check code
pull        Pull code and schemas
push        Push commits and tags
schemas     Update schemas
test        Run tests
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Make sure to add or update tests as appropriate.

Use [Black](https://black.readthedocs.io/en/stable/) for code formatting and [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) for commit messages.

## [Changelog](CHANGELOG.md)

## License

[MIT](https://choosealicense.com/licenses/mit/)

<!-- Markdown link & img dfn's -->

[pypi-image]: https://img.shields.io/pypi/v/iuliia?style=flat-square
[pypi-url]: https://pypi.org/project/iuliia/
[build-image]: https://img.shields.io/travis/nalgeon/iuliia-py?style=flat-square
[build-url]: https://travis-ci.org/nalgeon/iuliia-py
[coverage-image]: https://img.shields.io/coveralls/github/nalgeon/iuliia-py?style=flat-square
[coverage-url]: https://coveralls.io/github/nalgeon/iuliia-py
[quality-image]: https://img.shields.io/codeclimate/maintainability/nalgeon/iuliia-py?style=flat-square
[quality-url]: https://codeclimate.com/github/nalgeon/iuliia-py
