from remote_api import env,cd,run
from private import user, password

env.host_string = 'ssh.pythonanywhere.com'
env.user = "drdelozier"
env.password = password

setup = "source .bash_profile;"

import unittest

class Test_000_Environment(unittest.TestCase):

    def test_000_login(self):
        "Server is present and we can log in."
        with cd("~/workspace"):
            result = run("whoami")
        self.assertTrue(env.user in result)

    def test_001_python3(self):
        "Python 3 is installed."
        with cd("~"):
            result = run(setup + "python3 --version")
        self.assertTrue("Python 3" in result)

    def test_002_pip3(self):
        "Pip3 is installed."
        with cd("~"):
            result = run(setup + "pip3 --version")
        self.assertTrue(result.startswith("pip"))
        
    def test_003_git(self):
        "git is installed."
        with cd("~"):
            result = run(setup + "git --version")
        self.assertTrue(result.startswith("git"))
        
    def test_004_django(self):
        "Django is installed."
        with cd("~"):
            result = run(setup + "pip3 list | grep Django")
        self.assertTrue(result.startswith("Django"))
    
    def test_005_app_installed(self):
        "Test that the application directory and software are present"
        with cd("~/workspace"):
            result = run("ls -l")
        self.assertTrue("application" in result)
        with cd("~/workspace/application"):
            result = run("ls -l")
        self.assertTrue("manage.py" in result)
        self.assertTrue("lists" in result)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)