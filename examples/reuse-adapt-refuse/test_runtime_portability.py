"""A targeted build-compatibility regression using real in-memory SQLite."""
import sqlite3
import unittest
from unittest.mock import patch
import runtime

class WithoutExtensionAPI(sqlite3.Connection):
    def __getattribute__(self, name):
        if name == 'enable_load_extension':
            raise AttributeError(name)
        return super().__getattribute__(name)

class RuntimePortability(unittest.TestCase):
    def test_optional_extension_api_absent(self):
        con = sqlite3.connect(':memory:', factory=WithoutExtensionAPI)
        try:
            self.assertFalse(hasattr(con, 'enable_load_extension'))
            with patch.object(runtime.sqlite3, 'connect', return_value=con) as connect:
                engine = runtime.Engine([{'value': 10}, {'value': 20}])
                connect.assert_called_once_with(':memory:')
                result = engine.query('SELECT SUM(value) AS total FROM observations', {})
                self.assertEqual(result['rows'], [{'total': 30}])
                self.assertEqual(runtime.Engine.authorize(
                    sqlite3.SQLITE_FUNCTION, None, 'load_extension', 'main', None), sqlite3.SQLITE_DENY)
                with self.assertRaises(sqlite3.DatabaseError):
                    engine.query("SELECT load_extension(:path)", {'path': 'not-a-real-extension'})
        finally:
            con.close()

if __name__ == '__main__': unittest.main()
