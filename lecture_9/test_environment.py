from remote_api import env, cd, run
import private
import unittest

env.host_string = 'ssh.pythonanywhere.com'
env.user = private.user
env.password = private.password

class Test_000_Calculator(unittest.TestCase):

    def test_000_python3(self):
        result = run("python3 --version")
        self.assertTrue("3.4" in result)
    
    def test_002_directories(self):
        with cd("~"):
            result = run('ls')
            self.assertTrue("sites" in result.split())
        with cd("~/sites"):
            result = run('ls')
            self.assertTrue("todo.gdelo.com" in result.split())

    def test_003_directory_pemission(self):
        with cd("~/sites"):
            result = run("ls -l")
            results = result.split("\n")
            for result in results:
                if "todo.gdelo.com" in result:
                    self.assertTrue("drwxrwxr-x" in result)
                    
if __name__ == "__main__":
    unittest.main()
