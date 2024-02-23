import json

with open('response_ukraine.txt', 'r') as fp:
    data = json.load(fp)
fp.close()
prefixes = data['data']['resources']['ipv4']

prefixes.extend(data['data']['resources']['ipv6'])


with open('prefixes_ukraine.txt', 'w') as f:
    for p in prefixes:
        f.write(f"{p}\n")
