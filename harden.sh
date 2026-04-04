#!/bin/bash

echo "Starting system hardening..."

echo "Securing Vault directory..."
chmod 700 ~/Vault
chown $USER:$USER ~/Vault

echo "Auditing /etc/shadow..."
ls -l /etc/shadow

echo "Fixing ownership of /etc/shadow..."
sudo chown root:shadow /etc/shadow

echo "Fixing permissions of /etc/shadow..."
sudo chmod 640 /etc/shadow

echo "Verifying changes..."
ls -l /etc/shadow

echo "Hardening complete."


