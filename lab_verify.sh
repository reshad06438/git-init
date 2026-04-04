#!/bin/bash
hostname -I > setup_verify.txt
git --version >> setup_verify.txt
python3 --version >> setup_verify.txt
