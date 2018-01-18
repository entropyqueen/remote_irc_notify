#!/bin/bash
##
## CERTIFICATION AUTHORITY
##

# generate the CA
echo "Creating CA certificate: "
openssl req -new -x509 -days 365 -extensions v3_ca -keyout ca.key -out ca.crt
echo "CA creation done."

##
## SERVER SIDE
##

echo "Generating and signing server key:"
# generate the server key without encryption (needed for easier implem)
# TODO: check if we can add key encryption
openssl genrsa -out server.key 2048

# generate the CSR
openssl req -out server.csr -key server.key -new

# Signe the server key with the CA
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365

echo "Server key created and signed."


echo "All good! :)"
