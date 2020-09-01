# The root schema Schema

```txt
http://example.com/example.json
```

The root schema comprises the entire JSON document.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [litf_start.schema.json](../../../out/litf_start.schema.json "open original schema") |

## The root schema Type

`object` ([The root schema](litf_start.md))

## The root schema Examples

```json
{
  "litf_version": "0.0.1"
}
```

# The root schema Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                |
| :---------------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------ |
| [litf_version](#litf_version) | `string` | Required | cannot be null | [The root schema](litf_start-properties-the-litf_version-schema.md "\#/properties/litf_version#/properties/litf_version") |
| Additional Properties         | Any      | Optional | can be null    |                                                                                                                           |

## litf_version

An explanation about the purpose of this instance.


`litf_version`

-   is required
-   Type: `string` ([The litf_version schema](litf_start-properties-the-litf_version-schema.md))
-   cannot be null
-   defined in: [The root schema](litf_start-properties-the-litf_version-schema.md "\#/properties/litf_version#/properties/litf_version")

### litf_version Type

`string` ([The litf_version schema](litf_start-properties-the-litf_version-schema.md))

### litf_version Examples

```json
"0.0.1"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
