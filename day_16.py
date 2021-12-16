from re import sub
from utils import *
from textwrap import wrap
import json


class Packet:
    def __init__(self, bits) -> None:
        self.bits = cat(map(lambda x: bin(int(x, 16))[2:].zfill(4), list(bits.strip())))
        self.pos = 0

    def bits_to_int(self, num_bits):
        val = int(self.bits[self.pos:self.pos+num_bits], 2)
        self.pos += num_bits
        return val

    def decode_packet(self):
        packet_version = self.bits_to_int(3)
        packet_type_id = self.bits_to_int(3)
        data = self.decode_packet_data(packet_type_id)
        return (packet_version, packet_type_id, data)

    def decode_packet_data(self, packet_type_id):
        if packet_type_id == 4:
            return self.decode_packet_literal()
        return self.decode_packet_operator()

    def decode_packet_literal(self):
        number_bits = ''
        while True:
            prefix, *bits = self.bits[self.pos:self.pos+5]
            self.pos += 5
            number_bits += cat(bits)
            if prefix == '0':
                break
        return int(number_bits, 2)

    def decode_packet_operator(self):
        length_type_id = self.bits_to_int(1)

        if length_type_id == 1:
            return self.decode_n_packets(self.bits_to_int(11))

        return self.decode_length_packet(self.bits_to_int(15))

    def decode_n_packets(self, n):
        return [self.decode_packet() for _ in range(n)]

    def decode_length_packet(self, length):
        stop = self.pos + length
        sub_packets = []
        while self.pos < stop:
            sub_packets.append(self.decode_packet())
        return sub_packets


def part_1(p_Input):
    p = Packet(p_Input)
    x = p.decode_packet()

    def versions(packet):
        packet_version, packet_type_id, data = packet
        if packet_type_id == 4:
            return packet_version
        return packet_version + sum(map(versions, data))

    return versions(x)

def part_2(p_Input):
    pass


example_input_1 = 'D2FE28'
example_input_2 = '38006F45291200'
example_input_3 = 'EE00D40C823060'
example_input_4 = '8A004A801A8002F478'
example_input_5 = '620080001611562C8802118E34'
example_input_6 = 'C0015000016115A2E0802F182340'
example_input_7 = 'A0016C880162017C3686B18A3D4780'
challenge_input = Input('16')

assert(part_1(example_input_4) == 16)
assert(part_1(example_input_5) == 12)
assert(part_1(example_input_6) == 23)
assert(part_1(example_input_7) == 31)
print(f"Part 1: {part_1(challenge_input.strip())}")

assert(part_2(example_input_1) == 'None')
print(f"Part 2: {part_2(challenge_input)}")
