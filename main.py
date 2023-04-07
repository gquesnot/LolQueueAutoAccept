from base64 import b64encode

import requests
import time
from urllib3.exceptions import InsecureRequestWarning
import urllib3

urllib3.disable_warnings(InsecureRequestWarning)

LOCK_FILE_PATH = "J:\\riot\\Riot Games\\League of Legends\\League of Legends\\lockfile"


class LocalLolClient:

    def __init__(self, lockfile_path):
        self.lockfile_path = lockfile_path
        self.lockfile_data = self.get_lockfile_data()

    def get_lockfile_data(self):
        with open(self.lockfile_path, "r") as lockfile:
            data = lockfile.read().split(":")
            password = b64encode(bytes("riot:{}".format(data[3]), 'utf-8')).decode('ascii')
            return {"protocol": data[4], "port": data[2], "password": password}

    def get_request_headers(self):
        return {
            "Authorization": f"Basic {self.lockfile_data['password']}",
            "Content-Type": "application/json",
        }

    def get_local_server_url(self, endpoint):
        return f"{self.lockfile_data['protocol']}://127.0.0.1:{self.lockfile_data['port']}/{endpoint}"

    def accept_queue(self):
        url = self.get_local_server_url("lol-matchmaking/v1/ready-check/accept")
        headers = self.get_request_headers()

        try:
            response = requests.post(url, headers=headers, verify=False)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    def get_flow(self):
        url = self.get_local_server_url("lol-gameflow/v1/gameflow-phase")
        headers = self.get_request_headers()

        try:
            response = requests.get(url, headers=headers, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return False


def main():
    client = LocalLolClient(LOCK_FILE_PATH)
    is_checked = False
    while True:
        flow = client.get_flow()
        if flow != "ReadyCheck" and is_checked:
            is_checked = False
        if client.get_flow() == "ReadyCheck":
            client.accept_queue()
            is_checked = True
            print('match accepted')
        time.sleep(4)


if __name__ == '__main__':
    main()
