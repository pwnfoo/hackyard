from azure.identity import InteractiveBrowserCredential
import requests
import csv
import configparser
from os.path import expanduser,isfile

AZURE_CLI_ID = "04b07795-8ddb-461a-bbee-02f9e1bf7b46"

config = {
    "scope": ["User.ReadBasic.All",  # This is needed for Read from /users endpoint
              "People.Read"  # This is needed for reading from People API. Will only work if mailbox is enabled for user
              ],
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    "endpoint": "https://graph.microsoft.com/v1.0/me/people/"
    # More : https://docs.microsoft.com/en-us/graph/people-example
}


def _token_is_valid(token):
    """
    :param token: An authentication bearer token
    :return: bool - True if the token is valid and False if this token cannot be used to make further requests
    """

    # Fetching own info does not require any scope. Let's see if we can fetch self-profile
    test_endpoint = "https://graph.microsoft.com/v1.0/me/"

    graph_data = requests.get(test_endpoint, headers={
        'Authorization': 'Bearer ' + str(token)}).json()

    # Check if the API responded with a valid response for an authenticated user with a valid token
    if 'displayName' in graph_data.keys():
        return True
    else:
        return False


def _write_config(user, token):
    config = configparser.ConfigParser()
    config_path = expanduser("~") + "/.gallysecrets"

    config['creds'] = {}
    config['creds']['token'] = str(token)
    config['creds']['user'] = str(user)

    try:
        with open(config_path, 'w') as configfile:
            config.write(configfile)
            print("Config file written!")
            return True
    except (IOError, OSError):
        print(f"[!] Error writing config file to {args.output}. Check your permissions?")
        return False


def _handle_token(args):
    global config
    credential = InteractiveBrowserCredential()
    if args.api == 'people':
        config['endpoint'] = 'https://graph.microsoft.com/v1.0/me/people/'
    elif args.api == 'user':
        config['endpoint'] = 'https://graph.microsoft.com/v1.0/users?$top=999'
    # Calling graph using the access token
    config = configparser.ConfigParser()

    config_path = expanduser("~") + "/.gallysecrets"

    if isfile(config_path):
        # Read the existing config file
        config.read(config_path)

        if args.email == config['creds']['user']:
            print(f"[+] Cached credentials found for user {args.email}")

            if _token_is_valid(config['creds']['token']):
                return config['creds']
        else:
            auth_result = credential.get_token()
            token = auth_result.token
            _write_config(args.email, token)
            return token

    else:
        auth_result = credential.get_token()
        token = auth_result.token
        _write_config(args.email, token)
        return token


def o365dump(args):
    localconfig = {
        "scope": ["User.ReadBasic.All", "People.Read"],
        "endpoint": "https://graph.microsoft.com/v1.0/users?$top=999"
    }

    result = _handle_token(args)
    next_url = localconfig.get("endpoint")
    total_records = 0
    master_records = []
    while True:
        try:
            graph_data = requests.get(next_url, headers={
                'Authorization': 'Bearer ' + result['token']}).json()
        except TypeError:
            graph_data = requests.get(next_url, headers={
                'Authorization': 'Bearer ' + result}).json()

        # This is gonna happen because of multiple reasons. Let's print this info!
        if "error" in graph_data.keys():
            print(graph_data)

        # This field indicates that there's more info than what was requested, so use pagination logic loop
        if "@odata.nextLink" in graph_data.keys():
            terminate = False
            next_url = graph_data.get('@odata.nextLink')
        else:
            # If there's nothing, set a flag that we will use later
            terminate = True

        # Time to fetch all the GAL values from JSON. JUICY!
        if 'value' in graph_data.keys():
            people_data = graph_data.get('value')
            print(f"[+] Dumping {len(people_data)} GAL records from {args.email}'s Office 365 instance")
            total_records += len(people_data)
            master_records.extend(people_data)

        if terminate:
            break

    print(f"[*] Dumped a total of {len(master_records)} records from Office 365! Happy hacking!")

    csv_headers = list(master_records[0].keys())

    with open(args.output, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, csv_headers)
        dict_writer.writeheader()
        dict_writer.writerows(master_records)
