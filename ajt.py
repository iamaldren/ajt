import json
import yaml

from jsonbender import bend, S


def main():
    with open("./schema/schema1.yml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)

        mapping = {}
        for key in data_loaded['fields']:
            mapping[key] = S(data_loaded['fields'][key])

        source = {'pangalan': 'Aldren', 'apelyido': 'Bobiles'}
        result = bend(mapping, source)
        print(json.dumps(result, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
