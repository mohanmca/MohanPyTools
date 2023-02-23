from collections import defaultdict


def reverse_non_unique_mapping(d):
    dinv = {}
    for k, v in d.items():
        if v in dinv:
            dinv[v].append(k)
        else:
            dinv[v] = [k]
    return dinv

def recon(dict1, dict2) -> dict:
    result = defaultdict(list)
    common_keys = set(dict1.keys()) & set(dict2.keys())
    for key in common_keys:
        if dict1[key] == dict2[key]:
            common = result.get("common_key_value_1", [])
            common.append((key, dict1[key]))
            result['common_kv_1'] = common
        else:
            common = result.get("common_keys_2", [])
            common.append((key, dict1[key], dict2[key]))
            result['common_k_2'] = common
        dict1.pop(key, None)
        dict2.pop(key, None)

    r_dict1 = reverse_non_unique_mapping(dict1)
    r_dict2 = reverse_non_unique_mapping(dict2)
    common_values = set(r_dict1.keys()) & set(r_dict2.keys())
    for value in common_values:
        common_value = result.get("common_values_3", [])
        common_value.append((value, r_dict1[value], r_dict2[value]))
        result['common_values_3'] = common_value
        for k in r_dict1[value]:
            dict1.pop(k, None)
        for k in r_dict2[value]:
            dict2.pop(k, None)
    exclusive = [(k, v) for k, v in dict1.items()]
    result['exclusive_a'] = exclusive
    exclusive = [(k, v) for k, v in dict2.items()]
    result['exclusive_b'] = exclusive
    return result


if __name__ == "__main__":
    in_dict1 = {"a": 1, "b": 2, "c": 3, "d": "9"}
    in_dict2 = {"a": 1, "b": 7, "e": 4, "f": 3, "k": 8, "l": 13}
    result = recon(dict1=in_dict1, dict2=in_dict2)
    for x in result.keys():
        print(x, ':', result[x])
