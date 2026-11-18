
import re

PATTERN = re.compile(
    r"^(?P<timestamp>\S+) "
    r"user=(?P<user>\w+) "
    r"action=(?P<action>\w+) "
    r"result=(?P<result>success|failure)$"
)


def validate(event):
    """Return parsed fields or None if invalid."""
    match = PATTERN.fullmatch(event)
    return match.groupdict() if match else None


if __name__ == "__main__":
    logs = [
        "2026-11-18T08:00:00Z user=alice action=login result=success",
        "2026-11-18T08:01:00Z user=bob action=login result=failure",
        "2026-11-18T08:02:00Z user=charlie action=login",
        "malformed event without expected fields",
    ]

    accepted = []
    rejected = []

    for event in logs:
        parsed = validate(event)

        if parsed:
            accepted.append(parsed)
        else:
            rejected.append(event)

    print("Accepted:", len(accepted))
    print("Rejected:", len(rejected))

    for event in rejected:
        print("Rejected event:", event)
