from remote_api import env,cd,run
from private import user, password

env.host_string = 'localhost'
env.user = "codio"
env.password = ""

setup = "source .bash_profile;"

def setup_django():
    with cd("~"):
        result = run(setup + "pip3 install django")
    with cd("~"):
        result = run(setup + "pip3 list | grep Django")
    assert(result.startswith("Django"))

def setup_application():
    with cd("~/workspace"):
        run(setup + 
            "wget https://github.com/hjwp/book-example/archive/chapter_07.zip")
        run(setup + "unzip chapter_07.zip")
        run("mv book-example-chapter_07 application")
    with cd("~/workspace/application"):
        run(setup + "python3 manage.py migrate")
        
def start_application():
    with cd("~/workspace/application"):
        #run(setup + "nohup python3 manage.py runserver 0.0.0.0:3000 &")
        #run(setup + "nohup ps -aux \&")
        pass
    
if __name__ == "__main__":
    #setup_django()
    #setup_application()
    start_application()
