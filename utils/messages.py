import os

def with_fill(message='', length=None, fill_char='='):
	if length is None:
		_, length = os.get_terminal_size()
	return message.center(length, fill_char)
