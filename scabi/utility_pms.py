import subprocess
import sys
import shlex
import requests

def get_supported_pms():
    return ['apt', 
            'apt-get', 
            'gem',
            'npm',
            'composer']
    
def print_supported_pms():
    supported_pms = get_supported_pms()
    print("Supported PMS are : ")
    for pms_name in supported_pms : 
        print("\t", pms_name)


def run_command(pms_name, package):
    """
    run apt-rdepends command with the user given package to list dependencies on stdout
    """
    # Switch case for all pms supported : gem , apt, rpm , composer....
    if pms_name == "apt" or pms_name == 'apt-get': commandToRun = ["sudo", "apt-rdepends", str(package)]
    elif pms_name =='gem' :                        commandToRun = ["sudo", "gem", "dependency", "--pipe" , str(package)]
    elif pms_name == 'npm' :                       commandToRun = ["sudo", "npm", "view", "--json", str(package), "dependencies"]
    elif pms_name == 'composer' :  # Make api request to packagist
        base_url = "https://repo.packagist.org/packages/"
        url = base_url + package + ".json" # Ex : https://repo.packagist.org/packages/paragonie/random-lib.json
        return requests.get(url).text # return json 
    elif pms_name == 'pip': 
        base_url = "https://pypi.org/pypi/"
        url = base_url + package + "/json" 
        
        return requests.get(url,stream=True).text # return json 

    p = subprocess.run(commandToRun, stdout=subprocess.PIPE,  encoding="ascii")
    return p 

