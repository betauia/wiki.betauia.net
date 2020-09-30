# stegextract (extract hidden files and strings from images)
* installation:
```bash
sudo curl https://raw.githubusercontent.com/evyatarmeged/stegextract/master/stegextract > /usr/local/bin/stegextract
sudo chmod +x /usr/local/bin/stegextract
```
* extract hidden files and strings from images

```bash
stegextract simple.gif --output out
unzip out
cat secret.txt
stegextract complex.jpg --analyze --strings
```