
import re

# Synthetic authentication logs
logs = [
    "2026-11-11T08:00:00Z user=alice action=login result=success",
    "2026-11-11T08:01:00Z user=bob action=login result=failure",
    "2026-11-11T08:02:00Z user=charlie action=login",
    "malformed event without expected fields"
]

# Expected event structure
pattern = re.compile(
    r"^(?P<timestamp>\S+) "
    r"user=(?P<user>\w+) "
    r"action=(?P<action>\w+) "
    r"result=(?P<result>success|failure)$"
)

accepted = []
rejected = []

for event in logs:
    match = pattern.fullmatch(event)

    if match:
        accepted.append(match.groupdict())
    else:
        rejected.append(event)

print("Accepted:", len(accepted))
print("Rejected:", len(rejected))

for event in rejected:
    print("Rejected event:", event)
