# RSA

> "The art of breaking what should not be broken"

### Using atuomated tools:
`python RsaCtfTool.py -n 14303657909586312103 -e 65537 --private > private.key`


### Get exponent and modulus given a public key (reverse-engineer public key)
>https://m0x39.blogspot.com/2012/12/0x00-introduction-this-post-is-going-to.html
>https://github.com/Ganapati/RsaCtfTool
>
`openssl rsa -pubin -inform PEM -text -noout -in public.key`
`openssl rsa -pubin -inform PEM -text -noout -in public.key | awk '/Modulus:/{f=1;next} /Exponent/{f=0} f'`
`openssl rsa -pubin -inform PEM -text -noout -in public.key | awk '/Modulus:/{f=1;next} /Exponent/{f=0} f' | tr -d : | tr -d '\n' | tr -d ' '`
PUBKEY=`grep -v -- ----- public.key | tr -d '\n'`
### look into the ASN.1 structure:
`echo $PUBKEY | base64 -d | openssl asn1parse -inform DER -i`
The modulus and public exponent are in the last BIT STRING, offset 19, so use -strparse:
`echo $PUBKEY | base64 -d | openssl asn1parse -inform DER -i -strparse 19`
This will give you the modulus and the public exponent, in hexadecimal (the two INTEGERs)
convert hex to integer by opening python interactive
enter hex with : and newline removed, prepend 0x
remove last index (L)
check factordb.com
if status == FF then factorization (n) is found (p * q = modulus)
download rsa cracking tool:
>https://raw.githubusercontent.com/ius/rsatool/master/rsatool.py

`pythonm rsa.py -p P_VALUE -q Q_VALUE -n N_VALUE -e EXPONENT_VALUE -o private.key`
>https://github.com/adeptex/rsatool.git

decrypt encrypted file with private key:
`openssl rsautl -inkey private.key -decrypt -in secret.enc`