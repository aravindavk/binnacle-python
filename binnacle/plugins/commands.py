import subprocess

from binnacle.core import binnacle_task


def escaped_cmd(cmd):
    return cmd.replace("'", """'"'"'""")


def escaped_ssh_cmd(cmd):
    cmd = f"/bin/bash -c '{escaped_cmd(cmd)}'"
    cmd = f"sudo {cmd}" if _command_config.sudo else cmd

    return escaped_cmd(cmd)


def full_cmd(cmd):
    if _command_config.mode in ["", "local"] or _command_config.node in ["", "local"]:
        return cmd
    
    if _command_config.mode == "ssh":
        return f"""ssh {_command_config.ssh_user}@{_command_config.node} \
        -i {_command_config.ssh_pem_file} -p {_command_config.ssh_port}  \
        '{escaped_ssh_cmd(cmd)}'
        """ 

    elif _command_config.mode == 'docker':
        return f"""docker exec -i {_command_config.node} /bin/bash -c '{escaped_cmd(cmd)}'"""

    return cmd


@binnacle_task
def command_run(cmd, ret = 0, task=None):
    cmd = full_cmd(cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True, universal_newlines=True)
    task.ok = result.returncode == ret
    if not task.ok:
        task.info(f"Return code: {result.returncode}\n" + result.stderr.strip())
    return result.stdout


class CommandConfig:
    def __init__(self):
        self.node = ""
        self.mode = ""
        self.ssh_user = "root"
        self.ssh_pem_file = ""
        self.ssh_port = ""


_command_config = CommandConfig()


def command_node(name):
    _command_config.node = name


def command_container(name):
    _command_config.node = name


def command_mode(name):
    _command_config.mode = name


def command_ssh_user(name):
    _command_config.ssh_user = name
    
def command_ssh_sudo(name):
    _command_config.sudo = name

def command_ssh_pem_file(name):
    _command_config.ssh_pem_file = name

def command_port(name):
    _command_config.ssh_port = name
    
