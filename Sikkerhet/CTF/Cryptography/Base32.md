# Base32

Base32 uses a 32-character set comprising the twenty-six upper-case letters A–Z, and the digits 2–7.

## Examples

```
Plain:      Ibsens ripsbærbusker og andre buskevekster
Cipher:     JFRHGZLOOMQHE2LQONRMHJTSMJ2XG23FOIQG6ZZAMFXGI4TFEBRHK43LMV3GK23TORSXE===
```

## How to recognize

Only uses uppercase-letters. Uses = as padding.

## Encrypting base32 in python

```
import base64
base64.b32encode(str.encode("STRING")).decode("utf-8")
```

## Decrypting base32 in python
```
import base64
base64.b32decode("STRING")
```

