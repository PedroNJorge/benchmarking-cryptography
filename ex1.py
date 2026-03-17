import os
sizes = [8, 64, 512, 4096, 32768, 262144, 2097152]
for size in sizes:
    with open(f"file_{size}.txt", "wb") as f:
        f.write(os.urandom(size))