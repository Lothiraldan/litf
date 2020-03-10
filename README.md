# LITF

Language Independent Test Format is a new effort to have a language-independent test output and input format that is designed to be easy to produce and consume.

# Goals

The goals of this new format are:

- Be streamable.
- Be easy to write and read.
- Be extensible.
- Be an input format too.
- Be independant from any implementation.

# Definition

LITF is currently defined as a [JSON Lines](http://jsonlines.org/) format where every kind of message is defined as a separate JSON-Format. The specifications are located on the `spec` directory.

# Compatible emitters

Usual emitters are test tools or test frameworks.

## Python

- Pytest: [pytest-litf](https://github.com/Lothiraldan/pytest-litf).

## Shell

- Mercurial: [mercurial-litf](https://bitbucket.org/lothiraldan/mercurial_litf).

# Compatible consumers

## Test orchestrator

- Balto: [BAlto is a Language independent Test Orchestrator](https://lothiraldan.github.io/balto/).

# Validator script

You can use the `test.py` script to validate that an output is LITF valid. You can use it like this `pytest-litf "{}" | python /path/to/litf/scripts/test.py` or `python /path/to/litf/scripts/test.py < TEST_OUTPUT`.

# Output example

Here is an example of a LITF compatible output:

```json
{"test_number": 6, "_type": "session_start"}
{"test_name": "test_success", "file": "test_func.py", "outcome": "passed", "id": "test_func.py::test_success", "duration": 0.0003, "_type": "test_result", "skipped_messages": {}, "durations": {"call": 0.0001, "setup": 0.0001, "teardown": 0.0006}, "stderr": "", "line": 3, "stdout": "", "error": {"humanrepr": ""}}
{"test_name": "test_fails", "file": "test_func.py", "outcome": "failed", "id": "test_func.py::test_fails", "duration": 0.0003, "_type": "test_result", "skipped_messages": {}, "durations": {"call": 0.0001, "setup": 0.00008, "teardown": 0.0001}, "stderr": "", "line": 7, "stdout": "", "error": {"humanrepr": "def test_fails():\n>       assert False\nE       assert False\n\ntest_func.py:9: AssertionError"}}
{"test_name": "test_fixtures[0]", "file": "test_func.py", "outcome": "passed", "id": "test_func.py::test_fixtures[0]", "duration": 0.0006, "_type": "test_result", "skipped_messages": {}, "durations": {"call": 0.0001, "setup": 0.0004, "teardown": 0.0008}, "stderr": "", "line": 11, "stdout": "", "error": {"humanrepr": ""}}
{"test_name": "test_fixtures[1]", "file": "test_func.py", "outcome": "failed", "id": "test_func.py::test_fixtures[1]", "duration": 0.0005, "_type": "test_result", "skipped_messages": {}, "durations": {"call": 0.0002, "setup": 0.0001, "teardown": 0.0008}, "stderr": "", "line": 11, "stdout": "", "error": {"humanrepr": "number = 1\n\n    @pytest.mark.parametrize(\"number\", list(range(3)))\n    def test_fixtures(number):\n>       assert number % 2 == 0\nE       assert (1 % 2) == 0\n\ntest_func.py:14: AssertionError"}}
{"test_name": "test_fixtures[2]", "file": "test_func.py", "outcome": "passed", "id": "test_func.py::test_fixtures[2]", "duration": 0.0003, "_type": "test_result", "skipped_messages": {}, "durations": {"call": 0.0006, "setup": 0.0001, "teardown": 0.0006}, "stderr": "", "line": 11, "stdout": "", "error": {"humanrepr": ""}}
{"test_name": "test_error", "file": "test_func.py", "outcome": "failed", "id": "test_func.py::test_error", "duration": 0.0004, "_type": "test_result", "skipped_messages": {}, "durations": {"call": 0.0002, "setup": 0.0007, "teardown": 90.0007}, "stderr": "", "line": 16, "stdout": "", "error": {"humanrepr": "def test_error():\n>       1/0\nE       ZeroDivisionError: division by zero\n\ntest_func.py:18: ZeroDivisionError"}}

{"failed": 3, "total_duration": 0.03, "_type": "session_end", "skipped": 0, "error": 0, "passed": 3}
```

Here is what a nicely formated line looks like:

```json
{
  "test_name": "test_error",
  "file": "test_func.py",
  "outcome": "failed",
  "id": "test_func.py::test_error",
  "duration": 0.0004036426544189453,
  "_type": "test_result",
  "skipped_messages": {},
  "durations": {
    "call": 0.00023055076599121094,
    "setup": 7.62939453125e-05,
    "teardown": 9.679794311523438e-05
  },
  "stderr": "",
  "line": 16,
  "stdout": "",
  "error": {
    "humanrepr": "def test_error():\n>       1/0\nE       ZeroDivisionError: division by zero\n\ntest_func.py:18: ZeroDivisionError"
  }
}
```

The `test_result` message contains:

- An unique `id`, which can be used to relaunch this specific test.
- A `test_name`, a human-friendly representation name of the test.
- The `file` and `line` where the test is defined.
- The `outcome` of the test, either `passed`, `failed`, `error` or `skipped`.
- The `skipped_messages` in case the case is skipped.
- The `duration` in seconds and detailed `durations` in seconds.
- The `stdout` and `stderr`.
- The `error` message.

The format doesn't handle yet:

- Support for snapshot testing, with either a textual or graphical diff.
- The version of the spec.
- Collection and runner errors.
- Log lines with their levels, DEBUG, INFO, ERROR...

# Input example

LITF is also an input format. Basically LITF-compatible emitters receive a json string as first argument.

For running all the tests, they would receive:

```bash
tool-litf '{}'
```

For collecting all the tests, they would receive:

```bash
tool-litf '{"collect-only": true}'
```

For collecting all the tests in specific files, they would receive:

```bash
tool-litf '{"collect-only": true, "files": ["test_file1", "test_file2"]}'
```

For running specific tests, they would receive:

```bash
tool-litf '{"nodeids": ["test_id1", "test_id2"]}'
```

# Alternatives

See [Comparison doc](_docs/comparison.md).