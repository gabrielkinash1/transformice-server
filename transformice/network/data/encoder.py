from transformice.packet.outgoing.__init__ import Outgoing
from transformice.network.data import Buffer
class Encoder:
    @staticmethod
    def encode(data):
        if type(data) == str:
            return data.encode()

        elif type(data) == bytes:
            return data

        else:
            out_tokens = data.tokens
            out_buffer = data.buffer

            buffer = Buffer()
            length = out_buffer.length() + 2

            if length <= 0xFF:
                buffer.writeByte(1)
                buffer.writeByte(length)

            elif length <= 0xFFFF:
                buffer.writeByte(2)
                buffer.writeShort(length)

            elif length <= 0xFFFFFF:
                buffer.writeByte(3)
                buffer.writeInt24(length)

            buffer.writeByte(out_tokens[0])
            buffer.writeByte(out_tokens[1])

            out_data = out_buffer.toByteArray()
            data.buffer.clear()

            buffer.writeBytes(out_data)
            return buffer.toByteArray()