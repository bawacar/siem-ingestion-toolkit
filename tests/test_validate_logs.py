
import unittest

from examples.validate_logs import validate


class TestLogValidation(unittest.TestCase):

    def test_valid_success(self):
        event = (
            "2026-11-18T08:00:00Z "
            "user=alice action=login result=success"
        )
        result = validate(event)
        self.assertIsNotNone(result)
        self.assertEqual(result["user"], "alice")
        self.assertEqual(result["result"], "success")

    def test_valid_failure(self):
        event = (
            "2026-11-18T08:01:00Z "
            "user=bob action=login result=failure"
        )
        result = validate(event)
        self.assertIsNotNone(result)
        self.assertEqual(result["result"], "failure")

    def test_missing_result(self):
        event = (
            "2026-11-18T08:02:00Z "
            "user=charlie action=login"
        )
        self.assertIsNone(validate(event))

    def test_unknown_result(self):
        event = (
            "2026-11-18T08:03:00Z "
            "user=david action=login result=unknown"
        )
        self.assertIsNone(validate(event))


if __name__ == "__main__":
    unittest.main()
