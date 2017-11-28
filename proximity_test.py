import unittest
import numpy as np
from proximity import CoorCentroidQuery

class TestCoorCentroidQuery(unittest.TestCase):

	def setUp(self):

		self.centroids = np.array([[1,1],[2, 3]])
		self.coors = np.array([[4,5],[-4, -11]])

	def test_get_num_coors(self):
		ccq = CoorCentroidQuery(self.coors, self.centroids)
		self.assertEqual(ccq.get_num_coors(5), 1)
		self.assertEqual(ccq.get_num_coors(10), 1)
		self.assertEqual(ccq.get_num_coors(15), 2)
		self.assertRaises(ValueError, ccq.get_num_coors,-2)
	
	def test_get_min_radius(self):
		ccq = CoorCentroidQuery(self.coors, self.centroids)
		self.assertEqual(ccq.get_min_radius(0),0.0)
		self.assertAlmostEqual(ccq.get_min_radius(50), 2.82842712)
		self.assertEqual(ccq.get_min_radius(100), 13.0)
		self.assertRaises(ValueError, ccq.get_min_radius, 101)

	def test_get_max_radius(self):
		ccq = CoorCentroidQuery(self.coors, self.centroids)
		self.assertEqual(ccq.get_max_radius(2), float('inf'))
		self.assertAlmostEqual(ccq.get_max_radius(1), 12.999999900000001)
		self.assertRaises(ValueError, ccq.get_max_radius, 3)


if __name__ == '__main__':
	unittest.main()