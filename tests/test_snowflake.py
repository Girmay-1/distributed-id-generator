import unittest
from snowflake import Snowflake

class TestSnowflake(unittest.TestCase):
    def setUp(self):
        # given 
        self.snowflake = Snowflake(datacenter_id=1, worker_id=1)
        
    def test_id_uniqueness(self):
        ids = set()
        for _ in range(1000):
            #when
            id = self.snowflake.generate_id()
            #then
            self.assertNotIn(id, ids)
            ids.add(id)
            
    def test_id_format(self):
        #when
        id = self.snowflake.generate_id()
        #then
        self.assertLess(id, 1 << 64)
        self.assertGreaterEqual(id, 0)
        
if __name__ == '__main__':
    unittest.main()