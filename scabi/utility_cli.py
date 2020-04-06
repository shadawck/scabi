from scabi import utility_pms
from scabi import crawler

def print_dependencies(listDependencies):
    if listDependencies == [] : print("No dependencies found")
    print("The dependencies for <" + utility_pms.get_package_name() + "> are :")
    for dep in listDependencies : 
        print("...", dep)

def OSS_print_vulnerabiliies(listDependencies):
    list_vuln_by_dep = crawler.OSS_get_dep_vulerabilities(listDependencies)
    i = 0

    print("\n>>>>>>>>>>>>>>> SEARCH IN OSS INDEX <<<<<<<<<<<<<<<")

    for package in list_vuln_by_dep : 
        if package == [] :
            print("\n-------------- Package: <" + listDependencies[i] + "> --------------")
            print("NO VULNERABILITIES FOUND")
            i += 1
            continue
            
        print("\n-------------- Package: <" + listDependencies[i] + "> --------------", "\n")
        
        i += 1
        for v in package : 
            print( "title :"       , v[0])
            print( "description :" , v[1])
            print( "cvssScore :"   , v[2])
            print( "cve :"         , v[3])
            print( "reference :"   , v[4])
            print("\n")

def MITRE_print_vulnerabilites(listDependencies): 
    i = 0

    print("\n>>>>>>>>>>>>>>> SEARCH IN MITRE DATABASE <<<<<<<<<<<<<<<")


    for dep in listDependencies :
        list_vuln_by_dep = crawler.MITRE_get_main_page(dep)
        if list_vuln_by_dep == [] : 
            print("\n-------------- Package: <" + listDependencies[i] + "> --------------")
            print("NO VULNERABILITIES FOUND")
            i += 1
            continue

        print("\n-------------- Package: <" + listDependencies[i] + "> --------------\n")
        i +=1

        ## # [(cve_name1, cve_link1, cve_desc1),...,(cve_name_n, cve_link_n, cve_desc_n)]
        for cve in list_vuln_by_dep : 
            print("CVE :"       ,  cve[0]) # print cve_name 
            print("CVE DETAIL"  ,  cve[1]) # print cve_link
            print("DESCRIPTION" ,  cve[2]) # print cve_description
            print("\n")




        







    
