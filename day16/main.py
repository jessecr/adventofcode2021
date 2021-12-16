from collections import namedtuple
from math import prod

input_file = "input"
inp = open(input_file).read()

Packet = namedtuple("Packet", ["version", "type_id", "sub_packets", "value"])


def get_bits_from_hex(hex_value):
    return bin(int(hex_value, 16))[2:].zfill(len(hex_value) * 4)


def parse_hex_packet(h):
    return parse_packet(get_bits_from_hex(h))


def parse_packet(bits, i=0):
    version = int(bits[i : i + 3], 2)
    type_id = int(bits[i + 3 : i + 6], 2)

    i += 6

    if type_id == 4:
        value, i = parse_literal_packet(bits, i)
        return Packet(version, type_id, [], value), i
    else:
        sub_packets, i = parse_operator_packet(bits, i)
        return Packet(version, type_id, sub_packets, None), i


def parse_operator_packet(bits, i):
    subpackets = []
    if bits[i] == "0":
        sub_len = int(bits[i + 1 : i + 16], 2)
        i += 16
        sub_end = i + sub_len
        while i < sub_end:
            subpacket, i = parse_packet(bits, i)
            subpackets.append(subpacket)
    else:
        sub_packet_count = int(bits[i + 1 : i + 12], 2)
        i += 12
        for _ in range(sub_packet_count):
            subpacket, i = parse_packet(bits, i)
            subpackets.append(subpacket)

    return subpackets, i


def parse_literal_packet(bits, i):
    literal_bits = ""
    while True:
        i += 5
        literal_bits += bits[i - 4 : i]
        if bits[i - 5] == "0":
            break

    return int(literal_bits, 2), i


def calculate_packet(packet):
    sp_values = [calculate_packet(sp) for sp in packet.sub_packets]
    if packet.type_id == 0:
        return sum(sp_values)
    elif packet.type_id == 1:
        return prod(sp_values)
    elif packet.type_id == 2:
        return min(sp_values)
    elif packet.type_id == 3:
        return max(sp_values)
    elif packet.type_id == 4:
        return packet.value
    elif packet.type_id == 5:
        return 1 if sp_values[0] > sp_values[1] else 0
    elif packet.type_id == 6:
        return 1 if sp_values[0] < sp_values[1] else 0
    elif packet.type_id == 7:
        return int(sp_values[0] == sp_values[1])


def get_packet_verion_total(packet):
    return packet.version + sum(map(get_packet_verion_total, packet.sub_packets))


packet, i = parse_hex_packet(inp)

print("Part 1:", get_packet_verion_total(packet))
print("Part 2:", calculate_packet(packet))
