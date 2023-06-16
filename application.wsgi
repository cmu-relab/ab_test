#!/usr/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/study5_ab_test/')
from application import app as application
application.secret_key = 'bfb4bf26172efcaa4c964def619297d841361edfb19f4980'
