#!/usr/bin/env python3
from collections import OrderedDict

from scabi import utility_pms

def get_gem_dependencies(): 
    """
    get list of dependencies from pms command
    """
    gemDependencies = []
    try:
        package = utility_pms.get_command()[-1]
        p = utility_pms.run_command()

        motif = p.stdout.split("\n")

        for word in motif[0:-1]: 
            # remvove different Gem version
            if word.startswith(package):
                continue 
            gemDependencies.append(word.split("--version")[0].strip())

        # remove double
        gemDependencies = list(OrderedDict.fromkeys(gemDependencies))

        return gemDependencies
        
    except UnboundLocalError:
        print("Your Package Management System : is not supported")
        utility_pms.print_supported_pms()
        return []

