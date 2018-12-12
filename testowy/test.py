import subprocess

bashCommand = " ls /usr/bin/w /bin/ps"

#bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"


process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print(process)



