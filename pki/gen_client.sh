#!/bin/bash

##
## CLIENT SIDE
##
echo "Generating and signing a client key:"
# Generate client key without encryption
openssl genrsa -out client.key 2048

# generate CSR
openssl req -out client.csr -key client.key -new

# sign client key with CA
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365

