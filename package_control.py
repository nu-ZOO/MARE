import subprocess

# This was taken to create a better environment .yaml for MULE
# with specific versions, as declared by my local repository

def get_explicit_packages():
    # Get explicitly installed packages (without versions)
    history_cmd = ["conda", "env", "export", "--from-history"]
    history_output = subprocess.run(history_cmd, capture_output=True, text=True).stdout
    explicit_packages = set()
    for line in history_output.splitlines():
        if line.strip().startswith("-"):
            explicit_packages.add(line.split("-")[-1].strip())

    # Get installed packages with versions
    list_cmd = ["conda", "list"]
    list_output = subprocess.run(list_cmd, capture_output=True, text=True).stdout
    package_versions = {}
    for line in list_output.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0] in explicit_packages:
            package_versions[parts[0]] = parts[1]

    return package_versions

if __name__ == "__main__":
    explicit_with_versions = get_explicit_packages()
    for pkg, version in explicit_with_versions.items():
        print(f"{pkg}=={version}")

