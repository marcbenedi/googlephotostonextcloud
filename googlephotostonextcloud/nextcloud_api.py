import requests
from requests.auth import HTTPBasicAuth
from .xml_utils import get_default_xml_body
import subprocess

class NextCloudAPI:
    def __init__(self, url, user, pw, occ_cmd:callable) -> None:
        self.url = url
        self.user = user
        self.pw = pw
        self.occ_cmd = occ_cmd

    def _base_request(self, method, path, data=None):
        response = requests.request(
            method,
            f"{self.url}/remote.php/dav/files/{self.user}/{path}",
            auth=HTTPBasicAuth(self.user, self.pw),
            headers={'Content-Type': 'application/xml'},
            data=data
        )
        return response

    def get_file(self, file_path):
        response = self._base_request('GET', file_path)
        
        assert 200 <= response.status_code and response.status_code < 300, f"Error getting file {file_path}"
        return response.text
    
    def run_occ(self, command):
        full_command = self.occ_cmd(command)
        # print(full_command)
        
        process = subprocess.run(full_command, 
                                 shell=True,
                                 check=False, 
                                #  text=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        
        # print("STDOUT:", process.stdout)
        # print("STDERR:", process.stderr)
        return process.stdout.decode()
    
    def run_occs(self, commands):
        command = commands.join(" ; ")
        full_command = self.occ_cmd(command)
        # print(full_command)
        
        process = subprocess.run(full_command, 
                                 shell=True,
                                 check=False, 
                                #  text=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        
        # print("STDOUT:", process.stdout)
        # print("STDERR:", process.stderr)
        return process.stdout.decode()