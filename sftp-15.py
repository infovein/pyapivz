#!/usr/bin/python3

import paramiko

def commandtoissue(sshsession, command_to_issue):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

## shortcut to gathering targets

def gettargets():
    targetlist = []
    targetip = input("IP Address to connect to: ")
    targetlist.append(targetip)
    targetuser = input("username: ")
    targetlist.append(targetuser)
    return targetlist

def main():
    connectionlist = []
    while True:
        connectionlist.append(gettargets())
        zvarquit = input("Do you want to continue? y/N: ")
        if zvarquit.lower() =='n' or zvarquit == "":
            break

    reqfile = input("Path to Requirements file?: ")
    if reqfile == "":
        reqfile = "requirements.txt"

    sshsession = paramiko.SSHClient()
    
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connectionlist example = [["ipaddress", "user1"]["ipaddress2", ""user2"]]

    for x in range(len(connectionlist)):
        sshsession.connect(hostname=connectionlist[x][0], username=connectionlist[x][1], pkey=mykey)
        ftp_client=sshsession.open_sftp()
        ftp_client.put(reqfile,reqfile)

        print(commandtoissue(sshsession, "ls"))
        ftp_client.close()
        commandtoissue(sshsession, "sudo apt-get update -y")
        commandtoissue(sshsession, "sudo apt install python3-pip -y")
        commandtoissue(sshsession, "python3 -m pip install -r " + reqfile)

        sshsession.close()


if __name__ == "__main__":
    main()

