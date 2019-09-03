import json
import yaml


def transform(jsonschema, data):
    with open(jsonschema, 'r') as stream:
        schema_loaded = yaml.safe_load(stream)

        result = doTransform(data, schema_loaded['fields'])
        print(json.dumps(result, indent=4, sort_keys=True))


def doTransform(sourcedata, mapping):
    data = {}

    for key in mapping:
        if key == 'nested':
            array_key = next(iter(mapping[key]))
            array = mapping[key][array_key]
            data[array_key] = doTransform(sourcedata[next(iter(array))], array)
        elif type(mapping[key]) is dict:
            data = doTransform(sourcedata, mapping[key])
        else:
            data[key] = sourcedata[mapping[key]]

    return data
