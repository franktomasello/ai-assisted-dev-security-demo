import unittest
from contextlib import contextmanager
from types import ModuleType
from unittest.mock import MagicMock, patch
from urllib.parse import parse_qs, urlparse


class _FakeRequest:
    args = {}


class _FakeFlask:
    def __init__(self, name):
        self.name = name

    def route(self, _path):
        def decorator(func):
            return func
        return decorator

    @contextmanager
    def test_request_context(self, path):
        parsed = urlparse(path)
        original_args = _FakeRequest.args
        _FakeRequest.args = {
            key: values[-1] for key, values in parse_qs(parsed.query).items()
        }
        try:
            yield
        finally:
            _FakeRequest.args = original_args


fake_flask = ModuleType("flask")
fake_flask.Flask = _FakeFlask
fake_flask.request = _FakeRequest

with patch.dict("sys.modules", {"flask": fake_flask}):
    import user_lookup


class UserLookupTestCase(unittest.TestCase):
    def test_get_user_uses_parameterized_query(self):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ("alice",)

        with patch.object(user_lookup.sqlite3, "connect", return_value=mock_conn):
            with user_lookup.app.test_request_context("/user?username=alice' OR '1'='1"):
                response = user_lookup.get_user()

        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM users WHERE username = ?",
            ("alice' OR '1'='1",),
        )
        self.assertEqual(response, "('alice',)")


if __name__ == "__main__":
    unittest.main()
