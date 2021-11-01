#!/usr/bin/env python

import yaml
import os
import sys

CLASH_CFG_PATH = os.path.expanduser('~/.config/clash/custom.yaml')
CUSTOM_PATH = os.path.abspath('./custom.yaml')


if __name__ == '__main__':
    for fname in [CLASH_CFG_PATH, CUSTOM_PATH]:
        if not os.path.isfile(fname):
            print('%s not found!' % fname)

    rules = []
    with open(CLASH_CFG_PATH, 'r') as fp:
        data = yaml.load(fp, Loader=yaml.Loader)
        rules = filter(lambda r: r.split(',')[0] in ('DOMAIN-SUFFIX', 'DOMAIN-KEYWORD'), data['rules'])

    with open(CUSTOM_PATH, 'w') as fp:
        data = {'custom-rules': list(rules)}
        yaml.dump(data, fp)

