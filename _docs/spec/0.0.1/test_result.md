# A single test result Schema

```txt
test_rest
```

The test_collection message contains all identifying information about a test, its status and any information needed to debug it.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------------- |
| Can be instantiated | Yes        | Unknown status | No           | Forbidden         | Forbidden             | none                | [test_result.schema.json](../../../spec/0.0.1/test_result.schema.json "open original schema") |

## A single test result Type

`object` ([A single test result](test_result.md))

## A single test result Examples

```json
{
  "_type": "test_result",
  "duration": 0.00029659271240234375,
  "durations": {
    "call": 0.00007081031799316406,
    "setup": 0.00016164779663085938,
    "teardown": 0.00006413459777832031
  },
  "error": {
    "humanrepr": ""
  },
  "file": "test_class.py",
  "id": "test_class.py::TestClassPassing::()::test_passing",
  "line": 8,
  "outcome": "passed",
  "skipped_messages": {},
  "stderr": "",
  "stdout": "",
  "test_name": "TestClassPassing.test_passing"
}
```

```json
{
  "_type": "test_result",
  "duration": 0.0004444122314453125,
  "durations": {
    "call": 0.00015401840209960938,
    "setup": 0.00010013580322265625,
    "teardown": 0.00019025802612304688
  },
  "error": {
    "humanrepr": "self = <test_class.TestClassFailing object at 0x7f7fd3fd18d0>\n\n    def test_failing(self):\n>       assert False\nE       assert False\n\ntest_class.py:22: AssertionError"
  },
  "file": "test_class.py",
  "id": "test_class.py::TestClassFailing::()::test_failing",
  "line": 20,
  "outcome": "failed",
  "skipped_messages": {},
  "stderr": "",
  "stdout": "",
  "test_name": "TestClassFailing.test_failing"
}
```

```json
{
  "_type": "test_result",
  "duration": 0.00018453598022460938,
  "durations": {
    "setup": 0.00010895729064941406,
    "teardown": 0.00007557868957519531
  },
  "error": {
    "humanrepr": ""
  },
  "file": "test_skip.py",
  "id": "test_skip.py::test_skip_function",
  "line": 2,
  "outcome": "skipped",
  "skipped_messages": {
    "setup": "Skipped: Skip"
  },
  "stderr": "",
  "stdout": "",
  "test_name": "test_skip_function"
}
```

# A single test result Properties

