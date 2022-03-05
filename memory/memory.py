class Memory:
    """
    Implements RAM

    In theory, I should implement mirroring at addresses E000-FDFF and memory at FEA0-FEFF should not be accessible BUT
    Nintendo says use of this area is prohibited, so I will just leave it as it is

    sources: https://gbdev.io/pandocs/Memory_Map.html
    """
    def __init__(self):
        self.memory = [0] * 0x10000

    def __getitem__(self, address: int) -> int:
        """Get specified memory value"""
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
        """Set value byte at specified memory address"""
        # check if address is integer
        assert isinstance(address, int), f"Incorrect address type: {type(address)} [{address}]"
        # check if address is in proper range
        assert 0 <= address <= 0xffff, f"Wrong address: {hex(address)}"
        # check if new value is integer
        assert isinstance(value, int), f"Incorrect data type: {type(value)} [{value}]"

        self.memory[address] = value & 0xff

    # TODO: test functions below:
    def read_8(self, address: int) -> int:
        """Get 1 byte of data at specified address"""
        return self[address]    # no need to check conditions, everything is implemented in __getitem__

    def write_8(self, address: int, value: int) -> None:
        """Write 1 byte of data to specified address of memory"""
        self[address] = value   # no need to check conditions, everything is implemented in __setitem__

    def read_16(self, address: int) -> int:
        """Get 2 bytes of data at specified address"""
        # no need to check anything here, if there is something wrong, __getitem__ will assert exception
        # GB CPU is little endian, so less significant bytes go first
        return (self[address + 1] << 8) | self[address]

    def write_16(self, address: int, value: int) -> None:
        """Write 2 bytes of data to specified address of memory"""
        # only have to check here, if value is an integer, other things will be handled in __setitem__
        # GB CPU is little endian, so less significant bytes go first
        self[address] = value & 0xff
        self[address + 1] = (value & 0xff00) >> 8

