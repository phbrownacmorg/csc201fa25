import unittest
# import the code you want to test here
from idmaker import make_id

class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test

    # Simple case (one middle name, no funny characters)
    def test_phbrown(self) -> None:
        self.assertEqual('PHBrown001', make_id({'lastname': 'Brown', 
                                                'firstname': 'Peter H.'}))
        
    # No middle name
    def test_lfeitzinger(self) -> None:
        self.assertEqual('LFeitzinger001', make_id({'lastname': 'Feitzinger', 
                                                    'firstname': 'Laura'}))
        
    # Lots of middle names
    def test_wawindsorwa(self) -> None:
        self.assertEqual('WAWindsor001', make_id({'lastname': 'Windsor', 
                                                  'firstname': 'William Arthur Philip Louis'}))
        
    # Space in the last name
    def test_visanchezcazares(self) -> None:
        self.assertEqual('VISanchezCazares001', make_id({'lastname': 'Sanchez Cazares', 
                                                        'firstname': 'Vanessa Itzel'}))
        
    # Hyphen in last name
    def test_jgrantponce001(self) -> None:
        self.assertEqual('JGrant-Ponce001', make_id({'lastname': 'Grant-Ponce',
                                                    'firstname': 'Jamie'}))
        
    # Apostrophe in last name
    def test_bbobrian001(self) -> None:
        self.assertEqual('BBOBrian001', make_id({'lastname': "O'Brian",
                                                'firstname': 'Brian B.'}))
        
    # Last name not capitalized
    def test_mavonrichthofen001(self) -> None:
        self.assertEqual('MAvonRichthofen001', make_id({'lastname': 'von Richthofen',
                                                        'firstname': 'Manfred Albrecht'}))

if __name__ == '__main__':
    unittest.main()

