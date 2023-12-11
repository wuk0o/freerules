#!/usr/bin/env python3

import yaml
import os
import sys


OUTPUT_PATH = os.path.abspath('./rules/custom.yaml')


if __name__ == '__main__':
    for fname in [sys.argv[1], OUTPUT_PATH]:
        if not os.path.isfile(fname):
            print('%s not found!' % fname)

    rules = []
    with open(sys.argv[1], 'r') as fp:
        data = yaml.load(fp, Loader=yaml.Loader)
        rules = filter(lambda r: r.split(',')[0] in ('DOMAIN-SUFFIX', 'DOMAIN-KEYWORD'), data['rules'])

    with open(OUTPUT_PATH, 'w') as fp:
        data = {'custom-rules': list(rules)}
        yaml.dump(data, fp)

