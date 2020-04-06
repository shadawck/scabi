#!/usr/bin/env python3
from collections import OrderedDict

from scabi import utility_pms

def get_apt_dependencies(): 
    """
    get list of dependencies from pms command
    """
    aptDependencies = []
    try:
        p = utility_pms.run_command()
        # filter packages 
        for word in p.stdout.split():
            if word.startswith("Depends:") or word.endswith(")") or word.startswith("("):
                continue
            aptDependencies.append(word)

        # remove double
        aptDependencies = list(OrderedDict.fromkeys(aptDependencies))

        return aptDependencies
        
    except UnboundLocalError:
        print("Your Package Management System : is not supported")
        utility_pms.print_supported_pms()
        return []

    
