# -*- coding: utf-8 -*-

import unittest

from il2fb.commons.spatial import Point2D, Point3D


class Point2DTestCase(unittest.TestCase):

    def test_repr(self):
        testee = repr(Point2D(x=1, y=2))
        self.assertEqual(testee, "<Point2D '1.0;2.0'>")


class Point3DTestCase(unittest.TestCase):

    def test_repr(self):
        testee = repr(Point3D(x=1, y=2, z=3))
        self.assertEqual(testee, "<Point3D '1.0;2.0;3.0'>")
