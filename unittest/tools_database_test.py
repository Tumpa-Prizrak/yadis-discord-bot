import unittest
from src.database.tools import DatabaseConnection
from src.database.enums import DBFormat

class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        open("src\\database\\test.db", "w").close()

    def test_is_open(self):
        obj = DatabaseConnection()
        obj.open()
        self.assertTrue(obj._is_opened())
    
    def test_is_closed(self):
        obj = DatabaseConnection()
        self.assertTrue(obj._is_closed())

        obj.open()
        obj.close()

        self.assertTrue(obj._is_closed())
    
    def test_context_manager(self):
        with DatabaseConnection() as db:
            db._is_opened()
        db._is_closed()
    
    def test_write(self):
        obj = DatabaseConnection("test.db")
        obj.open()
        
        self.assertTrue(obj.write(
            """CREATE TABLE test (
                rowid               PRIMARY KEY,
                smth STRING,
                money       INTEGER
                );
            """, raise_errors=True
        ))
        self.assertTrue(obj.write("INSERT INTO test (smth, money) VALUES (?, ?)", "Me", 999, raise_errors=True))

        self.assertFalse(obj.write("SOMETHINGS THAT SHOUDN'T WORK 34%$478359435*$^Y%)635968746"))

        obj.close()
        del obj
    
    def test_read(self):
        obj = DatabaseConnection("test.db")
        obj.open()

        obj.write(
            """CREATE TABLE test (
                smth STRING,
                money       INTEGER
                );
            """, raise_errors=True
        )
        obj.write("INSERT INTO test (smth, money) VALUES (?, ?)", "Me", 999, raise_errors=True)



        self.assertEqual(obj.read("SELECT * FROM test", mode=DBFormat.One), ("Me", 999))
        self.assertEqual(obj.read("SELECT * FROM test", mode=DBFormat.List), [("Me", 999)])
        self.assertEqual(obj.read("SELECT * FROM test", mode=DBFormat.Raw), [("Me", 999)])

        obj.close()
        del obj


if __name__ == "__main__":
    unittest.main()
