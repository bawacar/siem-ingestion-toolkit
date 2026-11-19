
import unittest

from examples.diagnose_logs import diagnose


class TestLogDiagnostics(unittest.TestCase):

    def test_valid_event(self):
        event = (
            "2026-11-19T08:00:00Z "
            "user=alice action=login result=success"
        )
        self.assertEqual(diagnose(event), "accepted")

    def test_missing_result(self):
        event = (
            "2026-11-19T08:01:00Z "
            "user=bob action=login"
        )
        self.assertEqual(
            diagnose(event), "missing_result"
        )

    def test_invalid_result(self):
        event = (
            "2026-11-19T08:02:00Z "
            "user=charlie action=login result=unknown"
        )
        self.assertEqual(
            diagnose(event), "invalid_result"
        )

    def test_invalid_timestamp(self):
        event = (
            "invalid-date "
            "user=david action=login result=failure"
        )
        self.assertEqual(
            diagnose(event), "invalid_timestamp"
        )

    def test_duplicate_field(self):
        event = (
            "2026-11-19T08:03:00Z "
            "user=alice user=bob "
            "action=login result=failure"
        )
        self.assertEqual(
            diagnose(event), "duplicate_field"
        )

    def test_missing_user(self):
        event = (
            "2026-11-19T08:04:00Z "
            "action=login result=failure"
        )
        self.assertEqual(
            diagnose(event), "missing_user"
        )


if __name__ == "__main__":
    unittest.main()
