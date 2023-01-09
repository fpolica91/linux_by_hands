# systemclt

- in order to change systemctl default target, we must know what target is currently the default.
  this can be done by running `systemctl get-default`
- to set a different default target use `systemctl set-default <target>` the target options are `graphical.target | multi-user.target and emergency.target`
  `systemctl get-default`
  is a command that can be used to retrieve the default system runlevel in a Linux system that uses Systemd as its init system. The default runlevel specifies the set of services that are started at boot time, as well as the default target that is set after the system boots up.
