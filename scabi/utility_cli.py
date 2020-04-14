from scabi import crawler


def print_dependencies(package, listDependencies):
    if listDependencies == [] :
        print("No dependencies found")
    else :
        print("The dependencies for <" + package + "> are :")
        for dep in listDependencies : 
            print("...", dep)

def OSS_print_vulnerabiliies(pms_name, listDependencies, __verbose ):
    list_vuln_by_dep = crawler.OSS_get_dep_vulerabilities(pms_name, listDependencies)
    i = 0

    print("\n>>>>>>>>>>>>>>> SEARCH IN OSS INDEX <<<<<<<<<<<<<<<")

    for package in list_vuln_by_dep : 
        if package == [] :
            if __verbose : 
                print("\n-------------- Package: <" + listDependencies[i] + "> --------------")
                print("NO VULNERABILITIES FOUND")
            
            i += 1
            continue
        
        else :
            print("\n-------------- Package: <" + listDependencies[i] + "> --------------", "\n")
            
            i += 1
            for v in package : 
                print( "title :"       , v[0])
                print( "description :" , v[1])
                print( "cvssScore :"   , v[2])
                print( "cve :"         , v[3])
                print( "reference :"   , v[4])
                print("\n")

