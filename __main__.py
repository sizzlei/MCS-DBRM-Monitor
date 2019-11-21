import paramiko
import runTelegram

# Configure
alertTg = runTelegram.botTelegram('', '')

# OAM INFO
_svrip = ''
_svruser = ''
_svrport = 22
_mcspath = ''
_mcshostnm = ""
## SSH
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(_svrip, username=_svruser, port=_svrport, timeout=10)
    _dbrmcheck = '%s/bin/dbrmctl status' % _mcspath
    stdin, stdout, stderr = ssh.exec_command(_dbrmcheck)
    _sshdata = stdout.readlines()
except Exception as ssherr:
    alertTg.Send(ssherr)
finally:
    ssh.close()

# Checker
if _sshdata[0] == 'OK.\n':
    pass
else:
    alertTg.Send(_mcshostnm + " : " + _sshdata[0])