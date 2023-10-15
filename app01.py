'''
https://www.influxdata.com/blog/getting-started-python-influxdb/
'''

from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)

client.create_database('pyexample2')

client.get_list_database()

client.switch_database('pyexample2')

json_body = [
    {
        "measurement": "temperature",
        "fields": {"value": 25.5}
    },
    {
        "measurement": "temperature",
        "fields": {"value": 22.3}
    },
    {
        "measurement": "temperature",
        "fields": {"value": 23.7}
    }
]

client.write_points(json_body)
query = 'SELECT "value" FROM "temperature"'
result = client.query(query)

print(result)

print("Temperature data from InfluxDB:")
for point in result.get_points():
    print(f"Temperature: {point['value']}")

# Close the InfluxDB connection
client.close()
