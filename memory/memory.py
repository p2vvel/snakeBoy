class Memory:
    def __init__(self):
        self.memory = [0] * 0x10000

    def __getitem__(self, item):
        """Get memory byte value at 'item' address'"""
        try:
            # byte value should be an integer in range <0, 255>
            assert isinstance(self.memory[item], int), f"Incorrect byte type: {type(self.memory[item])} [{self.memory[item]}]"
            assert 0 <= self.memory[item] <= 0xff, f"Incorrect byte value: {self.memory[item]}"
            assert item >= 0, f"Negative byte index value: {item}"    # only integer values will be assigned to bytes

            return self.memory[item]
        except (IndexError, TypeError):
            print(f"Trying to access memory at wrong address: {item}")
            raise       # passing exception on

    def __setitem__(self, key, value):
        """Set 'value' byte at memory address 'key'"""
        try:
            assert isinstance(value, int), f"Incorrect byte type: {type(value)} [{value}]"    # only integer values will be assigned to bytes
            assert key >= 0, f"Negative byte index value: {key}"    # only integer values will be assigned to bytes

            self.memory[key] = value & 0xff
        except (IndexError, TypeError):
            print(f"Trying to access memory at wrong address: {key}")
            raise       # passing exception on
