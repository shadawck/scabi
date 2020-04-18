#!/usr/bin/env python3
# __main__.py

"""Scabi

Usage:
  scabi <pms> <package> [--verbose --detail ] [--oss  --mitre] [-s FILE]
  scabi -h --help --version

Options:
  -v --verbose      Show full output.
  -d --detail       Show CVE details.
  -o --oss          Search vulnerabilities only through OSS.
  -m --mitre        Search vulnerabilities only through MITRE.
  -s --save FILE    Save output to file.
  -h --help         Show this screen.      
"""

import sys
from docopt import docopt
from getdep import getdep
from getdep import utility as udep

import mitrecve
from mitrecve import utility as ucve


from scabi import utility_cli
from scabi import crawler
from scabi import __version__


def main():
    """
    Implement CLI logic 
    """
    arguments = docopt(__doc__, version='scabi ' + __version__)
    
    ############## CLI VAR ################
    __verbose    = arguments["--verbose"]
    __detail     = arguments["--detail"]
    __pms        = arguments["<pms>"]
    __package    = arguments["<package>"]
    __oss_mode   = arguments["--oss"]
    __mitre_mode = arguments["--mitre"]
    __save       = arguments["--save"] 

    print("START CRAWLING...")

    if __save    :  
        __save_ext = __save.split(".")[0]
        sys.stdout=open(__save,"w")



    ############# CLI PMS SELECTION #######
    if __pms == 'apt' or __pms == 'apt-get' : 
        deps = getdep.get_apt_dependencies(__package)

    elif __pms == 'composer'  : 
        deps = getdep.get_composer_dependencies(__package)
        if deps != None :
            deps = deps[1:-1] # remove "php" from dependency list

    elif __pms == 'gem'       : 
        deps = getdep.get_gem_dependencies(__package)

    elif __pms == 'npm'       : 
        deps = getdep.get_npm_dependencies(__package)

    elif __pms == 'pip'       : 
        deps = getdep.get_pip_dependencies(__package)
       
    else : 
        print("Your PMS is not supported for the moment")
        udep.print_supported_pms()
        exit()

    udep.print_dependencies(__package,deps)

    ############## DATABASE SELECTION ##########
    if __oss_mode : ## OSS MODE 
        utility_cli.OSS_print_vulnerabiliies(__pms,deps,__verbose)

    elif __mitre_mode : ## MITRE MODE
        
        if __detail :  # MITRE MODE with CVE DETAIL
            ucve.MITRE_print_vulnerabilites_detail(deps,__verbose)
        
        else : # MITRE MODE without CVE DETAIL
            ucve.MITRE_print_vulnerabilites(deps,__verbose)
    else : ## OSS AND MITRE MODE

        utility_cli.OSS_print_vulnerabiliies(__pms,deps,__verbose) 
        if __detail : ## WITH DETAIL
            ucve.MITRE_print_vulnerabilites_detail(deps,__verbose)
        else : ## WITHOUT DETAIl
            ucve.MITRE_print_vulnerabilites(deps,__verbose)
    

    ############### SAVE LOGIC ################

    if __save and __save_ext != 'txt' :
        print("save format :", __save_ext, "not supported for the moment")

    sys.stdout.close()
if __name__ == "__main__":
    main()