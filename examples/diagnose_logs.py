
from datetime import datetime

REQUIRED_FIELDS = ("user", "action", "result")
VALID_RESULTS = {"success", "failure"}


def diagnose(event):
    parts = event.split()

    if not parts:
        return "malformed_event"

    try:
        datetime.fromisoformat(
            parts[0].replace("Z", "+00:00")
        )
    except ValueError:
        return "invalid_timestamp"

    fields = {}

    for part in parts[1:]:
        if "=" not in part:
            return "malformed_field"

        key, value = part.split("=", 1)

        if not key:
            return "malformed_field"

        if key in fields:
            return "duplicate_field"

        fields[key] = value

    for field in REQUIRED_FIELDS:
        if not fields.get(field):
            return f"missing_{field}"

    if fields["result"] not in VALID_RESULTS:
        return "invalid_result"

    return "accepted"


if __name__ == "__main__":
    samples = [
        "2026-11-19T08:00:00Z user=alice action=login result=success",
        "2026-11-19T08:01:00Z user=bob action=login",
        "2026-11-19T08:02:00Z user=charlie action=login result=unknown",
        "invalid-date user=david action=login result=failure",
    ]

    for sample in samples:
        print(diagnose(sample))
