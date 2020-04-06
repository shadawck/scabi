import subprocess
import sys
import shlex
import requests

# Get install pms command :  pms apt install <package> -> apt install <package>
# Then run_command get stdout of pms command -> stdout of  "apt install <package>"

def get_command():
    """
    get command arguments from stdin
    """
    return sys.argv[1:]
    
    #RETURN STRING # return " ".join(map(cmd_quote, sys.argv[1:]))

def get_package_name():
    return get_command()[-1].strip(' ')

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

def get_pms_name():
    pms_command = get_command()

    if pms_command[0] == 'sudo':
        pms_name = pms_command[1]
    
    elif pms_command[0] == 'install' :
        print("You need to precise a Package management system : \n Ex : sudo apt install <package>")
        exit(0)
    elif pms_command[0] in get_supported_pms():
        pms_name = pms_command[0]
    elif len(get_command()) == 1 : 
        print("Please provide a correct installation command \n Ex : ./<pms>_scan.py sudo apt install ", pms_command[0])
        exit()
    else : 
        pms_name = pms_command[0]
    return pms_name


def run_command():
    """
    run apt-rdepends command with the user given package to list dependencies on stdout
    """
    pms_command = get_command()
    package = pms_command[-1]
    pms_name = get_pms_name()    

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

