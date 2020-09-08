# The end of a session Schema

```txt
session_end
```

The session_end message closes the session.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [session_end.schema.json](../../../spec/0.0.1/session_end.schema.json "open original schema") |

## The end of a session Type

`object` ([The end of a session](session_end.md))

## The end of a session Default Value

The default value is:

```json
{}
```

## The end of a session Examples

```json
{
  "_type": "session_end",
  "error": 4,
  "failed": 9,
  "passed": 14,
  "skipped": 4,
  "total_duration": 2.1059529781341553
}
```

# The end of a session Properties

| Property                          | Type      | Required | Nullable       | Defined by                                                                                                                            |
| :-------------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| [\_type](#_type)                  | `string`  | Required | cannot be null | [The end of a session](session_end-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")                          |
| [error](#error)                   | `integer` | Required | cannot be null | [The end of a session](session_end-properties-the-error-schema.md "\#/properties/error#/properties/error")                            |
| [failed](#failed)                 | `integer` | Required | cannot be null | [The end of a session](session_end-properties-the-failed-schema.md "\#/properties/failed#/properties/failed")                         |
| [passed](#passed)                 | `integer` | Required | cannot be null | [The end of a session](session_end-properties-the-passed-schema.md "\#/properties/passed#/properties/passed")                         |
| [skipped](#skipped)               | `integer` | Required | cannot be null | [The end of a session](session_end-properties-the-skipped-schema.md "\#/properties/skipped#/properties/skipped")                      |
| [total_duration](#total_duration) | `number`  | Required | cannot be null | [The end of a session](session_end-properties-the-total_duration-schema.md "\#/properties/total_duration#/properties/total_duration") |

## \_type

An explanation about the purpose of this instance.


`_type`

-   is required
-   Type: `string` ([The \_type schema](session_end-properties-the-_type-schema.md))
-   cannot be null
-   defined in: [The end of a session](session_end-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")

### \_type Type

`string` ([The \_type schema](session_end-properties-the-_type-schema.md))

### \_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value           | Explanation |
| :-------------- | ----------- |
| `"session_end"` |             |

## error

An explanation about the purpose of this instance.


`error`

-   is required
-   Type: `integer` ([The error schema](session_end-properties-the-error-schema.md))
-   cannot be null
-   defined in: [The end of a session](session_end-properties-the-error-schema.md "\#/properties/error#/properties/error")

### error Type

`integer` ([The error schema](session_end-properties-the-error-schema.md))

### error Examples

```json
4
```

## failed

An explanation about the purpose of this instance.


`failed`

-   is required
-   Type: `integer` ([The failed schema](session_end-properties-the-failed-schema.md))
-   cannot be null
-   defined in: [The end of a session](session_end-properties-the-failed-schema.md "\#/properties/failed#/properties/failed")

### failed Type

`integer` ([The failed schema](session_end-properties-the-failed-schema.md))

### failed Examples

```json
9
```

## passed

An explanation about the purpose of this instance.


`passed`

-   is required
-   Type: `integer` ([The passed schema](session_end-properties-the-passed-schema.md))
-   cannot be null
-   defined in: [The end of a session](session_end-properties-the-passed-schema.md "\#/properties/passed#/properties/passed")

### passed Type

`integer` ([The passed schema](session_end-properties-the-passed-schema.md))

### passed Examples

```json
14
```

## skipped

An explanation about the purpose of this instance.


`skipped`

-   is required
-   Type: `integer` ([The skipped schema](session_end-properties-the-skipped-schema.md))
-   cannot be null
-   defined in: [The end of a session](session_end-properties-the-skipped-schema.md "\#/properties/skipped#/properties/skipped")

### skipped Type

`integer` ([The skipped schema](session_end-properties-the-skipped-schema.md))

### skipped Examples

```json
4
```

## total_duration

An explanation about the purpose of this instance.


`total_duration`

-   is required
-   Type: `number` ([The total_duration schema](session_end-properties-the-total_duration-schema.md))
-   cannot be null
-   defined in: [The end of a session](session_end-properties-the-total_duration-schema.md "\#/properties/total_duration#/properties/total_duration")

### total_duration Type

`number` ([The total_duration schema](session_end-properties-the-total_duration-schema.md))

### total_duration Examples

```json
2.1059529781341553
```
