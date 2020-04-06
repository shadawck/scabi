#!/usr/bin/env python3
from collections import OrderedDict
import json

from scabi import utility_pms

def get_composer_dependencies(): 
    """
    get list of dependencies from composer command
    """
    composerDependencies = []
    try:
        p = utility_pms.run_command()

        data = json.loads(p)["package"]["versions"]
        for x in data :
            # Get dev-master dependencies
            # dev_master = data["dev-master"]["require"]
            
            # get Latest stable version and break loop
            if x.startswith("v") :
                [composerDependencies.append(x) for x in data[x]["require"]]
                break

        return composerDependencies
        
    except UnboundLocalError:
        print("Your Package Management System : is not supported")
        utility_pms.print_supported_pms()
        return []

