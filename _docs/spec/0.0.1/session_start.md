# The start of the session Schema

```txt
session_start
```

The start of the session follow the LITF version and precede the collection or results messages.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [session_start.schema.json](../../../spec/0.0.1/session_start.schema.json "open original schema") |

## The start of the session Type

`object` ([The start of the session](session_start.md))

## The start of the session Default Value

The default value is:

```json
{}
```

## The start of the session Examples

```json
{
  "_type": "session_start",
  "test_number": 29
}
```

# The start of the session Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                         |
| :-------------------------- | --------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| [\_type](#_type)            | `string`  | Required | cannot be null | [The start of the session](session_start-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")                 |
| [test_number](#test_number) | `integer` | Required | cannot be null | [The start of the session](session_start-properties-the-test_number-schema.md "\#/properties/test_number#/properties/test_number") |

## \_type

An explanation about the purpose of this instance.


`_type`

-   is required
-   Type: `string` ([The \_type schema](session_start-properties-the-_type-schema.md))
-   cannot be null
-   defined in: [The start of the session](session_start-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")

### \_type Type

`string` ([The \_type schema](session_start-properties-the-_type-schema.md))

### \_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | ----------- |
| `"session_start"` |             |

## test_number

An explanation about the purpose of this instance.


`test_number`

-   is required
-   Type: `integer` ([The test_number schema](session_start-properties-the-test_number-schema.md))
-   cannot be null
-   defined in: [The start of the session](session_start-properties-the-test_number-schema.md "\#/properties/test_number#/properties/test_number")

### test_number Type

`integer` ([The test_number schema](session_start-properties-the-test_number-schema.md))

### test_number Examples

```json
29
```
