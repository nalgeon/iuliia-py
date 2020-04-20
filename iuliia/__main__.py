"""
Iuliia command-line interface
"""

import sys
import iuliia


def main():
    """Transliterate string from command line"""
    if len(sys.argv) < 3:
        print("usage: iuliia SCHEMA SOURCE")
        sys.exit(1)

    schema_name = sys.argv[1]
    schema = iuliia.Schemas.__members__.get(schema_name)
    if schema is None:
        schemas = list(iuliia.Schemas.__members__.keys())
        print(f"Schema {schema_name} does not exist. Supported schemas:\n{schemas}")
        sys.exit(1)

    source = sys.argv[2]
    result = iuliia.translate(source, schema=schema.value)
    print(result)


if __name__ == "__main__":
    main()
