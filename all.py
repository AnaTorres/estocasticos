import subprocess

subprocess.Popen("python actioner.py", shell=True)
subprocess.Popen("python listener.py", shell=True)
