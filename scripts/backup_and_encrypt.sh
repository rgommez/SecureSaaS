#!/bin/bash
DATE=$(date +%F)
tar -czf /tmp/secure-backup-$DATE.tar.gz backend
gpg --symmetric --cipher-algo AES256 /tmp/secure-backup-$DATE.tar.gz