| Property                              | Type      | Required | Nullable       | Defined by                                                                                                             |
| :------------------------------------ | --------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------- |
| [\_type](#_type)                      | `string`  | Required | cannot be null | [A single test result](test_result-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")           |
| [duration](#duration)                 | `number`  | Optional | cannot be null | [A single test result](test_result-properties-the-duration-schema.md "\#/properties/duration#/properties/duration")    |
| [durations](#durations)               | `object`  | Optional | cannot be null | [A single test result](test_result-properties-the-durations-schema.md "\#/properties/durations#/properties/durations") |
| [error](#error)                       | `object`  | Optional | cannot be null | [A single test result](test_result-properties-the-error-schema.md "\#/properties/error#/properties/error")             |
| [file](#file)                         | `string`  | Optional | cannot be null | [A single test result](test_result-properties-the-file-schema.md "\#/properties/file#/properties/file")                |
| [id](#id)                             | `string`  | Required | cannot be null | [A single test result](test_result-properties-the-id-schema.md "\#/properties/id#/properties/id")                      |
| [line](#line)                         | `integer` | Optional | cannot be null | [A single test result](test_result-properties-the-line-schema.md "\#/properties/line#/properties/line")                |
| [logs](#logs)                         | `string`  | Optional | cannot be null | [A single test result](test_result-properties-logs.md "test_rest#/properties/logs")                                    |
| [outcome](#outcome)                   | `string`  | Required | cannot be null | [A single test result](test_result-properties-the-outcome-schema.md "\#/properties/outcome#/properties/outcome")       |
| [skipped_messages](#skipped_messages) | `object`  | Optional | cannot be null | [A single test result](test_result-properties-skipped_messages.md "test_rest#/properties/skipped_messages")            |
| [stderr](#stderr)                     | `string`  | Optional | cannot be null | [A single test result](test_result-properties-the-stderr-schema.md "\#/properties/stderr#/properties/stderr")          |
| [stdout](#stdout)                     | `string`  | Optional | cannot be null | [A single test result](test_result-properties-the-stdout-schema.md "\#/properties/stdout#/properties/stdout")          |
| [test_name](#test_name)               | `string`  | Optional | cannot be null | [A single test result](test_result-properties-the-test_name-schema.md "\#/properties/test_name#/properties/test_name") |

## \_type

An explanation about the purpose of this instance.


`_type`

-   is required
-   Type: `string` ([The \_type schema](test_result-properties-the-_type-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")

### \_type Type

`string` ([The \_type schema](test_result-properties-the-_type-schema.md))

### \_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | ----------- |
| `"test_result"` |             |

## duration

An explanation about the purpose of this instance.


`duration`

-   is optional
-   Type: `number` ([The duration schema](test_result-properties-the-duration-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-duration-schema.md "\#/properties/duration#/properties/duration")

### duration Type

`number` ([The duration schema](test_result-properties-the-duration-schema.md))

### duration Examples

```json
0.00029659271240234375
```

## durations

An explanation about the purpose of this instance.


`durations`

-   is optional
-   Type: `object` ([The durations schema](test_result-properties-the-durations-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-durations-schema.md "\#/properties/durations#/properties/durations")

### durations Type

`object` ([The durations schema](test_result-properties-the-durations-schema.md))

## error

An explanation about the purpose of this instance.


`error`

-   is optional
-   Type: `object` ([The error schema](test_result-properties-the-error-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-error-schema.md "\#/properties/error#/properties/error")

### error Type

`object` ([The error schema](test_result-properties-the-error-schema.md))

## file

An explanation about the purpose of this instance.


`file`

-   is optional
-   Type: `string` ([The file schema](test_result-properties-the-file-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-file-schema.md "\#/properties/file#/properties/file")

### file Type

`string` ([The file schema](test_result-properties-the-file-schema.md))

### file Examples

```json
"test_class.py"
```

## id

An explanation about the purpose of this instance.


`id`

-   is required
-   Type: `string` ([The id schema](test_result-properties-the-id-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-id-schema.md "\#/properties/id#/properties/id")

### id Type

`string` ([The id schema](test_result-properties-the-id-schema.md))

### id Examples

```json
"test_class.py::TestClassPassing::()::test_passing"
```

## line

An explanation about the purpose of this instance.


`line`

-   is optional
-   Type: `integer` ([The line schema](test_result-properties-the-line-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-line-schema.md "\#/properties/line#/properties/line")

### line Type

`integer` ([The line schema](test_result-properties-the-line-schema.md))

### line Examples

```json
8
```

## logs




`logs`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [A single test result](test_result-properties-logs.md "test_rest#/properties/logs")

### logs Type

`string`

## outcome

An explanation about the purpose of this instance.


`outcome`

-   is required
-   Type: `string` ([The outcome schema](test_result-properties-the-outcome-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-outcome-schema.md "\#/properties/outcome#/properties/outcome")

### outcome Type

`string` ([The outcome schema](test_result-properties-the-outcome-schema.md))

### outcome Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | ----------- |
| `"passed"`  |             |
| `"failed"`  |             |
| `"skipped"` |             |

## skipped_messages




`skipped_messages`

-   is optional
-   Type: `object` ([Details](test_result-properties-skipped_messages.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-skipped_messages.md "test_rest#/properties/skipped_messages")

### skipped_messages Type

`object` ([Details](test_result-properties-skipped_messages.md))

## stderr

An explanation about the purpose of this instance.


`stderr`

-   is optional
-   Type: `string` ([The stderr schema](test_result-properties-the-stderr-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-stderr-schema.md "\#/properties/stderr#/properties/stderr")

### stderr Type

`string` ([The stderr schema](test_result-properties-the-stderr-schema.md))

### stderr Examples

```json
""
```

## stdout

An explanation about the purpose of this instance.


`stdout`

-   is optional
-   Type: `string` ([The stdout schema](test_result-properties-the-stdout-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-stdout-schema.md "\#/properties/stdout#/properties/stdout")

### stdout Type

`string` ([The stdout schema](test_result-properties-the-stdout-schema.md))

### stdout Examples

```json
""
```

## test_name

An explanation about the purpose of this instance.


`test_name`

-   is optional
-   Type: `string` ([The test_name schema](test_result-properties-the-test_name-schema.md))
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-test_name-schema.md "\#/properties/test_name#/properties/test_name")

### test_name Type

`string` ([The test_name schema](test_result-properties-the-test_name-schema.md))

### test_name Examples

```json
"TestClassPassing.test_passing"
```

# A single test result Definitions
