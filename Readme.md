# Setup Development Environment

## Prerequisites

[Dependencies](docs/dependencies.md)

## Quick Start

1. Clone GitHub - **git clone https://github.com/scottbrumley/opendxl-joesandbox.git**
2. [Copy DXL Information](docs/dxlinfo.md)
3. Edit your scripts/bootstrap.sh script and Add your Joe Sandbox Key
4. Start Environment - **vssh.sh** 

## Quick Start Video
[Joe Sandbox Dev Environment Video](https://youtu.be/3aCX6tAZC4o)

### Example
```
./vssh.sh on Linux/Mac OS
vssh.sh on Windows (make sure Windows has Git ssh in the path)
```

## Phoenix the Environment
If you want to burn the whole thing to the ground just exit the guest and use this command.
```
exit
./vclean.ssh
```

### About Vagrant
https://www.vagrantup.com/

Vagrant uses the Vagrantfile to build environment.  Important lines:
```
config.vm.box = "sbrumley/opendxl"
config.vm.provision "shell", path: "scripts/bootstrap.sh"
```

### About Git
https://git-scm.com

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## LICENSE

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
