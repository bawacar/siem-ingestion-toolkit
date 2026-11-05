# Troubleshooting SIEM Log Ingestion

## Problem

A collector service can be healthy while
expected security events remain unavailable
for investigation.

## Diagnostic workflow

| Stage | Question | Evidence |
|---|---|---|
| Source | Was the event generated? | Test event |
| Transport | Did it reach the destination? | Authorised network evidence |
| Collector | Was the event received and forwarded? | Collector diagnostics |
| Parsing | Was the event processed correctly? | Parsing outcome |
| SIEM | Is the event searchable? | Search result |

## Synthetic test event

[2026-11-05 08:00:00] INFO
[demo.auth:42] user=test_user action=login
result=success

## Troubleshooting principles

1. A running collector does not prove
   successful ingestion.
2. Network connectivity does not prove
   successful event processing.
3. Successfully received events may
   still be filtered or incorrectly parsed.
4. End-to-end validation requires locating
   a unique synthetic event in the SIEM.

## Limitations

This is a diagnostic checklist, not a
validated SIEM integration or incident report.

## Security

Use only synthetic examples and authorised
test environments. Never publish real
employer logs, credentials, internal IPs
or confidential infrastructure details.
