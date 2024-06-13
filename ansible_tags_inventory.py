#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
    
# Settings Variable
hosts_tag_file_path = "hosts_tag_file"


# read hosts files
f = open(hosts_tag_file_path, "r")
lines = f.readlines()

# decalre tags group list
tags_group = []

# get hosts tags list 
for host in lines:
    for item in host.split():
        sub_string = "tags="
        if sub_string in item:
            tags_group = tags_group + (item.split('=')[1].split(','))

# uniqe list values
tags_group = list(set(tags_group))


# Create ansible inventory structure
ansible_inventory = {
    "_meta":{
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
         "hosts": []
    }
}

# Insert tags_group's data into inventory
for group in tags_group:
    obj = {group: {"hosts": []}}
    ansible_inventory.update(obj)

# Insert host's fqdn to groups
for host in lines:
    host_fqdn = host.split()[1]
    for item in host.split():
        sub_string = "tags="
        if sub_string in item:
            host_group_list = item.split('=')[1].split(',')
            for host_group in host_group_list:
                ansible_inventory[host_group]['hosts'].append(host_fqdn)

# Insert All hosts fqdn to ungrouped
for host in lines:
    host_fqdn = host.split()[1]
    ansible_inventory['ungrouped']['hosts'].append(host_fqdn)


# Insert host's fqdn relate with ipv4 in ansible_inventory._meta.hostvars
for host in lines:
    host_ipv4 = host.split()[0]
    host_fqdn = host.split()[1]
    obj = {
        host_fqdn: {
            'ip': [
                host_ipv4
            ]
        }
    }
    ansible_inventory['_meta']['hostvars'].update(obj)

print(json.dumps(ansible_inventory, indent=4, sort_keys=True))


