# import pybgpstream

# stream = pybgpstream.BGPStream(
#     from_time="2017-07-07 00:00:00", until_time="2017-07-07 00:10:00 UTC",
#     collectors=["route-views.sg", "route-views.eqix"],
#     record_type="updates",
#     filter="peer 11666 and prefix more 210.180.0.0/16"
# )

# for elem in stream:
#     # record fields can be accessed directly from elem
#     # e.g. elem.time
#     # or via elem.record
#     # e.g. elem.record.time
#     print(elem)

import requests as r
import json

url = "https://stat.ripe.net/data/country-resource-list/data.json?resource=ua&time=2022-02-22&v4format=prefix"

resp = r.get(url)



with open('response_ukraine.txt', 'w') as f:
    json.dump(resp.json(), f, indent=4)
