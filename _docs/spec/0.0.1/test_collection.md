# A single test collection message Schema

```txt
test_collection
```

The test_collection message contains all identifying information about a test that has been collected but not runned.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ----------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [test_collection.schema.json](../../../spec/0.0.1/test_collection.schema.json "open original schema") |

## A single test collection message Type

`object` ([A single test collection message](test_collection.md))

## A single test collection message Default Value

The default value is:

```json
{}
```

## A single test collection message Examples

```json
{
  "_type": "test_collection",
  "file": "test_class.py",
  "id": "test_class.py::TestClassPassing::()::test_passing",
  "line": 8,
  "test_name": "TestClassPassing.test_passing"
}
```

# A single test collection message Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                             |
| :---------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| [\_type](#_type)        | `string`  | Required | cannot be null | [A single test collection message](test_collection-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")           |
| [file](#file)           | `string`  | Optional | cannot be null | [A single test collection message](test_collection-properties-the-file-schema.md "\#/properties/file#/properties/file")                |
| [id](#id)               | `string`  | Required | cannot be null | [A single test collection message](test_collection-properties-the-id-schema.md "\#/properties/id#/properties/id")                      |
| [line](#line)           | `integer` | Optional | cannot be null | [A single test collection message](test_collection-properties-the-line-schema.md "\#/properties/line#/properties/line")                |
| [test_name](#test_name) | `string`  | Optional | cannot be null | [A single test collection message](test_collection-properties-the-test_name-schema.md "\#/properties/test_name#/properties/test_name") |

## \_type

An explanation about the purpose of this instance.


`_type`

-   is required
-   Type: `string` ([The \_type schema](test_collection-properties-the-_type-schema.md))
-   cannot be null
-   defined in: [A single test collection message](test_collection-properties-the-_type-schema.md "\#/properties/\_type#/properties/\_type")

### \_type Type

`string` ([The \_type schema](test_collection-properties-the-_type-schema.md))

### \_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value               | Explanation |
| :------------------ | ----------- |
| `"test_collection"` |             |

## file

An explanation about the purpose of this instance.


`file`

-   is optional
-   Type: `string` ([The file schema](test_collection-properties-the-file-schema.md))
-   cannot be null
-   defined in: [A single test collection message](test_collection-properties-the-file-schema.md "\#/properties/file#/properties/file")

### file Type

`string` ([The file schema](test_collection-properties-the-file-schema.md))

### file Examples

```json
"test_class.py"
```

## id

An explanation about the purpose of this instance.


`id`

-   is required
-   Type: `string` ([The id schema](test_collection-properties-the-id-schema.md))
-   cannot be null
-   defined in: [A single test collection message](test_collection-properties-the-id-schema.md "\#/properties/id#/properties/id")

### id Type

`string` ([The id schema](test_collection-properties-the-id-schema.md))

### id Examples

```json
"test_class.py::TestClassPassing::()::test_passing"
```

## line

An explanation about the purpose of this instance.


`line`

-   is optional
-   Type: `integer` ([The line schema](test_collection-properties-the-line-schema.md))
-   cannot be null
-   defined in: [A single test collection message](test_collection-properties-the-line-schema.md "\#/properties/line#/properties/line")

### line Type

`integer` ([The line schema](test_collection-properties-the-line-schema.md))

### line Examples

```json
8
```

## test_name

An explanation about the purpose of this instance.


`test_name`

-   is optional
-   Type: `string` ([The test_name schema](test_collection-properties-the-test_name-schema.md))
-   cannot be null
-   defined in: [A single test collection message](test_collection-properties-the-test_name-schema.md "\#/properties/test_name#/properties/test_name")

### test_name Type

`string` ([The test_name schema](test_collection-properties-the-test_name-schema.md))

### test_name Examples

```json
"TestClassPassing.test_passing"
```
