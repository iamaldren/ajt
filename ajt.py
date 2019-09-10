import json
import yaml

count = 0


def transform(jsonschema, data):
    with open(jsonschema, 'r') as stream:
        schema_loaded = yaml.safe_load(stream)

        result = shift(data, schema_loaded['shift'])
        print(json.dumps(result, indent=4, sort_keys=True))


def shift(sourcedata, mapping):
    data = {}
    subdata = {}

    global count
    count += 1
    print("count is ", count)

    for key in mapping:
        if type(mapping[key]) is dict:
            data = shift(sourcedata[key], mapping[key])
        elif ":" in mapping[key]:
            pair = mapping[key].split(":")
            parent = pair[0]
            child = pair[1]
            subdata[child] = sourcedata[key]
            data[parent] = subdata
        else:
            data[mapping[key]] = sourcedata[key]

    return data
