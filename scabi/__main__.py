#!/usr/bin/env python3
# __main__.py



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

    pms = utility_pms.get_pms_name()
    package = utility_pms.get_package_name()
    

    if pms == 'apt' or pms == 'apt-get' : 
        deps = apt_scan.get_apt_dependencies()
        utility_cli.print_dependencies(deps)
        utility_cli.OSS_print_vulnerabiliies(deps)

    elif pms == 'composer'  : 
        deps = composer_scan.get_composer_dependencies()
        utility_cli.print_dependencies(deps)
        utility_cli.OSS_print_vulnerabiliies(deps)

    elif pms == 'gem'       : 
        deps = gem_scan.get_gem_dependencies()
        utility_cli.print_dependencies(deps)
        utility_cli.OSS_print_vulnerabiliies(deps)

    elif pms == 'npm'       : 
        deps = npm_scan.get_npm_dependencies()
        utility_cli.print_dependencies(deps)
        utility_cli.OSS_print_vulnerabiliies(deps)

    elif pms == 'pip'       : 
        deps = pip_scan.get_pip_dependencies()
        utility_cli.print_dependencies(deps)
        utility_cli.OSS_print_vulnerabiliies(deps)
        utility_cli.MITRE_print_vulnerabilites(deps)

    else : 
        print("Your PMS is not supported for the moment")
        utility_pms.print_supported_pms()
    


if __name__ == "__main__":
    main()