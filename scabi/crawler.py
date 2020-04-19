"""
Get the vulnerabilities from different source (See docs/vuln-source.md) for each package found
"""
import json
import requests


# curl -X GET "https://ossindex.sonatype.org/api/v3/component-report/pkg://pypi/requests@latest" -H "accept: application/vnd.ossindex.component-report.v1+json"

############################
##### OSS Index Source #####
############################
# https://ossindex.sonatype.org/search

def get_platform_for_eco():
    """ Just for os dependent pms like apt
    get the platform of execution to select the right ecosystem. 
    Ex : fedora -> eco : fedora
         ubuntu -> eco : deb
         alpine -> eco : alpine
         RHEL   -> eco : rpm
        
    Insert in OSS_send_api_request->construct_ecosystem()
    """
    pass

def OSS_send_api_request(pms_name,package):
    """Get vulnerabilities (CVE) of given package management system and package.

    Args:
        pms_name (str) : Name of the package management system.
        package (str): Name of the package choosen by the user.

    Return: 
        dict. dict (json) of CVE for gievn input.

    """

    def construct_ecosystem():
        if pms_name == 'apt'         : eco = 'deb'
        elif pms_name == 'composer'  : eco = 'composer'
        elif pms_name == 'gem'       : eco = 'rubygem'
        elif pms_name == 'npm'       : eco = 'npm'
        elif pms_name == 'pip'       : eco = 'pypi'
        else : 
            eco = ''
            print("PMS not supported for the moment")
            exit()
        return eco

    def OSS_build_uri():

        ecosystem = construct_ecosystem()
        base_url = "https://ossindex.sonatype.org/api/v3/component-report/pkg://"
        url = base_url + ecosystem + "/" + package + "@latest" # Change @latest to version variable in futur release
        return url
    
    url = OSS_build_uri()

    headers = {'Authorization': 'token user:7d1b2c92676d07f9a5a24fd6d4e175d64a4cba55',
               'accept':'application/vnd.ossindex.component-report.v1+json'
    }

    rq = requests.get(url, headers=headers)

    # Exit if request return noting ( HTTP 429 )
    if rq.status_code != 200:
        print('OSS Index : You have to wait a little: Too Many Request. Status code : ', rq.status_code, "\n")
        exit()
    
    rq = rq.json()
    return rq

def OSS_parse_api_reponse(pms_name, package):
    """Parse dict of OSS_send_api_request(pms_name, package)
    
    Args:
        pms_name (str) : Name of the package management system.
        package (str): Name of the package choosen by the user.

    Return:
        list. List of CVE for given package
    
    """
    
    resp = OSS_send_api_request(pms_name,package)
    cve_list =  []

    # if package is unkown or don't have dependencies, just return an empty list 
    if resp["vulnerabilities"] == [] :
        return cve_list # list is empty

    for vuln in resp["vulnerabilities"]:
        cve_list.append(
            (  
               vuln["title"],
               vuln["description"],
               vuln["cvssScore"],
               vuln["cve"], 
               vuln["reference"]
            )
        )
    return cve_list
        
def OSS_get_dep_vulerabilities(pms_name, listPackage):
    """
    
    Args:
        pms_name (str) : Name of the package management system.
        listPackage (list) : List of package (dependencies)

    return:
        list. List of cve for all the package from "listPackage"

    """



    list_vuln_by_dep = []

    for dep in listPackage: 
        list_vuln_by_dep.append(OSS_parse_api_reponse(pms_name,dep))
    
    return list_vuln_by_dep

############################
##### CIRCL CVE source #####
############################
# https://cve.circl.lu/
# https://cve.circl.lu/api/
# ABORTED : the api doesn't expose search by product. To search for a keyword (product) you need
# the vendor name and the product name so you can't discover CVE just based on package
# SOLUTION : Create a new API which parse the cve.circl.lu search page

# TODO

############################
##### VULDB CVE source #####
############################
# https://vuldb.com/?doc.api
# https://vuldb.com/?search.advanced

# TODO
