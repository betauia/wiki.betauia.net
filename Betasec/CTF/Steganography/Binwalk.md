# Binwalk (Any File)

## Installation (Mac, Linux, Windows)
* Debian/ Ubuntu
    * apt install binwalk
* Arch
    * pacman -Ss binwalk
* Windows
    *


## Usage
```bash
binwalk door.jpg
```

* Exctract all files from a file format
```bash
binwalk --dd='.*' door.jpg
```