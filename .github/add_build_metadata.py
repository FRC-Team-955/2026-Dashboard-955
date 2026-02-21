from subprocess import run

build_metadata = run(
    ["git", "log", '-1', '--format=%as %s'],
    capture_output=True,
    check=True,
    text=True,
).stdout.strip()
print(f"Build metadata: {build_metadata}")

with open("lib/services/app_distributor.dart", "r") as f:
    content = f.read()

with open("lib/services/app_distributor.dart", "w") as f:
    f.write(content.replace("Not built from CI", build_metadata))
