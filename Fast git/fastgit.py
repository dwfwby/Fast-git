import sublime, sublime_plugin, os, subprocess, inspect


def plugin_loaded():
	FastGitState.script_folder = os.path.dirname(os.path.abspath(__file__));
	FastGitState.batch_folder = os.path.join(FastGitState.script_folder,"batch")
	FastGitState.token_file = os.path.join(FastGitState.script_folder,"secret_token")


def get_secret_token():
	f = open(FastGitState.token_file, "a+")
	f.seek(0)
	data = f.readlines();
	if not data:
		print("Info: token not found")
	else:
		return data[0].strip()


def set_secret_token(token):
	f = open(FastGitState.token_file, "a+")
	f.seek(0)
	f.truncate()
	f.write(token)
		
		


def get_remote_repo(repo_folder):
	bat_path = os.path.join(FastGitState.batch_folder,"get_RemoteURL.bat")
	remote_url = subprocess.Popen([bat_path,repo_folder], stdout=subprocess.PIPE).communicate()[0].decode('UTF-8').strip()
	if not remote_url:
		return
	else:
		return remote_url

def set_remote_repo(remote_url, repo_folder):
	bat_path = os.path.join(FastGitState.batch_folder,"set_RemoteURL.bat")
	remote_url = subprocess.Popen([bat_path,repo_folder,remote_url])


class InputPanel:
	caption = set()
	initial_text = set()
	on_done = set()
	on_cancel = set()
	on_change = set()

class FastGitState:
	clone_link = set();
	batch_folder = set()
	script_folder = set()
	token_file = set()


class FastGitSetRemote(sublime_plugin.ApplicationCommand):
	def is_visible(self, index):
		if not self.description(index):
			return False
		else:
			return True

	def description(self, index):
		self.open_folders = sublime.active_window().folders()
		if len(self.open_folders) >= int(index)+1:
			return self.open_folders[index]

	def run(self, index):
		self.description(index)
		if len(self.open_folders) <= index:
			return
		input_p = InputPanel();
		input_p.caption = "New remote url: "
		def on_done(val, repo_folder = self.open_folders[index]):
			set_remote_repo(val, repo_folder)
		input_p.on_done = on_done; input_p.on_cancel = ""; input_p.on_change = ""; input_p.initial_text = "";
		sublime.active_window().show_input_panel(**input_p.__dict__)


class FastGitSetToken(sublime_plugin.ApplicationCommand):
	def run(self):
		input_p = InputPanel();
		input_p.caption = "Your token: "
		def on_done(val):
			set_secret_token(val)
		input_p.on_done = on_done; input_p.on_cancel = ""; input_p.on_change = ""; input_p.initial_text = "";
		sublime.active_window().show_input_panel(**input_p.__dict__)


class FastGitUpdate(sublime_plugin.ApplicationCommand):
	def is_visible(self, index):
		if not self.description(index):
			return False
		else:
			return True

	def description(self, index):
		self.open_folders = sublime.active_window().folders()
		if len(self.open_folders) > int(index):
			return self.open_folders[index]

	def run(self, index):
		self.description(index)
		token = get_secret_token()
		if (not token) or (len(self.open_folders) <= index):
			return
		repo_folder = self.open_folders[index]
		repository_link = get_remote_repo(repo_folder).replace("https://github.com/","https://"+token+":x-oauth-basic@github.com/");
		bat_path = os.path.join(FastGitState.batch_folder,"update.bat")
		subprocess.Popen([bat_path,repo_folder,repository_link])


class FastGitClone(sublime_plugin.ApplicationCommand):
	def is_visible(self, index):
		if not self.description(index):
			return False
		else:
			return True

	def description(self, index):
		self.open_folders = sublime.active_window().folders()
		if len(self.open_folders) >= int(index)+1:
			return self.open_folders[index]

	def run(self, index):
		self.description(index)
		if len(self.open_folders) <= index:
			return
		input_p = InputPanel();
		input_p.caption = "Clone repository link: "
		def on_done(val, repo_folder = self.open_folders[index], bat_path = os.path.join(FastGitState.batch_folder,"clone.bat")):
			subprocess.Popen([bat_path,repo_folder,val])
		input_p.on_done = on_done; input_p.on_cancel = ""; input_p.on_change = ""; input_p.initial_text = "";
		sublime.active_window().show_input_panel(**input_p.__dict__)



class FastGitCreate(sublime_plugin.ApplicationCommand):
	def is_visible(self, index):
		if not self.description(index):
			return False
		else:
			return True

	def description(self, index):
		self.open_folders = sublime.active_window().folders()
		if len(self.open_folders) >= int(index)+1:
			return self.open_folders[index]

	def run(self, index):
		self.description(index)
		token = get_secret_token()
		if (not token) or (len(self.open_folders) <= index):
			return
		repo_folder = self.open_folders[index]
		repo_name = repo_folder.split("\\")[-1]
		bat_path = os.path.join(FastGitState.batch_folder,"create.bat")
		repo_url = subprocess.Popen([bat_path,repo_name], stdout=subprocess.PIPE).communicate()[0].decode('UTF-8').strip()
		if repo_url:
			set_remote_repo(repo_url, repo_folder)
