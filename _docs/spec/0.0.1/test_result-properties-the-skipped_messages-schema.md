# The skipped_messages schema Schema

```txt
#/properties/skipped_messages#/properties/skipped_messages
```

This field contains the skipped message or reasons, the field name coud indicate when the test was marked as skipped, for example during setup or the actuall call.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                      |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [test_result.schema.json\*](../../../spec/0.0.1/test_result.schema.json "open original schema") |

## skipped_messages Type

`object` ([The skipped_messages schema](test_result-properties-the-skipped_messages-schema.md))

## skipped_messages Default Value

The default value is:

```json
{}
```

## skipped_messages Examples

```json
{
  "setup": "Skipped: Skip"
}
```

# The skipped_messages schema Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                             |
| :-------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `^.*$`                | `number` | Optional | cannot be null | [A single test result](test_result-properties-the-skipped_messages-schema-patternproperties-.md "\#/properties/skipped_messages#/properties/skipped_messages/patternProperties/^.\*$") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                        |

## Pattern: `^.*$`




`^.*$`

-   is optional
-   Type: `number`
-   cannot be null
-   defined in: [A single test result](test_result-properties-the-skipped_messages-schema-patternproperties-.md "\#/properties/skipped_messages#/properties/skipped_messages/patternProperties/^.\*$")

### ^.\*$ Type

`number`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
