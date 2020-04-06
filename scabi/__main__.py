#!/usr/bin/env python3
# __main__.py

"""cli

usage:
  cli.py <pms> install <package> [--verbose ] [--oss | --mitre]
  cli.py <pms> install <package> -s <filename> 
  cli.py --version

options:
  -v --verbose      Show full output.
  -o --oss          Search vulnerabilities only through OSS
  -m --mitre        Search vulnerabilities only through MITRE
  -s --save         Save output to file
  -h --help         Show this screen.

"""

from docopt import docopt
from scabi import utility_pms
from scabi import utility_cli

from scabi import pip_scan
from scabi import gem_scan
from scabi import npm_scan
from scabi import apt_scan
from scabi import composer_scan
from scabi import crawler


def main():
    """
    Implement CLI logic 
    """

    arguments = docopt(__doc__, version='scabi 1.0.1')
    print(arguments)
    
    ############## CLI VAR ################
    __verbose  = arguments["--verbose"]
    __pms        = arguments["<pms>"]
    __package    = arguments["<package>"]
    __oss_mode   = arguments["--oss"]
    __mitre_mode = arguments["--mitre"]
    __save       = arguments["--save"] 


    if __pms == 'apt' or __pms == 'apt-get' : 
        deps = apt_scan.get_apt_dependencies(__package)
        utility_cli.print_dependencies(__package, deps)
        utility_cli.OSS_print_vulnerabiliies(__pms, deps,__verbose)
        utility_cli.MITRE_print_vulnerabilites(deps,__verbose)

    elif __pms == 'composer'  : 
        deps = composer_scan.get_composer_dependencies(__package)
        utility_cli.print_dependencies(__package, deps)
        utility_cli.OSS_print_vulnerabiliies(__pms,deps,__verbose)
        utility_cli.MITRE_print_vulnerabilites(deps[1:-1],__verbose)


    elif __pms == 'gem'       : 
        deps = gem_scan.get_gem_dependencies(__package)
        utility_cli.print_dependencies(__package,deps)
        utility_cli.MITRE_print_vulnerabilites(deps,__verbose)
        utility_cli.OSS_print_vulnerabiliies(__pms,deps,__verbose)

    elif __pms == 'npm'       : 
        deps = npm_scan.get_npm_dependencies(__package)
        utility_cli.print_dependencies(__package,deps)
        utility_cli.MITRE_print_vulnerabilites(deps,__verbose)
        utility_cli.OSS_print_vulnerabiliies(__pms,deps,__verbose)

    elif __pms == 'pip'       : 
        deps = pip_scan.get_pip_dependencies(__package)
        utility_cli.print_dependencies(__package,deps)
        utility_cli.MITRE_print_vulnerabilites(deps,__verbose)
        utility_cli.OSS_print_vulnerabiliies(__pms,deps,__verbose)
       

    else : 
        print("Your PMS is not supported for the moment")
        utility_pms.print_supported_pms()
    

if __name__ == "__main__":
    main()