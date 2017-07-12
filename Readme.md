# Joe Sandbox Cloud McAfee Threat Intelligence Exchange Integration
## Overview
This Solution allows the Cloud version of Joe Sandbox to update McAfee Threat Intelligence Exchange "TIE" 
Enterprise file reputations based on files convicted by Joe Sandbox.

The updated reputation can be seen in the TIE Server via ePO in the TIE Reputation page->File Overrides tab.
The comment field/column has the text "Reputations Score from Joe Sandbox".

The Solution gets the latest list of files convictedBy Joe Sandbox by querying the Server with the specified
Polling Interval and sets the TIE Enterprise reputation over DXL.
 
## Prerequisites
The solution sets the Enterprise reputation of a file in TIE. This requires a working TIEServer environment
Please refer to the prerequisites of tie client at https://github.com/opendxl/opendxl-tie-client-python/wiki/Prerequisites.

Note: Python Client must have permissions to set Reputation. 
See [FAQ](https://github.com/opendxl/opendxl-tie-client-python/wiki/FAQ)
to change authorization permissions in ePO for allowing Python Client to set TIE reputations.


To start using the Joe Sandbox Cloud McAfee Threat Intelligence Exchange Integration,
you can do a Standalone install or Vagrant setup

## Usage Standalone
The following steps walk through running the OpenDXL Slack/TIE integration in standalone mode:

* Download the latest release of the [OpenDXL Joe Sandbox](https://github.com/scottbrumley/opendxl-slack/releases)
* Extract the downloaded release
* Provision the files necessary for an OpenDXL client (dxlclient.config and related certificate files).
    * The steps are identical to those described in the OpenDXL Client Samples Configuration documentation.
* Place the dxlclient.config and related certificate files into the same directory as the dxl_bot.py file (in the extracted release)
* python install -r requirements.txt   
* Create a [Joe Sandbox](https://www.joesecurity.org/joe-sandbox-cloud) account and get a API Key
* Set the Environment variables JOE_POLL and JOE_KEY.
    * `JOE_POLL` (Poll Interval Ex 1) 
    * `JOE_KEY` (The provided API Key)    
  * Run the joe-service.py module
    * `python joe-service.py`
* Login to ePO. The updated reputation can be seen in the TIE Server via ePO in the TIE Reputation page->File Overrides tab.
The comment field/column has the text `Reputations Score from Joe Sandbox`

## Vagrant Setup Development Environment

### Prerequisites

[Dependencies](docs/dependencies.md)

### Quick Start

1. Clone GitHub - **git clone https://github.com/scottbrumley/opendxl-joesandbox.git**
2. [Copy DXL Information](docs/dxlinfo.md)
3. Edit your scripts/bootstrap.sh script and Add your Joe Sandbox Key
4. Start Environment - **vssh.sh** 

### Quick Start Video
[Joe Sandbox Dev Environment Video](https://youtu.be/3aCX6tAZC4o)


#### Example
```
./vssh.sh on Linux/Mac OS
vssh.sh on Windows (make sure Windows has Git ssh in the path)
```

### Phoenix the Environment
If you want to burn the whole thing to the ground just exit the guest and use this command.
```
exit
./vclean.ssh
```
#### About Vagrant
https://www.vagrantup.com/

Vagrant uses the Vagrantfile to build environment.  Important lines:
```
config.vm.box = "sbrumley/opendxl"
config.vm.provision "shell", path: "scripts/bootstrap.sh"
```

#### About Git
https://git-scm.com

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

### LICENSE

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
