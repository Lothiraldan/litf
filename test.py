""" Test runner for validating LITF plugins
"""

import json
import os
import os.path
import shlex
import subprocess
import sys

from jsonschema import ValidationError, validate

script_dir = os.path.dirname(os.path.abspath(__file__))


def test(cmd, directory):
    # Change directory
    os.chdir(directory)

    # Launch the script
    # TODO check input too
    process = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    errors = []
    warnings = []
    total_lines = 0
    valid_lines = 0

    # Check stdout
    for line in process.stdout:

        line = line.strip()

        # Ignore empty line
        if not line:
            continue

        # Count not empty lines
        total_lines += 1

        # Check that the data is UTF-8
        try:
            decodedline = line.decode("UTF-8")
        except UnicodeDecodeError:
            errors.append(("Invalid UTF-8 line", repr(decodedline)))
            continue

        # Check that the data is valid JSON
        try:
            data = json.loads(decodedline)
        except (json.JSONDecodeError, ValueError) as e:
            errors.append(("Invalid JSON line", decodedline))
            continue

        # Get the msg type
        try:
            msg_type = data["_type"]
        except KeyError:
            errors.append(("Missing msg_type", decodedline))
            continue

        # Get the schema
        schema_path = os.path.join(script_dir, msg_type + ".json")

        with open(schema_path, 'r') as schema_file:
            schema = json.load(schema_file)

        # Validate the line
        try:
            validate(data, schema)
        except ValidationError as exc:
            errors.append(("Invalid data", decodedline, str(exc)))
            continue

        # Validate the logic
        # TODO

        valid_lines += 1

    # Check stderr
    for line in process.stderr:
        warnings.append(("Stderr line", repr(line)))

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
    test(sys.argv[1:-1], sys.argv[-1])
