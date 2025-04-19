from binnacle import *

#mode 3: docker
command_mode("docker")
command_container("server1")

# Check if report is generated or a file exists in a container
command_run("echo 'Hello World!' > /root/reports.txt")
command_run("stat /root/reports.txt") #report exixts
command_run("stat /root/reports1.txt 2>/dev/null && echo 'File exists' || echo 'File does not exist'") #report1 does not exixt

