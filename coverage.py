#@author Adrien Bournat shirokai@protonmail.com
#@category Pooxy

from ghidra.app.plugin.core.colorizer import ColorizingService
from java.awt import Color
from ghidra.program.model.address import Address

import struct

file1 = askFile("FILE", "Choose file:")

offset = askInt("Offset", "Do you want to add an offset ?")

f = open(str(file1), "r")
data = f.read()
data_len = len(data)

service = state.getTool().getService(ColorizingService)

i = 0
while (i < data_len):
    addr = struct.unpack("<Q", data[i:i + 8])[0]
    size = struct.unpack("<h", data[i + 8:i + 10])[0]
    address = currentProgram.getAddressFactory().getAddress('0x{:02x}'.format(addr + offset))
    print(address, size)
    service.setBackgroundColor(address, address.add(size), Color.GRAY)
    i += 10