class Memory:
    def __init__(self):
        self.memory = [0] * 0x10000

    def __getitem__(self, address: int) -> int:
        """Get memory byte value at 'item' address'"""
        # check if address is integer
        assert isinstance(address, int), f"Wrong memory address type: {type(address)}"
        # check if address in range <0, 0xffff>
        assert 0 <= address <= 0xffff, f"Memory address out of bounds: {hex(address)}"
        # check if data at specified memory address is integer
        assert isinstance(self.memory[address], int), f"Wrong byte type: {type(self.memory[address])} [{self.memory[address]}]"
        # check if data is stores proper byte value (in range <0, 255>)
        assert 0 <= self.memory[address] <= 0xff, f"Incorrect byte value: {self.memory[address]}"

        return self.memory[address]

    def __setitem__(self, address: int, value: int) -> None:
        """Set 'value' byte at memory address 'key'"""
        # check if address is integer
        assert isinstance(address, int), f"Incorrect address type: {type(address)} [{address}]"
        # check if address is in proper range
        assert 0 <= address <= 0xffff, f"Wrong address: {hex(address)}"    # only integer values will be assigned to bytes
        # check if new value is integer
        assert isinstance(value, int), f"Incorrect data type: {type(value)} [{value}]"

        self.memory[address] = value & 0xff
