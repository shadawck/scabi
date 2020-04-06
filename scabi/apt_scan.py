#!/usr/bin/env python3
from collections import OrderedDict

from scabi import utility_pms

def get_apt_dependencies(package): 
    """
    get list of dependencies from pms command
    """
    aptDependencies = []

    p = utility_pms.run_command("apt", package)
    # filter packages 
    for word in p.stdout.split():
        if word.startswith("Depends:") or word.endswith(")") or word.startswith("("):
            continue
        aptDependencies.append(word)
    # remove double
    aptDependencies = list(OrderedDict.fromkeys(aptDependencies))
    return aptDependencies


    
