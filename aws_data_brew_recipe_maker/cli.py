import argparse
import json


def main():
    opts = get_options()
    print(f'start make Data Brew recipe from JSON. opts: {opts}')
    with open(opts.input_json) as f:
        in_json = json.load(f)

    output = []
    for key, _ in in_json.items():
        dic = {
            'Action': {
                'Operation': 'EXTRACT_VALUE',
                'Parameters': {
                    'path': key,
                    'sourceColumn': opts.output_column_prefix,
                    'targetColumn': f'{opts.output_column_prefix}_{key}'
                }
            }
        }
        output.append(dic)

    out_json = f'{opts.output_column_prefix}_recipe.json'
    with open(out_json, 'w') as f:
        json.dump(output, f, indent=4)

    print(f'finish make Data Brew recipe from JSON. output: {out_json}')


def get_options():
    parser = argparse.ArgumentParser(description='Make Data Brew recipe from JSON.')
    parser.add_argument('--input_json', help='Input JSON file path')
    parser.add_argument('--output_column_prefix', help='Input JSON file path')
    return parser.parse_args()
