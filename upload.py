import os

os.system("scp -r -i /home/pi/.ssh/fileserver.pem /home/pi/speed-camera/media/images/speed-20180204-1558/* root@ec2-54-185-58-144.us-west-2.compute.amazonaws.com:/home/bitnami/stack/apps/owncloud/data/user/files/Photos")

os.system("rm -rf /home/pi/speed-camera/media/images/speed-20180204-1558/*")

os.system("ssh -i /home/pi/.ssh/fileserver.pem root@ec2-54-185-58-144.us-west-2.compute.amazonaws.com /home/bitnami/rescan.sh")
