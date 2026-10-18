# ADR-001: No I/O in the inventory package

- Status: Accepted

## Context

`inventory` is a library embedded in other programs. Those programs decide where and how data is
stored.

## Decision

The package performs no file or network I/O. It keeps state in memory only. Persistence belongs
to callers: the package may offer pure conversions to and from strings, never reads or writes
files itself.

## Consequences

Changing this requires a new ADR agreed by the maintainers; code must not contradict it.
