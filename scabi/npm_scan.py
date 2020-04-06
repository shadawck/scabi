#!/usr/bin/env python3
from collections import OrderedDict
import json

from scabi import utility_pms

def get_npm_dependencies(): 
    """
    get list of dependencies from pms command
    """
    npmDependencies = []

    try:
        p = utility_pms.run_command() # Json data

        try:    
            loaded_json = json.loads(p.stdout)
            for word in loaded_json:
            	npmDependencies.append(word)
                
        except json.decoder.JSONDecodeError:
            print("No dependencies")

        return npmDependencies
        
    except UnboundLocalError:
        print("Your Package Management System : is not supported")
        utility_pms.print_supported_pms()
        return []

