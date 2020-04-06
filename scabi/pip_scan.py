#!/usr/bin/env python3
from collections import OrderedDict
import json

from scabi import utility_pms

def get_pip_dependencies(): 
    """
    get list of dependencies from pip command
    """
    pipDependencies = []
    try:
        p = utility_pms.run_command()
        
        try:    
            data = json.loads(p)['info']['requires_dist']
            for word in data : 
                pipDependencies.append(word.split()[0])
                
        except TypeError:
            print("No dependencies")

        # remove double
        pipDependencies = list(OrderedDict.fromkeys(pipDependencies))

        return pipDependencies
        
    except UnboundLocalError:
        print("Your Package Management System : is not supported")
        utility_pms.print_supported_pms()
        return []
