#!/usr/bin/env python3
from collections import OrderedDict
import json

from scabi import utility_pms

def get_npm_dependencies(package): 
    """
    get list of dependencies from pms command
    """
    npmDependencies = []


    p = utility_pms.run_command("npm",package) # Json data
    try:    
        loaded_json = json.loads(p.stdout)
        for word in loaded_json:
        	npmDependencies.append(word)
            
    except json.decoder.JSONDecodeError:
        return []
    
    return npmDependencies
        


