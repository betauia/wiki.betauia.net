
#### extracting meta data using exiftool
 `exiftool image.jpg`
 `exiftool sound.wav`
 
 #### extract hidden data
 ##### extracting hidden files and strings using stegextract
 ###### installation
 ```
 sudo curl https://raw.githubusercontent.com/evyatarmeged/stegextract/master/stegextract > /usr/local/bin/stegextract
 sudo chmod +x /usr/local/bin/stegextract
 ```
 ###### extracting data
 all output:
 ```
 stegextract simple.gif --output out
 unzip out
 ```
 extract strings:
 
 `stegextract image.jpg --strings`
 
 ###### extracting thumbnails
 If you have an image where the data you need is covered, try viewing the thumbnail.
 
 `exiftool -b -ThumbnailImage my_image.jpg > my_thumbnail.jpg`
 
 #### extract hidden encryted data
 ##### brute-force files using stegcracker
 ###### installation
 ```
 sudo apt-get install steghide -y
 pip install stegcracker
 ```
 
 ###### usage
 ```
stegcracker <file>
stegcracker <file> [<wordlist>]
 ```
 
 ###### example
 ```
 stegcracker image.jpg
 stegcracker image.jpg rockyou.txt
 ```