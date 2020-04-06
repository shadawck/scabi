"""
Get the vulnerabilities from different source (See docs/vuln-source.md) for each package found
"""
import json
import requests
from bs4 import BeautifulSoup

from scabi import utility_pms
from scabi import pip_scan
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

    headers = {'Authorization': 'token user:1c236b9c013d300d0f973f42d855692533535f2c',
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
    list_vuln_by_dep = []

    for dep in listPackage: 
        list_vuln_by_dep.append(OSS_parse_api_reponse(pms_name,dep))
    
    return list_vuln_by_dep


############################
##### CVE MITRE Source #####
############################
# https://cve.mitre.org/cve/search_cve_list.html

# No API but you can download the source in differents format XML, CSV ... but these are heavy file 
# It's more pratical to make little requests
# So let's go make a litle API with beautifulsoup and requests


def MITRE_get_main_page(package): 
    """
    Get all the CVE for a package/keyword
    """
    base_url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=" + package
    rq = requests.get(base_url).text

    # data struct : 
    # [(cve_name1, cve_link1, cve_desc1),...,(cve_name_n, cve_link_n, cve_desc_n)]
    cve_group = []
    soup = BeautifulSoup(rq, 'html.parser')


    # Get each line (cve_name/link, cve_description) from request rq in html format
    soup = soup.select("#TableWithRules")[0].find_all("tr") 

    souptd = []
    for el in soup : 
        souptd.append(el.find_all("td"))

    for td in souptd[1:] : 

        cve_group.append(
            (
                td[0].string.strip(), 
                 "https://cve.mitre.org" + td[0].a['href'],
                td[1].string.strip()
            )
        )
    return cve_group

def MITRE_get_cve_detail(package):
    cve_group = MITRE_get_main_page(package)
    cve_detail = []
    cve_ref = []


    def get_links():
        listLinks = []
        for i in range(len(cve_group)) :
            listLinks.append(cve_group[i][1])
        return listLinks
    
    links = get_links()

    # Big loop -> need opti
    for l in links: 
        rq = requests.get(l).text
        soup = BeautifulSoup(rq, 'html.parser')
        
        ## reference links
        ref_links = soup.select("#GeneratedTable > table > tr > td > ul")[0].find_all("a") 
        ## Get NVD links for more detail
        more = soup.select("#GeneratedTable .ltgreybackground .larger")[0].find("a")["href"]

        # construct list of reference links 
        for ref in ref_links : 
            cve_ref.append(ref["href"])

        # construct final list 
        # data struct : 
        # [(more_cve_1, [ref_1_cve_1, ref_2_cve_1]) ,..., (more_cve_n, [ref_1_cve_n, ref_2_cve_n])]
        cve_detail.append(
            (
                more,
                cve_ref
                # add more data here
            )
        )
    
    return cve_detail 


############################
##### CIRCL CVE source #####
############################
# https://cve.circl.lu/
# https://cve.circl.lu/api/
# ABORTED : the api doesn't expose search by product. To search for a keyword (product) you need
# the vendor name and the product name so you can't discover CVE just based on package
# SOLUTION : Create a new API which parse the cve.circl.lu search page





############################
##### VULDB CVE source #####
############################
# https://vuldb.com/?doc.api
# https://vuldb.com/?search.advanced