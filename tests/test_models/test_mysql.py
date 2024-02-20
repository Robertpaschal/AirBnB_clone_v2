import unittest
import MySQLdb
import sys

class TestMySQLScripts(unittest.TestCase):
    def setUp(self):
        self.connection = MySQLdb.connect(
            host="127.0.0.0.1",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_create_state_command(self):
        initial_count = self.get_states_count()
        final_count = self.get_states_count()
        self.assertEqual(final_count, initial_count + 1, "New state record was not added")

    def get_states_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM states")
        result = self.cursor.fecthone()
        return result[0]
    
    if __name__ == '__main__':
        unittest.main()