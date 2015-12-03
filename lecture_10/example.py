from remote_api import env,cd,run
from private import user, password

env.host_string = 'ssh.pythonanywhere.com'
env.user = user
env.password = password

with cd(""):
    print(run("ls -l | grep READ"))
