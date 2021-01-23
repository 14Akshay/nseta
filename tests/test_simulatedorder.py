# -*- coding: utf-8 -*-
import pdb
import unittest

from nseta.strategy.simulatedorder import simulatedorder, OrderType, INITIAL_FUNDS
from nseta.common import urls
from baseUnitTest import baseUnitTest

class TestSimulatedOrder(baseUnitTest):
	def setUp(self):
		super().setUp()

	def test_buy_sell_MIS(self):
		price = 500
		s = simulatedorder(order_type=OrderType.MIS)
		self.assertEqual(s.margin, 0.2)
		self.assertEqual(s.funds, INITIAL_FUNDS)
		self.assertEqual(s.holdings_size, 0)
		self.assertEqual(s.order_type, OrderType.MIS)
		s.sell(price)
		self.assertEqual(s.order_size, int(INITIAL_FUNDS/(price*s.margin)))
		self.assertEqual(s.holdings_size, 0 - int(INITIAL_FUNDS/(price*s.margin)))
		self.assertEqual(s.funds, 0)
		holdings_size = s.holdings_size
		s.square_off(2*price)
		self.assertEqual(s.order_size, holdings_size)
		self.assertEqual(s.holdings_size, 0)
		self.assertEqual(s.funds, 2*INITIAL_FUNDS)

	def tearDown(self):
		super().tearDown()

if __name__ == '__main__':

	suite = unittest.TestLoader().loadTestsFromTestCase(TestSimulatedOrder)
	result = unittest.TextTestRunner(verbosity=2).run(suite)
	if six.PY2:
		if result.wasSuccessful():
			print("tests OK")
		for (test, error) in result.errors:
			print("=========Error in: %s===========" % test)
			print(error)
			print("======================================")

		for (test, failures) in result.failures:
			print("=========Error in: %s===========" % test)
			print(failures)
			print("======================================")
