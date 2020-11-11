"""Regex primitives."""

import re


ANYTHING = r".+"
WHITESPACE = r"\s"
WHITESPACES = r"{0}+".format(WHITESPACE)
NON_WHITESPACE = r"\S"
NON_WHITESPACES = r"{0}+".format(NON_WHITESPACE)
DIGIT = r"\d"
NUMBER = r"{0}+".format(DIGIT)
FLOAT = r"{0}.{0}".format(NUMBER)
START_OF_STRING = r"^"
END_OF_STRING = r"$"


def make_matcher(pattern):
  return re.compile(pattern, re.VERBOSE).match


def group(expression):
  return "({0})".format(expression)


def named_group(group_name, expression):
  return "(?P<{0}>{1})".format(group_name, expression)


def choices(values, delimiter="|"):
  return delimiter.join(values)
