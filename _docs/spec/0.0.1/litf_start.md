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
  "litf_version": "0.0.1"
}
```

# LITF version message Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                     |
| :---------------------------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| [litf_version](#litf_version) | `string` | Required | cannot be null | [LITF version message](litf_start-properties-the-litf_version-schema.md "\#/properties/litf_version#/properties/litf_version") |

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
