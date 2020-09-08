# README

## Top-level Schemas

-   [A single test collection message](./test_collection.md "The test_collection message contains all identifying information about a test that has been collected but not runned") – `test_collection`
-   [A single test result](./test_result.md "The test_collection message contains all identifying information about a test, its status and any information needed to debug it") – `test_rest`
-   [LITF version message](./litf_start.md "LITF version message") – `litf_start`
-   [The end of a session](./session_end.md "The session_end message closes the session") – `session_end`
-   [The start of the session](./session_start.md "The start of the session follow the LITF version and precede the collection or results messages") – `session_start`

## Other Schemas

### Objects

-   [The durations schema](./test_result-properties-the-durations-schema.md "An explanation about the purpose of this instance") – `#/properties/durations#/properties/durations`
-   [The skipped_messages schema](./test_result-properties-the-skipped_messages-schema.md "This field contains the skipped message or reasons, the field name coud indicate when the test was marked as skipped, for example during setup or the actuall call") – `#/properties/skipped_messages#/properties/skipped_messages`

### Arrays
