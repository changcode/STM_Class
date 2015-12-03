from remote_api import env,cd,run
from private import user, password

env.host_string = 'localhost'
env.user = "codio"
env.password = ""

with cd("~/workspace"):
    print(run("ls -l"))