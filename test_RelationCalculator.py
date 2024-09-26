import unittest
from CaculatorClass import Calculator
from RelationsClass import Relation,RelationDefineByInt

class TestMyFunction(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(3)
        self.relation = Relation({'A','B','C'},[('C',6)])
        self.relationDefineByInt = RelationDefineByInt(511,3)

    def test_count_transitive_relations(self):
        self.assertEqual(self.calculator.count_transitive_relations(), 171)

    def test_relation_is_related(self):
        self.relation.add_relation('A','B')
        self.relation.add_relation('A','C')
        self.relation.add_relation('B','C')
        self.assertEqual(self.relation.is_related('A','C'), True)

    def test_relation_define_by_int_get_all_elements(self):
        self.assertEqual(self.relationDefineByInt.get_all_elements(), [1,2,3])

if __name__ == '__main__':
    unittest.main()
