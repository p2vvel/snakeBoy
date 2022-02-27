from unittest import TestCase
from memory import Memory

class TestOperators(TestCase):
    def setUp(self) -> None:
        self.memory = Memory()

    def test_memory_write_operator(self):
        """__setitem__ operator should write one byte of data at specified memory address"""
        memory = self.memory

        self.assertEqual(memory.memory[0], 0)   # 0 is initial value
        memory[0] = 0xff    # writing 0 to memory at address 0
        self.assertEqual(memory.memory[0], 0xff)

        memory[0] = 0x997    # testing overflow
        self.assertEqual(memory.memory[0], 0x97)    # higher bites should be cut off

        # assigning non-int value should cause exception raise
        with self.assertRaises(AssertionError):
            memory[0] = "wrong type"

        # assigning non-int value should cause exception raise
        with self.assertRaises(AssertionError):
            memory[0] = 2.15

        # allowing for negative addresses would make code harder to debug
        with self.assertRaises(AssertionError):
            memory[-1] = 12

    def test_memory_read_operator(self):
        """__getitem__ operator should return memory value at given address"""
        memory = self.memory
        self.assertEqual(memory[0], 0)   # 0 is initial value

        memory.memory[0] = 0xff     # writing data at given address
        self.assertEqual(memory[0], 0xff)   # 0 is initial value

        # trying to access unavailable memory should raise an exception
        self.assertRaises(IndexError, lambda: memory[0x10000])
        self.assertRaises(TypeError, lambda: memory["xd"])
        memory.memory[0] = "test"
        self.assertRaises(AssertionError, lambda: memory[0])    # byte should never be a non-string
        self.assertRaises(AssertionError, lambda: memory[-1])   # allowing for negative addresses would make code harder to debug
