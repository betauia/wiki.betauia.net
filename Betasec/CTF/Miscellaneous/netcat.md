# netcat
echo remote server:
`echo "ffffffff" | nc 192.168.1.32 12345`
use with cat and/or sleep if no response:
`(sleep 1; echo "fffffff"; cat) | nc 192.168.1.32 12345`
echo own server (prints when a client connects):
`echo "fffffff" | nc -lvvp 8080`

* setup server:
```bash
nc -nvlp 1234
```

* setup client:
```bash
nc -nv 192.168.1.10 1234
```
* save any incoming file/input:
```bash
nc -nvlp 1234 > data.txt/sh
```