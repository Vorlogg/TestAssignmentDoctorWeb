import subprocess
import re

text = subprocess.check_output("driverquery /nh /fo csv ", encoding='cp866')
text = text.split("\n")
output = []
for line in text:
    driver = re.sub("[\"]", "", line)
    driver = re.sub(",", " ", driver)
    driver = driver.rstrip() + "\n"
    output.append(driver)

with open("result.txt", "w", encoding='utf-8') as file:
    for driver in output:
        file.write(driver)

with open("result.txt", "r", encoding='utf-8') as file:
    for line in file:
        if line.find("File System") != -1:
            print(line.rstrip())
