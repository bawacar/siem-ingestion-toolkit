# siem-ingestion-toolkit
Practical troubleshooting guides and reusable resources for SIEM log ingestion and detection engineering even when a collector service is running.

Problem
A healthy collector process does not prove that log sources can reach it, that messages are accepted, that parsing succeeds, or that events become searchable.
Architecture
Synthetic log source -> network -> collector listener -> parser -> SIEM search
Troubleshooting checklist
1. Source: Confirm the source is configured to emit the intended events to the correct destination, port, and transport protocol.
2. Collector health: On an authorised Linux test host, check sudo systemctl status humio-log-collector (service name may differ).
3. Listener: Run sudo ss -tulnp | grep ':1514'. Confirm whether TCP, UDP, or both are actually bound.
4. Network: On the collector host, run sudo tcpdump -ni any 'port 1514' while sending a synthetic test event from an authorised lab source. Packet arrival does not establish application-level acceptance.
5. Collector logs: Run sudo journalctl -u humio-log-collector -n 50 --no-pager and inspect errors without publishing secrets.
6. Parsing: Check the selected parser and whether the test event was rejected, filtered, or transformed.
7. SIEM search: Search for a unique synthetic test marker within the appropriate time window, repository and timezone.
8. Document outcome: Record which stages passed, failed, or remain unverified.
Example synthetic log
2026-10-29T09:00:00Z lab-host demo-app[1234]: INFO test_marker=LAB-INGEST-001 message="Synthetic ingestion validation event"

This is a demonstration event, not an employer log.
Diagnostic table
Symptom	Possible explanation	Validation
Service active, no traffic	Wrong destination, routing or firewall issue	Confirm source settings and packet arrival
Traffic arrives, no event	Collector input mismatch or rejection	Inspect collector logs and input configuration
Event rejected or filtered	Parser or filter mismatch	Test with synthetic examples and inspect parser outcomes
Event accepted, search empty	Repository, query, timestamp or indexing issue	Check ingestion status and search scope


Safety and scope
Use only systems and traffic you own or are authorised to test. Do not upload internal logs, customer information, credentials, infrastructure addresses, or employer-specific configurations. Sanitise screenshots and use synthetic examples.
Project roadmap
- [ ] Reproduce one failure in a controlled lab
- [ ] Capture redacted command outputs and diagnostic notes
- [ ] Add a simple source-to-SIEM architecture diagram
- [ ] Publish a walkthrough with verified results
- [ ] Invite peer feedback and track issues or improvements
Evidence of impact
Record independently verifiable contributions such as accepted pull requests, external issue reports, community reuse and workshop invitations. Stars and impressions alone are not evidence of technical impact.
License
Choose and add an open-source license before inviting reuse or contributions.
