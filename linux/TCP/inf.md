## TCP Wrappers and Systemd Sockets

### Introduction

TCP wrappers and Systemd sockets are two methods of securing network services on a Linux host.

TCP wrappers are a security feature that allows administrators to control access to internet services on a host by IP address and hostname. It works by intercepting network connection requests and checking them against a set of rules defined in two configuration files: /etc/hosts.allow and /etc/hosts.deny. Any service that is linked against the libwrap library can use these rules to control access.

On the other hand, Systemd sockets is a system and service manager for Linux operating systems. It provides a way to configure and manage network services through socket-based activation. This means that the service only starts when a connection is made to the socket and stops when the connection is closed. This feature allows to limit the attack surface of a service, and also allows to start or stop services based on the load.

Both methods have their own advantages and disadvantages, but they can be used together to provide a more robust security for your host. For example, you can use TCP wrappers to control access to a service based on IP or hostname and use Systemd sockets to control the start and stop of a service based on connections.

It's worth mentioning that both of these methods are not the only way to secure a host, there are other methods and tools that can be used to secure a host like firewalls, intrusion detection/prevention systems, and so on.

### Using at to Schedule Commands

`sudo at now + 3 minutes` is a command that schedules a task to be executed in 3 minutes time. The at command is used to schedule commands to be executed at a specified time in the future. The now argument specifies that the task should be scheduled to run immediately, and the + 3 minutes argument specifies that the task should be scheduled to run 3 minutes in the future.

The command at> `systemctl stop sshd.service` will stop the ssh daemon service, and the command at> `systemctl start sshd.socket` will start the ssh daemon socket, so after 3 minutes the ssh daemon will not be accessible via network, but the task will start the ssh daemon socket again, making it accessible via network.

It is worth mentioning that, this is a hypothetical scenario, you should be aware of the consequences of stopping and starting ssh service, and make sure to plan accordingly.

### Modifying allow and deny rules

`sudo vim /etc/hosts.allow` and add `sshd2 sshd : ALL`
`sudo vim /etc/hosts.deny` and add `ALL : ALL`
