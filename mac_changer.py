#!usr/bin/env python3

import subprocess

from sqlalchemy import true

subprocess.call("ifconfig", shell=true)

