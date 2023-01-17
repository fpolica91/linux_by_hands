## Troubleshoting RPM packages

#### Install telnet (in this example there is a problem with the RPM database)

1. First, let's become root:
   `sudo -i`
2. Install the telnet package:
   `yum install -y telnet`

3. Verify the integrity of the RPM database:
   `cd /var/lib/rpm/`
   `/usr/lib/rpm/rpmdb_verify Packages`

4. Move Packages to Packages.bad and create a new RPM database from Packages.bad:
   `mv Packages Packages.bad`
   `/usr/lib/rpm/rpmdb_dump Packages.bad | /usr/lib/rpm/rpmdb_load Packages`

5. Verify the integrity of the new RPM database:  
   `/usr/lib/rpm/rpmdb_verify Packages`

6. Query installed packages for errors:
   `rpm -qa > /dev/null`

7. Rebuild the RPM database:
   `rpm -vv --rebuilddb`

8. Install telnet:
   `yum install -y telnet`

### Install Apache (in this example httpd is excluded in the yum configuration)

1. Attempt to install Apache:
   `yum install -y httpd`

2. Edit `/etc/yum.conf`:
   `vim /etc/yum.conf`

3. Remove the exclusion for httpd:
   `exclude=httpd`
4. Save and close the file:
   `:wq`
5. Install Apache:
   `yum install -y httpd`
