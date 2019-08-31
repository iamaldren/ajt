import json
import yaml


def main():
    with open("./schema/schema1.yml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)

        source = {
            'pangalan': 'Aldren',
            'apelyido': 'Bobiles',
            'trabaho': {
                'posisyon': 'Developer',
                'industriya': 'IT',
                'kakayahan': {
                    'lengwahe': 'Python'
                }
            }
        }
        result = transform(source, data_loaded['fields'])
        print(json.dumps(result, indent=4, sort_keys=True))


def transform(source, mapping):
    data = {}

    for key in mapping:
        if key == 'nested':
            array_key = next(iter(mapping[key]))
            array = mapping[key][array_key]
            data[array_key] = transform(source[next(iter(array))], array)
        else:
            if type(mapping[key]) is dict:
                data = transform(source, mapping[key])
            else:
                data[key] = source[mapping[key]]

    return data


if __name__ == "__main__":
    main()
