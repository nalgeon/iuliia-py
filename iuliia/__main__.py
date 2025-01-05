"""
Iuliia command-line interface
"""

import sys
import iuliia


def main():
    """Transliterate string from command line"""
    if len(sys.argv) < 3:
        print("usage: iuliia SCHEMA SOURCE")
        print("Supported schemas:")
        print("\n".join(iuliia.schemas.names()))
        sys.exit(1)

    schema_name = sys.argv[1]
    schema = iuliia.schemas.get(schema_name)
    if schema is None:
        print(f"Schema '{schema_name}' does not exist. Supported schemas:")
        print("\n".join(iuliia.schemas.names()))
        sys.exit(1)

    source = sys.argv[2]
    result = schema.translate(source)
    print(result)


if __name__ == "__main__":
    main()
