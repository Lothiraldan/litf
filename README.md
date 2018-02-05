# LITF

Language Independent Test Format is a new effort to have a language-independent test format that is designed to be easy to produce and consume.

It's somehow equivalent of Junit.xml but based on Line-delimited JSON and can be consumed in a streaming fashion. 

# JSON-Schema

The format is designed as test-formats present in the current directory.

# Compatible emitters

Usual emitters are test tools or frameworks.

## Python

- Pytest: [pytest-litf](https://github.com/Lothiraldan/pytest-litf).

# Compatible consumers

## Test orchestrator

- Balto: [BAlto is a Language independent Test Orchestrator](https://lothiraldan.github.io/balto/).

# Validator

You can use the `test.py` script to validate that an output is LITF valid. You can use it like this `pytest-litf "{}" | python /path/to/litf/test.py` or `python /path/to/litf/test.py < TEST_OUTPUT`.