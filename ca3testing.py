

import unittest

from ca3 import Commit

class TestCommit(unittest.TestCase): 

    def setUp(self):
        self.commit = Commit()
        self.commit.prepare_data = range (10, 14)
        self.hours =[]
        self.num_commits =422        
        
     
        
if __name__ == '__main__':   
    unittest.main()   
    
    
