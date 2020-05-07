import os

if 'BSDG_ENV' in os.environ:
	if os.environ['BSDG_ENV'] == 'STAGING':
		from . staging import *
	else:
		from . production import *
else:
	from . local import *
