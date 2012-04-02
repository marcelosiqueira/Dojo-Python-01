#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Teste do Programa

import unittest
from dojo import Dojo

class DojoTest(unittest.TestCase):
    def test_create_Dojo(self):
        self.assertNotEqual(Dojo(), None)
        
    def test_saque_zero(self):
	dojo = Dojo()
	self.assertEqual(len(dojo.saque(0)), 0)
      
    def test_saque_100(self):
	dojo = Dojo()
	self.assertEqual(len(dojo.saque(100)), 1)
	self.assertEqual(dojo.saque(100), {100:1})

    def test_saque_40(self):
	dojo = Dojo()
	self.assertEqual(dojo.saque(40), {20:2})
	
    def test_saque_70(self):
	dojo = Dojo()
	self.assertEqual(dojo.saque(70), {50:1,20:1})
	
    def test_saque_105(self):
	dojo = Dojo()
	self.assertEqual(dojo.saque(105),{})
	
    def test_saque_2(self):
	self.assertEqual(Dojo().saque(2),{})

    	
if __name__ == '__main__':
    unittest.main()
