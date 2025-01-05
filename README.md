# `Iuliia`

> Transliterate Cyrillic → Latin in every possible way

Transliteration means representing Cyrillic data (mainly names and geographic locations) with Latin letters. It is used for international passports, visas, green cards, driving licenses, mail and goods delivery etc.

`Iuliia` makes transliteration as easy as:

```python
>>> import iuliia
>>> iuliia.WIKIPEDIA.translate("Юлия Щеглова")
'Yuliya Shcheglova'
```

## Why use `Iuliia`

-   20 Russian transliteration schemas (all major international and national standards).
-   Official Uzbek transliteration schema.
-   Simple API and zero third-party dependencies.

For schema details and other information, see [iuliia.ru](https://iuliia.ru/) (in Russian).

[Limitations](https://github.com/nalgeon/iuliia/blob/master/README.md#issues-and-limitations)

## Installation

```sh
pip install iuliia
```

## Usage

Transliterate using specified schema:

```python
>>> source = "Юлия Щеглова"
>>> iuliia.ICAO_DOC_9303.translate(source)
'Iuliia Shcheglova'
```

Or pick schema by name

```python
>>> iuliia.schemas.has("wikipedia")
True
>>> schema = iuliia.schemas.get("wikipedia")
>>> schema.translate("Юлия Щеглова")
'Yuliya Shcheglova'
```

List all supported schemas:

```python
for name, schema in iuliia.schemas.items():
    print("{0:<20}{1}".format(name, schema.description))
```

```text
ala_lc              ALA-LC transliteration schema
ala_lc_alt          ALA-LC transliteration schema
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
uz                  Uzbekistan cyr-lat transliteration schema
wikipedia           Wikipedia transliteration schema
yandex_maps         Yandex.Maps transliteration schema
yandex_money        Yandex.Money transliteration schema
```

Command line:

```sh
$ iuliia icao_doc_9303 "Юлия Щеглова"
Iuliia Shcheglova
```

## Development setup

```sh
$ python3 -m venv env
$ . env/bin/activate
$ make deps schemas
$ make
```

Development tasks:

```text
make [task]
```

```text
task                 help
------               ----
all                  Run tests with coverage and linting
coverage             Run tests with coverage
deps                 Install dependencies
lint                 Lint and static-check code
pull                 Pull code and schemas
push                 Push commits and tags
schemas              Update schemas
test                 Run functional tests
timing               Run performance tests
```

## Contributing

Contributions are welcome. For anything other than bugfixes, please first open an issue to discuss what you want to change.

Be sure to add or update tests as appropriate.

Use [Black](https://black.readthedocs.io/en/stable/) for code formatting.

## Release notes

See [CHANGELOG.md](CHANGELOG.md)

## License

[MIT](https://choosealicense.com/licenses/mit/)
