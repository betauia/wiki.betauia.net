# Imagemagick (Images)


## Installation (Mac, Linux, Windows)
* Debian/ Ubuntu
    * apt install imagemagick
* Arch
    * pacman -Ss imagemagick
* Windows
    * ????


## Usage
* Extract frames from gif:
```bash
convert image.gid %02d.png
```

* Replace white with transperency in image:
```bash
convert image.png -transparent white result.png
```
* Multiple images:
```bash
ls *.png | while read filename; do convert $filename -transparent white $filename; done
```
* Overlay images/stack:
```bash
ls *.png | while read filename; do convert $filename 00.png -gravity center -composite 00.png; done
```