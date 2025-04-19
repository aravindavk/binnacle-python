from binnacle import *

#mode2: ssh
command_mode("ssh")
command_node("192.168.29.65")
command_ssh_user("test1")
command_ssh_sudo(False) 
command_ssh_pem_file("~/.ssh/id_rsa")
command_port("22")

# All the future command_run will be executed as ssh command
# unless command_node("local")
command_run("cat /tmp/hello")
show_summary()


