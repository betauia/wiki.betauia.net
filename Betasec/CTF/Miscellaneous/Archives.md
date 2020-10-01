# archives
Examples of extracting different fileformats.
## rar


`unrar -e archive.rar`

## zip

`unzip archive.zip`

### crack file:
`fcrackzip -v -D -u -p wordlist.txt archive.zip`

>*-v=verbose;-D=dictionary;-u=decompress if false positive;*

>*replace wordlist.txt with any wordslist e.g. rockyou.txt*

## XZ


`unxz archive.xz`

## bzip2


`bunzip2 archive.bz2`

## tar


`tar xzvf archive.tar`

## 7-zip


`7z e archive.7z`