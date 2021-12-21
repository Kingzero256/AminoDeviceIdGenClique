from time import time
from requests import get
from pyfiglet import figlet_format
from concurrent.futures import ThreadPoolExecutor
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(figlet_format("aminodeviceIdgenclique", font="graffiti", width=80))
device_Ids = open("deviceids.txt", "a")

# request link is from https://github.com/Alert-Aigul/Amino.ed
def device_Id_generator():
    try:
        device_Id = get(
            f"https://ed-server.herokuapp.com/api/generator/ndcdeviceid?data={time()}"
        ).json()["message"]
        print(f"device_Id: {device_Id}")
        device_Ids.write(f"{device_Id}\n")
    except BaseException:
        return

while True:
    with ThreadPoolExecutor(max_workers=100) as executor:
        _ = [executor.submit(device_Id_generator) for _ in range(500)]
