#!/usr/bin/env python3
from collections import OrderedDict
import json

from scabi import utility_pms

def get_pip_dependencies(package): 
    """
    get list of dependencies from pip command
    """
    pipDependencies = []
    p = utility_pms.run_command("pip", package)
    
    try:    
        data = json.loads(p)['info']['requires_dist']
        for word in data : 
            pipDependencies.append(word.split()[0])
        
        # remove double
        pipDependencies = list(OrderedDict.fromkeys(pipDependencies))
            
    except TypeError:
        return [] # if data doesn't exist
        

    return pipDependencies
        
