import pybgpstream

from datetime import datetime, timedelta

# Define the time range
start_date = datetime(2021, 2, 1)
end_date = datetime(2021, 4, 30)

# Specify the collectors
collectors = ["rrc00", "rrc13", "rrc22"]

ru_prefixes = []
uk_prefixes = []

with open('prefixes_russia.txt', 'r') as f:
   for line in f:
      ru_prefixes.append(line.strip())
f.close()
with open('prefixes_ukraine.txt', 'r') as f:
    for line in f:
        uk_prefixes.append(line.strip())
f.close()

# Iterate over each day in the time range
current_date = start_date
while current_date <= end_date:
    count = 0
    # Create a BGPStream instance for the current day
    from_time = current_date.strftime("%Y-%m-%d 00:00:00")
    until_time = current_date.strftime("%Y-%m-%d 23:59:59")

    bgp_stream = pybgpstream.BGPStream(
        from_time=from_time,
        until_time=until_time,
        collectors = collectors,
        record_type = "updates"
    )

    # Start the stream and iterate through the records for the current day
    # comment from here
    # for record in bgp_stream.records():
    #     # Extract relevant information from the record
    #     elem = record.get_next_elem()
    #     while elem:
    #         # Your processing logic here
    #         count += 1

    #         # Get the next BGP update element in the record
    #         elem = record.get_next_elem()
    # comment ends here
    rec = list(bgp_stream.records())
    print(f"{current_date} - {len(rec)}")

    # Move to the next day
    current_date += timedelta(days=1)
