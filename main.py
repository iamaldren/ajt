import os
import ajt

if __name__ == "__main__":
    path = "./schema/"

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

    for r, d, f in os.walk(path):
        for schema in f:
            if '.yml' in schema:
                ajt.transform(os.path.join(r, schema), source)
