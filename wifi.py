## sudo iwlist wlan0 scan |egrep "Cell|ESSID|Signal|Rates"
## command for finding data

import subprocess
output = subprocess.run('sudo iwlist wlan0 scan |egrep "Cell|ESSID|Signal|Rates"', shell=True, stdout=subprocess.PIPE, 
                        universal_newlines=True)
print(output.stdout)
