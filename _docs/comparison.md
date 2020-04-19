---
title: LITF versus other test formats
permalink: /docs/comparison/
---

The goal of LITF is to offer both an output format for test result (which is similar to what exists today) but also an input format in order to being able to select precisely what test subset to launch.

# LITF vs Junit.xml

`Junit.xml` is a well-known test output format vastly used in various community and supported by most of CI tools.

## Pros

- Well supported by testing and CI tools.

## Cons

- `junit.xml` output is generated at the end of a the test suite execution and if not, streaming it would require a XML streamer based reader which might be hard for some languages.
- There is no single and accepted definition for junit.xml, which means that various tools might produce incompatible files. For example:
    - https://github.com/kyrus/python-junit-xml/issues/63
    - https://stackoverflow.com/questions/442556/spec-for-junit-xml-output

# LITF vs TAP

[TAP](http://testanything.org/) is another well-know test output format.

## Pros

- Moderately supported by testing tools and CI tools.

## Cons

- TAP requires a ad-hoc parser for readers to parse it.
- A test failure extends over several lines while in LITF a single line contains everything about a test, passing or not, making it easier to stream it.
- TAP by default has very few defined fields (status, test number and a description) and include a free-form Yaml block but as of version 13 the format has not been standardized.

# LITF vs TAP-Y/J

[TAP-Y and TAP-J](https://github.com/rubyworks/tapout/wiki/TAP-Y-J-Specification) are test streams loosely based on TAP. TAP-Y is based on YAML while TAP-J is based on JSON lines. TAP-J is extremely close to LITF.

[https://github.com/rubyworks/tapout](https://github.com/rubyworks/tapout)

## Pro

## Cons


# LITF vs Mozlog

[Mozlog](https://firefox-source-docs.mozilla.org/mozbase/mozlog.html#data-format) is a lesser-known test output format.

## Pro

TODO: Fill-up

## Cons

- Parsing a Mozlog stream requires to keep a state because one test result generate one `test_start` message and one `test_end`. It's a bit more complex on the reader side.

# LITF vs Subunit

[Subunit](https://github.com/testing-cabal/subunit) is a binary test output format. It already has support for several producing libraries in several languages. The biggest differences are that it's a binary protocol and has a more stream-based design, it's designed to easily merge, filter and transform output streams. Replacing LITF with subunit by adding needed LITF characteristics (input format and extensibility) is currently under consideration.

# Other formats

There is several discussions regarding creating a new test output format which need to be streamable and might be based on JSON in the Junit community:
- https://github.com/ota4j-team/opentest4j/issues/9
- https://github.com/junit-team/junit5/issues/373