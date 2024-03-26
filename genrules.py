import sys
import re
from datetime import datetime
import yaml


ip_cidr_regexp = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{2}')
ip_cidr6_regexp = re.compile(r'([a-f0-9:]+:+)+[a-f0-9]+/\d{1,3}')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('''Usage: 
    {} ruleset1.yaml [ruleset2.yaml ...]
'''.format(sys.argv[0]))
        sys.exit(0)
    
    ruleset = set()
    for filename in sys.argv[1:]:
        with open(filename, 'r') as fp:
            data = yaml.load(fp, Loader=yaml.Loader)

            if 'payload' in data:
                for rule in data.get('payload'):
                    if rule.startswith('+.') or rule.startswith('*.'):
                        # DOMAIN-SUFFIX
                        ruleset.add('DOMAIN-SUFFIX,{},PROXY'.format(rule[2:]))
                    elif ip_cidr_regexp.fullmatch(rule) is not None:
                        # IP-CIDR
                        ruleset.add('IP-CIDR,{},PROXY'.format(rule))
                    elif ip_cidr6_regexp.fullmatch(rule) is not None:
                        # IP-CIDR6
                        ruleset.add('IP-CIDR6,{},PROXY'.format(rule))
                    else:
                        ruleset.add('DOMAIN,{},PROXY'.format(rule))
            
            # Add custom rules
            if 'custom-rules' in data:
                ruleset.update(data['custom-rules'])

    print('''# FreeRules for Shadowrocket: {}
[General]
bypass-system = true
skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, localhost, *.local, captive.apple.com
tun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.18.0.0/15, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32
dns-server = system
ipv6 = false\n'''.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    print('[Rule]')
    for rule in ruleset:
        print(rule)
    print('FINAL,DIRECT\n')

#     print('''[URL Rewrite]
# ^http://(www.)?google.cn https://www.google.com 302\n''')

#     # Scripts
#     print('''[Script]
# bypass_paywalls = type=http-request,script-path=https://raw.githubusercontent.com/wuk0o/freerules/release/scripts/bypass_paywalls.js,pattern=https://www.wsj.com,enable=true
# ''')
