# Base64
Base64 is a generic term for a number of similar encoding schemes that encode binary data by treating it numerically and translating it into a base 64 representation.

## Examples
`Man is distinguished, not only by his reason, but ...`
represented as an ASCII byte sequence is encoded in MIME's Base64 scheme as follows:
`TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCAuLi4=`

## How to recognize
Uses a mix of upper- and lowercase letters. The total length always need to be divisible by four, so padding is sometimes added: uses equals symbol: =

## Decrypting base64 string in bash
`echo "QkVUQUNURntOT19ET05UX1VTRV9CQVNFNjRfSU5fUFJPRH0=" | base64 -d`

## Encrypting base64 string in bash
`echo "BETACTF{NO_DONT_USE_BASE64_IN_PROD}" | base64`

## Misc
Determine the correct and original Base64 encoding from lowercased base64: [flattened-base64-recovery.py](../Cryptography/flattened-base64-recovery.py)
