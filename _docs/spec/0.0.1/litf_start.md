# LITF version message Schema

```txt
litf_start
```

LITF version message


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [litf_start.schema.json](../../../spec/0.0.1/litf_start.schema.json "open original schema") |

## LITF version message Type

`object` ([LITF version message](litf_start.md))

## LITF version message Examples

```json
{
  "_type": "litf_start",
  "litf_version": "0.0.1"
}
```

# LITF version message Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                     |
| :---------------------------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| [\_type](#_type)              | `string` | Optional | cannot be null | [LITF version message](litf_start-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")                    |
| [litf_version](#litf_version) | `string` | Required | cannot be null | [LITF version message](litf_start-properties-the-litf_version-schema.md "\#/properties/litf_version#/properties/litf_version") |

## \_type

An explanation about the purpose of this instance.


`_type`

-   is optional
-   Type: `string` ([The \_type schema](litf_start-properties-the-_type-schema.md))
-   cannot be null
-   defined in: [LITF version message](litf_start-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")

### \_type Type

`string` ([The \_type schema](litf_start-properties-the-_type-schema.md))

### \_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | ----------- |
| `"litf_start"` |             |

## litf_version

An explanation about the purpose of this instance.


`litf_version`

-   is required
-   Type: `string` ([The litf_version schema](litf_start-properties-the-litf_version-schema.md))
-   cannot be null
-   defined in: [LITF version message](litf_start-properties-the-litf_version-schema.md "\#/properties/litf_version#/properties/litf_version")

### litf_version Type

`string` ([The litf_version schema](litf_start-properties-the-litf_version-schema.md))

### litf_version Examples

```json
"0.0.1"
```
