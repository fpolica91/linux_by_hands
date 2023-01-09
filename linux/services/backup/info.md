##[backup.timer]
This configuration specifies a timer unit in Systemd that runs a task on a specific schedule. The timer unit is defined by the [Timer] section, which specifies the schedule and other options for the timer.

The OnCalendar option specifies the schedule for the timer in the form of a cron-style calendar event. In this case, the timer is set to run at 23:00 (11:00 PM) every day. The _-_-\* part of the schedule specifies that the timer should run every day of the month, every month, and every day of the week.

The Persistent option specifies that the timer should save its state between reboots. If this option is set to true, then the timer will continue to run on its schedule even if the system is restarted. If it is set to false, then the timer will reset its state when the system is restarted.

The Unit option specifies the name of the service unit that the timer should run. In this case, the timer is set to run the web-backup.service unit. This service unit should contain the instructions for the task that the timer is scheduled to run.

To run this service you must enabled copy it to the executable to `/usr/local/sbin/` and the services to `/etc/systemd/system/` the first location is used to store executable and the `/etc/systemd/system/` is used to store Systemd services.

### excuting script

1. Reload daemon `systemctl daemon-reload`
2. Enable services `systemctl enable web-backup.service` and `systemctl enable web-backup.timer`
3. Set permissions for file to be executable `chmod +x /usr/local/sbin/web-backup.sh`
4. Manually start services `systemctl start web-backup.service` and `systemctl start web-backup.timer`
