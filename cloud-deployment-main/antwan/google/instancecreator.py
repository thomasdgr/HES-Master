#!/usr/bin/env python

# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example of using the Compute Engine API to create and delete instances.
Creates a new compute engine instance and uses it to apply a caption to
an image.
    https://cloud.google.com/compute/docs/tutorials/python-guide
For more information, see the README.md under /compute.
"""

import argparse
import os
import time

import googleapiclient.discovery


# [START list_instances]
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None
# [END list_instances]


# [START create_instance]
def create_instance(compute, project, zone, name, bucket, image, scrypt):
    # Configure the machine
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), scrypt), 'r').read()

    config = {
        'name': name,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': "projects/"+ project +"/global/images/" + image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            },{
                'key': 'bucket',
                'value': bucket
            }]
        }
    }

    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()


def wait_for_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)


def get_external_ip(compute, project, zone, name):
    return compute.instances().get(
        project = project,
        zone = zone,
        instance = name).execute()

def write_frontend_sh(ip):
    f = open("front.sh", "w")
    f.write("#!/bin/bash\n")
    f.write("cd /home/antoine_blancy\n")
    #sed -i '1c\const backddr = "130.211.201.255";' script.js
    f.write("sed -i '1c\const backaddr = \"http://" + ip + "\";' script.js\n")
    f.write("python3 -m http.server")
    f.close()

    
if __name__ == '__main__':
    compute = googleapiclient.discovery.build('compute', 'v1')
    project = "cloud-dep"
    zone = "europe-west6-a"
    bucket = ""
    instance_name = ["backdndndo", "frontdndndo"]
    name = ["vm-back", "vm-front"]
    imagename = ["backendtemp", "frontendtemp"]

    operation = create_instance(compute, project, zone, instance_name[0], bucket, imagename[0], "back.sh")
    wait_for_operation(compute, project, zone, operation['name'])

    #modify startup script for backend ip in frontend
    info = get_external_ip(compute, project, zone, instance_name[0])
    print(info['networkInterfaces'][0]['accessConfigs'][0]['natIP'])
    write_frontend_sh(info['networkInterfaces'][0]['accessConfigs'][0]['natIP'])

    operation = create_instance(compute, project, zone, instance_name[1], bucket, imagename[1],"front.sh")
    wait_for_operation(compute, project, zone, operation['name'])

    info = get_external_ip(compute, project, zone, instance_name[1])
    print(info['networkInterfaces'][0]['accessConfigs'][0]['natIP'])

    instances = list_instances(compute, project, zone)
    for instance in instances:
        print(' - ' + instance['name'])

