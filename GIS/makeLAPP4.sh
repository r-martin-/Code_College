#!/bin/bash

## The purpose of this script is to extend a standard LAPP (Linux/Apache/PostgreSQL/PHP  [1]) stack and extend it to handle
## spatial data. To do this we need to install PostGIS (a spatial database extender for PostgreSQL) and GeoServer (an
## open source server for sharing geospatial data). GeoServer, in this example, lives in Tomcat (an open source software
## implementation of the Java Servlet technologies).
##
## To make our LAPP stack we need to do the following
##
## 1.Create a Virtual Machine.
## We can, of course deploy LAPP on a real machine but the more usual use-case is to create a virtual machine instance
## on a larger server machine or, as is likely with our classroom examples, on our own LapTop. To create a VM we need an
## environment to support this. In our examples we'll use VirtualBox (https://www.virtualbox.org/).
##
## 1.1 Download and install VirtualBox for your platform (Windows, Linux or Mac).
## 1.2 Create a new VM. give it a name. The OS is Linux and Type is Debian 64 bit. Take all the defaults.
## 1.3 In Settings>Network You create or modify a virtual NIC (Network Interface Card). If your VM is to be deployed on a
## fixed network and is intended to be accessible from outside the network, convert Adapter 1 from NAT to Bridged Adapter.
## If you intend to deploy on a personal LapTop then leave Adapter 1 as is and enable Adapter 2. Set Adapter 2 as
## Host-only Adapter. Evertthing else in this section defaults.
## 1.4 You may want to adjust other settings to reflect your environment. For example you might wish to increase memory
## available to the VM from the 512Mb default. How much you can allocate depends on mow much physical memory is available.
##
## You have now set up a new virtual machine but it has no operating system installed yet.
##
## 2. Install LAPP
## You should get a LAPP 'appliance' from turnKey Linux (http://www.turnkeylinux.org/lapp). An appliance is the stack
## components pre-configured to work well together. You could build the stack yourself but this approach is better.
## Download the latest ISO image. You can, as an alternative, deploy easily to the Amazon EC2 cloud if you wish. In our
## example we use the ISO image.
##
## 2.1 In your VM, go to Settings>Storage and attach (mount) the ISO CD/DVD controller (the CD icon).This is the virtual
## equivalent of placing a DVD in a drive.
## 2.2 Start the VM.
## 2.3 Choose the following settings during the install process
## 2.3.1 Partitioning method: Guided - use entire disk
## 2.3.2 Wrtie changes to disks: Yes
## 2.3.3 install the GRUB boot loader... : Yes
## 2.3.4 Restart?: Yes
## 2.3.5 Ceate a password for the Root and postgres accounts.
## 2.3.6 Turnkey backup and migration ... : Skip
## 2.3.7 Security Updates: Skip
##
## You have now installed and configured LAPP. depending on your environment, you might want to assign a static IP
## address to your host-only adapter (useful if you intend to run more than one VM).The NAT IP address will be 10.0.2.15.
## The others will more than likely start with 192.168 or 192.168.56 (host-only). The 192.168 address is the IP you'll
## use to access the VM.
##
## 3. Run this script.
## To run this you need to upload it and give it execute permissions.
## 3.1 Point a browser at the 192 address, give prmission to access this untrusted site and go to webmin.
## 3.2 Login as root and go to Tools>Upload and Download>Upload to server.
## 3.3 Upload this script to /root.  [2]
## 3.4 Logout and login again from webshell in the main menu.
## 3.5 Give the script execute permissions using chmod e.g chmod +x makeLAPP4
## 3.6 Run the script by entering ./makeLAPP4. Note the preceeding './'..
## 3.7 Choose the following options
## 3.7.1 Restart servcies during package upgrades : Yes
## 3.7.2 Select language files - suggest en, en_GB, en_GB.UTF-8
## 3.7.3 Modified file...: Keep local...
## 3.7.4 Set time zone data
##
## ----------------
## You're Done!
## ----------------
##
## [1] Or any language starting with P - Python, Perl etc.
## [2] You should craete an 'ordinary' user for normal use. Logging in as root is not good practice. It's OK to get you
## started but is inappropirate for normal use.

echo "**";
echo "** Bash script to download/install/congigure PostGIS and Geoserver on a pre-existing LAPP stack.";
echo "** Assume LAPP stack from Turnkey Linux: -- http://www.turnkeylinux.org/lapp -- version 13.0";
echo "**";
echo "** Mark Foley, October 2011.  Amended November 2013.";
echo "**";

# Check that script run as root 
if ! [ $UID = 0 ]; then
	echo "**";
	echo "** This script should be run as root. Exiting now.";
	echo "**";
	exit 1;
fi

echo "**";
echo "** Using ... ".$(psql -V);
echo "** Check the script to ensure that you are installing the correct versions of PostGIS and Geoserver";
echo "** This script assumes PostgreSQL 9.x, Geoserver 2.x and Tomcat 7";
echo "**";

echo "**";
echo "** 1. Install required packages";
echo "**";

apt-get -y update && apt-get -y upgrade		# Make sure that you have an up-to-date sources list and 
						# upgrade to latest versions of everything.

echo "**";
echo "** 2. Build PostGIS 2.1 from source";
echo "**";

## apt-get -y install postgresql-8.4-postgis	# Install appropriate version of PostGIS.
## This will be upodated when PostGIS 2.x in Debian/Ubuntu repositories. Meanwhile, build from source.

apt-get -y install build-essential postgresql-9.1 postgresql-server-dev-9.1 libxml2-dev libproj-dev libjson0-dev libgeos-dev xsltproc docbook-xsl docbook-mathml
apt-get -y install libgdal-dev

wget http://download.osgeo.org/postgis/source/postgis-2.1.1.tar.gz
tar xfz postgis-2.1.1.tar.gz
cd postgis-2.1.1
# PostGIS 2.x can be configured to disable topology or raster extensions, 
# using the configure flags --without-raster and --without-topology. 
# The default is to build both extensions
./configure
make
make install
ldconfig
make comments-install
cd ~
#  Enable the command-line tools to work from your shell
ln -sf /usr/share/postgresql-common/pg_wrapper /usr/local/bin/shp2pgsql
ln -sf /usr/share/postgresql-common/pg_wrapper /usr/local/bin/pgsql2shp
ln -sf /usr/share/postgresql-common/pg_wrapper /usr/local/bin/raster2pgsql

echo "**";
echo "** 3. Download and install Geoserver";
echo "**";

apt-get -y install tomcat7			# Servlet container to run Geoserver as it's written in Java

# wget http://sourceforge.net/projects/geoserver/files/GeoServer/2.4.1/geoserver-2.4.1-war.zip
wget http://sourceforge.net/projects/geoserver/files/GeoServer/2.5.2/geoserver-2.5.2-war.zip
#unzip geoserver-2.4.1-war.zip 
unzip geoserver-2.5.2-war.zip
cp -v geoserver.war /var/lib/tomcat7/webapps/
 
echo "**";
echo "** 4. Clear up any unnecessary rubbish left behind";
echo "**";

apt-get -y update && apt-get -y upgrade && apt-get -y autoremove && apt-get -y autoclean 

echo "**";
echo "** 5. Check that date/time/timezone are set correctly";
echo "**";

dpkg-reconfigure tzdata

echo "**";
echo "** 6. Finished";
echo "**";

