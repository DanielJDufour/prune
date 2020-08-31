from unittest import TestCase
import json
from prune import prune

class SimpleCases(TestCase):

    def test_simple_tree_with_single_key(self):
        tree = { "a":  1 }
        prune(tree, ["a"])
        self.assertEquals(json.dumps(tree), "{}")

    def test_simple_tree_with_two_keys(self):
        tree = { "a":  1, "b": 2 }
        prune(tree, ["a"])
        self.assertEquals(json.dumps(tree), '{"b": 2}')

class AdvancedCases(TestCase):

    def test_simple_tree_with_nested_key(self):
        tree = { "a":  1, "b": { "c": "d" } }
        prune(tree, ["b.c"])
        self.assertEquals(json.dumps(tree), '{"a": 1, "b": {}}')

    def test_simple_tree_with_single_key(self):
        tree = { "a":  1, "b": { "c": "d", "e": "f" } }
        prune(tree, ["b.c"])
        self.assertEquals(json.dumps(tree), '{"a": 1, "b": {"e": "f"}}')
