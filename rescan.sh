#!/bin/bash

chown -R daemon:daemon /home/bitnami/stack/apps/owncloud/data/user/files/Photos
sudo -u daemon php /opt/bitnami/apps/owncloud/htdocs/occ files:scan user
