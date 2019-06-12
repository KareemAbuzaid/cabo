from cabo import cabo
import unittest

class TestCabo(unittest.TestCase):
	
	def setUp(self):
		self.c = cabo()
		self.c['a'] = 1

	def test_1_add_key_str(self):
		self.assertEqual(self.c['a'], 1)
		print("No issues adding items using str keys")
		
	def test_2_get_by_str_key(self):
		self.assertEqual(self.c['a'], 1)
		print("No issues getting items using str keys")
	
	def test_3_get_by_int_key(self):
		self.assertEqual(self.c[0], ('a', 1))
		print("No issues getting items using int keys")
	
	def test_4_del_cabo_by_str_key(self):
		with self.assertRaises(TypeError):
			del self.c['a']
		print("Delete never happens using str key")
	
	def test_5_del_cabo_by_int_key(self):
		with self.assertRaises(TypeError):
			del self.c[0]
		print("Delete never happens using int key")

if __name__ == '__main__':
	unittest.main()

