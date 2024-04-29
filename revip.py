import requests
from tabulate import tabulate
from termcolor import colored

def lookup_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        ip_query = data["query"]
        country = data["country"]
        region_name = data["regionName"]
        city = data["city"]
        zipcode = data["zip"]
        timezone = data["timezone"]
        isp = data["isp"]
        org = data["org"]
        asn = data["as"]

        table_data = [
            ["IP Query", ip_query],
            ["Country", country],
            ["Region", region_name],
            ["City", city],
            ["Zip Code", zipcode],
            ["Timezone", timezone],
            ["ISP", isp],
            ["Organization", org],
            ["ASN", asn]
        ]

        headers = ["Attribute", "Value"]

        # Colorize the table
        colored_table = []
        for row in table_data:
            colored_row = [colored(row[0], "cyan"), colored(row[1], "yellow")]
            colored_table.append(colored_row)

        print(tabulate(colored_table, headers=headers, tablefmt="grid"))
    else:
        print("Error: Unable to retrieve information for the provided IP address.")

if __name__ == "__main__":
    ip_address = input("Enter the IP address to lookup (press Enter for current IP): ").strip()
    if not ip_address:
        ip_address = requests.get("https://api.ipify.org").text.strip()

    lookup_ip(ip_address)
