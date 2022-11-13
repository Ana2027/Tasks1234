import json
import sys


def rec(lst_vals: list[dict], lst_tst: list[dict]):
    for it in lst_tst:
        if it.get('values') is None:
            for item in lst_vals:
                if item['id'] == it['id']:
                    it['value'] = item['value']

        elif isinstance(it.get('values'), list):
            for item in lst_vals:
                if item['id'] == it['id']:
                    it['value'] = item['value']
            rec(lst_vals, it['values'])


def parse_json(tests_file, values_file):
    with open(tests_file, 'r') as js_tests, open(values_file, 'r') as js_vals, open('report.json', 'w') as o_file:
        inp_tests = json.load(js_tests)['tests']
        inp_vals = json.load(js_vals)['values']
        rec(inp_vals, inp_tests)
        report = inp_tests
        json.dump(report, o_file, indent=1)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        parse_json(sys.argv[1], sys.argv[2])
    else:
        sys.exit(1)
