# The outcome schema Schema

```txt
#/properties/outcome#/properties/outcome
```

An explanation about the purpose of this instance.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                      |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [test_result.schema.json\*](../../../spec/0.0.1/test_result.schema.json "open original schema") |

## outcome Type

`string` ([The outcome schema](test_result-properties-the-outcome-schema.md))

## outcome Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | ----------- |
| `"passed"`  |             |
| `"failed"`  |             |
| `"skipped"` |             |
