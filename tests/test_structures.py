# -*- coding: utf-8 -*-

import datetime
import unittest

from candv import SimpleConstant, Constants

from il2fb.commons.structures import BaseStructure


class BaseStructureTestCase(unittest.TestCase):

    class Foo(BaseStructure):
        __slots__ = ['a', 'b', 'c', ]

        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    def test_creation(self):
        foo = BaseStructureTestCase.Foo(1, 2, 3)
        self.assertEqual(foo.a, 1)
        self.assertEqual(foo.b, 2)
        self.assertEqual(foo.c, 3)

    def test_equals(self):
        foo = BaseStructureTestCase.Foo(1, 2, 3)
        bar = BaseStructureTestCase.Foo(1, 2, 3)

        self.assertNotEqual(id(foo), id(bar))
        self.assertEqual(foo, bar)

    def test_not_equals(self):
        self.assertNotEqual(
            BaseStructureTestCase.Foo(1, 2, 3),
            BaseStructureTestCase.Foo(4, 5, 6))

        self.assertNotEqual(
            BaseStructureTestCase.Foo(1, 2, 3),
            int(123))

    def test_hash(self):
        foo = BaseStructureTestCase.Foo(1, 2, 3)

        self.assertEqual(hash(foo), hash((1, 2, 3)))

        bar = BaseStructureTestCase.Foo(1, 2, 3)
        d = {foo: 123}

        self.assertEqual(d[bar], 123)

    def test_to_primitive(self):

        class types(Constants):
            primary = SimpleConstant()
            secondary = SimpleConstant()

        foo = BaseStructureTestCase.Foo(
            1,
            types.primary,
            datetime.datetime(2016, 1, 1))

        expected = {
            'a': 1,
            'b': {'name': 'primary'},
            'c': "2016-01-01T00:00:00",
        }

        self.assertEqual(foo.to_primitive(), expected)
