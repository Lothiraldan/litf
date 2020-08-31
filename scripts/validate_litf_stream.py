""" Test runner for validating LITF plugins
"""
import argparse
import json
import os.path
import sys
from os.path import abspath, dirname, join

from jsonschema import ValidationError, validate

current_dir = dirname(abspath(__file__))
script_dir = join(current_dir, '../spec')


def test(stream):
    errors = []
    warnings = []
    total_lines = 0
    valid_lines = 0

    # Check stdout
    for line in stream.readlines():

        line = line.strip()

        # Ignore empty line
        if not line:
            continue

        # Count not empty lines
        total_lines += 1

        # Check that the data is valid JSON
        try:
            data = json.loads(line)
        except (json.JSONDecodeError, ValueError) as e:
            errors.append(("Invalid JSON line", line))
            continue

        # Get the msg type
        try:
            msg_type = data["_type"]
        except KeyError:
            errors.append(("Missing msg_type", line))
            continue

        # Get the schema
        schema_path = os.path.join(script_dir, msg_type + ".json")

        with open(schema_path, 'r') as schema_file:
            schema = json.load(schema_file)

        # Validate the line
        try:
            validate(data, schema)
        except ValidationError as exc:
            errors.append(("Invalid data", line, str(exc)))
            continue

        # Validate the logic
        # TODO

        valid_lines += 1

    print("%d/%d valid lines" % (valid_lines, total_lines))

    if errors:
        print("%d ERRORS" % len(errors))
        for error in errors:
            print("Error:    ".join(error))

    if warnings:
        print("%d WARNINGS" % len(warnings))
        for warning in warnings:
            print("Warning:   ".join(warning))

    if errors:
        sys.exit(1)

    if not errors and not warnings:
        print("OK")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "stream", help="Which file to read, use - for reading stdin instead", action="store", default="-"
    )

    args = parser.parse_args()

    if args.stream == "-":
        test(sys.stdin)
    else:
        with open(args.stream) as stream:
            test(stream)
