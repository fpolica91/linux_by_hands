## Problem

1. In this lab I was given a task to start `httpd.service`, which threw an error `httpd: Could not open configuration file /etc/httpd/conf/httpd.conf:`
2. We discovered that the `httpd.conf` file was missing, but there was a backup present by using `ls -l /etc/httpd/conf`
3. To solve this we need to restore the origin `httpd.conf` as follows `mv /etc/httpd/conf/httpd.conf.bkup /etc/httpd/conf/httpd.conf`. This command is usually used to restore the deleted files
4. Restart the service `systemctl restart httpd.service`
5. Check the status of the service `systemctl status httpd.service`
6. Navigate to the local page `elinks http://localhost`
