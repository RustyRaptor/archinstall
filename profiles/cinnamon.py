# A desktop environment using "Cinnamon"
import archinstall

is_top_level_profile = False

def _prep_function(*args, **kwargs):
	"""
	Magic function called by the importing installer
	before continuing any further. It also avoids executing any
	other code in this stage. So it's a safe way to ask the user
	for more input before any other installer steps start.
	"""

	# Cinnamon requires a functioning Xorg installation.
	profile = archinstall.Profile(None, 'xorg')
	with profile.load_instructions(namespace='xorg.py') as imported:
		if hasattr(imported, '_prep_function'):
			return imported._prep_function()
		else:
			print('Deprecated (??): xorg profile has no _prep_function() anymore')

# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("cinnamon", "/somewhere/cinnamon.py")
# or through conventional import cinnamon
if __name__ == 'cinnamon':
	# Install dependency profiles
	installation.install_profile('xorg')

	# Install the application cinnamon from the template under /applications/
	cinnamon = archinstall.Application(installation, 'cinnamon')
	cinnamon.install()

	installation.enable_service('lightdm') # Light Display Manager
