from collections import defaultdict
from copy import deepcopy
from itertools import chain, combinations
import numpy as np


input_file = "example_input"
input_file = "input"

input_text = open(input_file).read()

def parse_input(inp):
    scanners = []
    scanner = []
    for line in inp.splitlines():
        if not line.strip():
            scanners.append(scanner)
            scanner = []
        elif '---' not in line:
            scanner.append(np.array(list(map(int, line.split(',')))))
    scanners.append(scanner)
    return scanners

def get_beacon_distances(scanner):
    distances = defaultdict(list)
    for i in range(len(scanner)):
        src = scanner[i]
        for j in range(i + 1, len(scanner)):
            dist = np.linalg.norm(src - scanner[j])
            if dist in distances:
                raise ValueError("Dupe distance", i)
            distances[dist] = (i, j)
    return distances


def get_route_to_zero(offsets, path):
    idx = path[-1]
    if 0 in offsets[idx]:
        return path + [0]
    paths = []
    for next_idx in offsets[idx]:
        if next_idx not in path:
            p = get_route_to_zero(offsets, path + [next_idx])
            if p:
                paths.append(p)
    return sorted(paths)[0] if paths else None

def transform_point(point, offset):
    adjusted = [point[i] for i in offset['idx']]
    adjusted *= offset['sign']
    adjusted -= offset['pos']
    return adjusted

def transform_point_to_scanner_zero(src_scanner_id, point):
    rtz = get_route_to_zero(offsets, [src_scanner_id])
    for curr_id, next_id in zip(rtz[:-1], rtz[1:]):
        point = transform_point_between_scanners(curr_id, next_id, point)
    return point

def transform_point_between_scanners(src_scanner_id, dst_scanner_id, point):
    # offset = offsets_to_zero[src_scanner]
    offset = offsets[src_scanner_id][dst_scanner_id]
    return transform_point(point, offset)


scanners = parse_input(input_text)
beacon_distances_to_ids = [get_beacon_distances(sc) for sc in scanners]

id_maps = {}
for i in range(len(beacon_distances_to_ids)):
    src_ds = beacon_distances_to_ids[i]
    src_id_maps = {}
    for j in range(i + 1, len(beacon_distances_to_ids)):
        dst_ds = beacon_distances_to_ids[j]

        distances = set(src_ds).intersection(dst_ds)

        src_ids = set(chain(*[src_ds[k] for k in distances]))
        dst_ids = set(chain(*[dst_ds[k] for k in distances]))

        id_map = {}
        for dist1, dist2 in combinations(distances, 2):
            common = set(src_ds[dist1]).intersection(src_ds[dist2])
            if common and not common.intersection(id_map):
                common2 = set(dst_ds[dist1]).intersection(dst_ds[dist2])

                id_map[list(common)[0]] = list(common2)[0]

        src_id_maps[j] = id_map
    id_maps[i] = src_id_maps

id_maps_12 = {}
for k, v in id_maps.items():
    id_maps_12[k] = {k2: v2 for k2, v2 in v.items() if len(v2) >= 12}

id_maps_12_full = deepcopy(id_maps_12)
for sca, v in id_maps_12.items():
    for scb, mapping in v.items():
        id_maps_12_full[scb][sca] = dict(ids[::-1] for ids in mapping.items())


# Get offset. There is assuredly a fancy way of doing this. Do it the dumb way
offsets = defaultdict(dict)
for sc1, v in id_maps_12_full.items():
    for sc2, v2 in v.items():
        idx_pairs = list(v2.items())
        sc1_id1, sc2_id1 = idx_pairs[0]
        sc1_id2, sc2_id2 = idx_pairs[1]

        sc1_id1_pos = scanners[sc1][sc1_id1]
        sc1_id2_pos = scanners[sc1][sc1_id2]
        sc2_id1_pos = scanners[sc2][sc2_id1]
        sc2_id2_pos = scanners[sc2][sc2_id2]

        sc1_offset = sc1_id1_pos - sc1_id2_pos
        sc2_offset = sc2_id1_pos - sc2_id2_pos

        sc1_abs = abs(sc1_offset)
        sc2_abs = abs(sc2_offset)

        sc2_idx_mapping = [np.where(sc2_abs == v)[0][0] for v in sc1_abs]
        sc2_offset_remapped = [sc2_offset[i] for i in sc2_idx_mapping]
        sc2_sign_mapping = sc1_offset / sc2_offset_remapped

        sc1_idx_mapping = [np.where(sc1_abs == v)[0][0] for v in sc2_abs]
        sc1_offset_remapped = [sc1_offset[i] for i in sc1_idx_mapping]
        sc1_sign_mapping = sc2_offset / sc1_offset_remapped

        sc2_conv = [sc2_id1_pos[i] for i in sc2_idx_mapping]
        sc2_conv_full = sc2_conv * sc2_sign_mapping
        sc2_pos_offset = sc2_conv_full - sc1_id1_pos
        sc1_pos_offset = sc1_id1_pos - sc2_conv_full

        sc2_offset = {'idx': sc2_idx_mapping, 'sign': sc2_sign_mapping, 'pos': sc2_pos_offset}
        offsets[sc2][sc1] = sc2_offset

        sc1_offset = {'idx': sc1_idx_mapping, 'sign': sc1_sign_mapping, 'pos': sc1_pos_offset}
        # offsets[sc1][sc2] = sc1_offset

        # print(sc2, sc1, sc2_idx_mapping, sc2_sign_mapping, sc2_pos_offset)
        # print(sc1, sc2, sc1_idx_mapping, sc1_sign_mapping, sc1_pos_offset)


all_points = scanners[0].copy()
for scanner_id in range(1, len(scanners)):
    for point in scanners[scanner_id]:
        all_points.append(transform_point_to_scanner_zero(scanner_id, point))

print(len(set(tuple(p) for p in all_points)))
