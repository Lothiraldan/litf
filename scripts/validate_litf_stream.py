# -*- coding: utf-8 -*-

# The MIT License (MIT)
# Copyright (c) 2020 Boris Feld
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

""" Test runner for validating LITF plugins
"""
import argparse
import json
import os.path
import sys
from os.path import abspath, dirname, join

from jsonschema import ValidationError, validate

current_dir = dirname(abspath(__file__))
script_dir = join(current_dir, "../spec")

VALID_TRANSITIONS = {
    None: ["litf_start"],
    "litf_start": ["session_start"],
    "session_start": ["test_collection", "test_result", "session_end"],
    "test_collection": ["test_collection", "session_end"],
    "test_result": ["test_result", "session_end"],
    "session_end": [],
}


def test(stream):
    errors = []
    warnings = []
    total_lines = 0
    valid_lines = 0

    current_state = None

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
            errors.append(("Invalid JSON line", line, str(e)))
            continue

        # Get the msg type
        try:
            msg_type = data["_type"]
        except KeyError:
            errors.append(("Missing msg_type", line))
            continue

        # Check that the transition is correct
        if msg_type not in VALID_TRANSITIONS[current_state]:
            errors.append(
                (
                    "Invalid transition",
                    line,
                    "%r is not a valid transition from %r" % (msg_type, current_state),
                )
            )
            continue

        # Get the schema
        litf_version = "0.0.1"  # TODO: Use the first message to get version
        schema_path = os.path.join(script_dir, litf_version, msg_type + ".schema.json")

        with open(schema_path, "r") as schema_file:
            schema = json.load(schema_file)

        # Validate the line
        try:
            validate(data, schema)
        except ValidationError as exc:
            errors.append(("Invalid data", line, str(exc)))
            continue

        current_state = msg_type

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
        "stream",
        help="Which file to read, use - for reading stdin instead",
        action="store",
        default="-",
    )

    args = parser.parse_args()

    if args.stream == "-":
        test(sys.stdin)
    else:
        with open(args.stream) as stream:
            test(stream)
