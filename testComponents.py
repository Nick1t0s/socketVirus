def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    b = bytes(result.stdout+result.stderr, "cp866")#cp1251
    s = str(b, "cp866")
    return s
import subprocess
print(run_command("ls -l"))