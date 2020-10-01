# Examples
This slide is a dump of examples of different stego-tools that might be useful in a CTF.

## Extracting meta data using exiftool
 `exiftool image.jpg`
 `exiftool sound.wav`
 
## stegextract
Extracting hidden files and strings
### installation
```
sudo curl https://raw.githubusercontent.com/evyatarmeged/stegextract/master/stegextract > /usr/local/bin/stegextract
sudo chmod +x /usr/local/bin/stegextract
```
### extracting data
all output:
```
stegextract simple.gif --output out
unzip out
```
extract strings:

`stegextract image.jpg --strings`

### extracting thumbnails
If you have an image where the data you need is covered, try viewing the thumbnail.

`exiftool -b -ThumbnailImage my_image.jpg > my_thumbnail.jpg`

## stegcracker
Brute-force files using steghide
### installation
```
sudo apt-get install steghide -y
pip install stegcracker
```

### usage
```
stegcracker <file>
stegcracker <file> [<wordlist>]
```

### example
```
stegcracker image.jpg
stegcracker image.jpg rockyou.txt
```

## Secret Sauce
```docker run -it --rm -v "$(pwd):/data" dominicbreuker/stego-toolkit /bin/bash```