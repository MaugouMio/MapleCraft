# -*- coding: UTF-8 -*-
import sys, os, shutil, configparser, colorama
from io import StringIO
from colorama import Fore, Style
colorama.init()

config_path = os.path.expandvars("%LOCALAPPDATA%\\mcdp")
config = configparser.ConfigParser()
config.read(config_path + "\\mcdp_config.ini", encoding="utf-8")
install_path = config.get("Path", "Install")
module_path = [install_path + "lib\\"]

class Folder:
	def __init__(self):
		self.name = ""
		self.items = dict()
		self.virtual = False
		self.is_namespace = False
		
		self.argv = []
		self.unparsed = []
		
	def copy(self):
		new_folder = Folder()
		for key in self.items.keys():
			new_folder.items[key] = self.items[key].copy()
		new_folder.name = self.name
		new_folder.virtual = self.virtual
		new_folder.argv = list(self.argv)
		new_folder.unparsed = list(self.unparsed)
		# not copying namespace status
		
		return new_folder
		
	def build(self, dir, func_path):
		if not self.is_namespace:
			func_path = func_path + self.name + '/'
			
		if not self.virtual:
			sub_dir = dir + self.name
			os.mkdir(sub_dir)
			if self.is_namespace:
				sub_dir += "\\functions"
				os.mkdir(sub_dir)
			
			for key in self.items.keys():
				self.items[key].build(sub_dir + '\\', func_path)
		
class Function:
	def __init__(self):
		self.name = ""
		self.commands = ""
		self.virtual = False
		
		self.argv = []
		self.unparsed = []

	def copy(self):
		new_function = Function()
		new_function.name = self.name
		new_function.commands = self.commands
		new_function.virtual = self.virtual
		new_function.argv = list(self.argv)
		new_function.unparsed = list(self.unparsed)
		
		return new_function
		
	def build(self, dir, func_path):
		self.commands = self.commands.replace("ARG(_PATH)", func_path)
		if self.commands.find("ARG(__PATH)") >= 0 and max(func_path[:-1].rfind(':'), func_path[:-1].rfind('/')) < 0:
			raise ValueError("ARG(__PATH) not exist\n  %s" %(func_path + self.name))
		self.commands = self.commands.replace("ARG(__PATH)", func_path[:(max(func_path[:-1].rfind(':'), func_path[:-1].rfind('/')) + 1)])
		if not self.virtual:
			with open(dir + self.name + ".mcfunction", "w", encoding="utf-8") as f:
				f.write(self.commands)
		
		

sep_char = [' ', ',']
backslash_char = ['\\', '"']
backslash_sign = {'n':'\n', 't':'\t', 'r':'\r'}

def get_raw_text(string):
	backslash = False
	raw_string = ""
	for i in range(1, len(string)):
		if backslash:
			if string[i] in backslash_char:
				raw_string += string[i]
			elif string[i] in backslash_sign.keys():
				raw_string += backslash_sign[string[i]]
			else:
				raise ValueError("Unknown character '\\%s'\n  %s" % (string[i], string))
			backslash = False
		else:
			if string[i] == '\\':
				backslash = True
			elif string[i] == '"': # end of raw string
				return raw_string, i
			else:
				raw_string += string[i]
				
	raise SyntaxError("EOL while scanning string literal\n  " + string)

def split_by_chars(string, sep = sep_char, local_sign = None, parse_string = False, clear_null = True):
	# local_sign is a string like '()' or '{}'
	splitted = []
	
	in_local = False
	
	first_char = 0
	index = 0
	while index < len(string):
		if in_local:
			if parse_string and string[index] == '"':
				# escape raw string
				raw_string, str_len = get_raw_text(string[index:])
				index += str_len
			elif string[index] == local_sign[1]:
				splitted.append(split_by_chars(string[first_char:index], parse_string = True))
				in_local = False
				first_char = index + 1
			else:
				# ignore all contents
				pass
		elif local_sign != None and string[index] == local_sign[0]:
			in_local = True
			if not (clear_null and index == first_char):
				splitted.append(string[first_char:index])
			first_char = index + 1
		
		elif parse_string and string[index] == '"':
			if not (clear_null and index == first_char):
				splitted.append(string[first_char:index])
			raw_string, str_len = get_raw_text(string[index:])
			splitted.append(raw_string)
			index += str_len
			first_char = index + 1
			
		elif string[index] in sep_char:
			if not (clear_null and index == first_char):
				splitted.append(string[first_char:index])
			first_char = index + 1
		
		index += 1
	
	if in_local:
		raise SyntaxError("EOL while scanning %s...%s literal\n  %s" % (local_sign[0], local_sign[1], string))
	
	if not (clear_null and first_char == len(string)):
		splitted.append(string[first_char:])
	
	return splitted

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def legal_name(name):
	try:
		name.encode("ascii")
	except UnicodeEncodeError:
		raise ValueError("'%s' is not a legal variable name" %name)
	
	for char in name:
		if not (char.isalnum() or char == '_'):
			raise ValueError("'%s' is not a legal variable name" %name)
	
	return name

def folder_copy(root_src_dir, root_dst_dir):
	for src_dir, dirs, files in os.walk(root_src_dir):
		dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
		if not os.path.exists(dst_dir):
			os.makedirs(dst_dir)
		for file_ in files:
			src_file = os.path.join(src_dir, file_)
			dst_file = os.path.join(dst_dir, file_)
			if os.path.exists(dst_file):
				# in case of the src and dst are the same file
				if os.path.samefile(src_file, dst_file):
					continue
				os.remove(dst_file)
			shutil.copy2(src_file, dst_dir)

###########################################
#             tool functions              #
# ======================================= #
#            normal functions             #
###########################################

def find_lib(script_name, search_path):
	for path in search_path:
		# fix directory path
		if path[-1] != '\\' and path[-1] != '/':
			path += '\\'
			
		if os.path.isfile(path + script_name + ".dpl"):
			with open(path + script_name + ".dpl", "r", encoding='UTF-8') as f:
				script = f.read().splitlines()
			return script, path
		elif os.path.isfile(path + script_name + "\\__main__.dpl"):
			with open(path + script_name + "\\__main__.dpl", "r", encoding='UTF-8') as f:
				script = f.read().splitlines()
			return script, path + script_name + '\\'
			
	raise ImportError("No module named '" + script_name + "'")

def parse_code(code):
	old_stdout = sys.stdout
	redirected_output = sys.stdout = StringIO()
	warning_msg = False
	try:
		exec(code, globals())
	except Warning as w:
		warning_msg = w
	sys.stdout = old_stdout
	
	if warning_msg:
		print(f"{Fore.YELLOW}Warning:", warning_msg, f"{Style.RESET_ALL}")
	return redirected_output.getvalue()

def read_block(code, this, namespaces, argv = [], arg_name = []): # 'this' is a Folder() or Function() object
	# copy of code
	code = list(code)
	# replace arguments
	for i in range(len(code)):
		for j in range(len(argv)):
			code[i] = code[i].replace("ARG(%s)" %arg_name[j], argv[j])
	
	# simply parse python code and return function object
	if isinstance(this, Function):
		# parse pycode
		in_pycode = False
		indent = 0
		pycode = ""
		line_index = 0
		while line_index < len(code):
			if in_pycode:
				if code[line_index].lstrip(" \t").rstrip(" \t") == "```":
					parsed_pycode = parse_code(pycode).split('\n')
					for i in range(len(parsed_pycode)):
						code.insert(line_index + 1, parsed_pycode[len(parsed_pycode) - i - 1])
					# reset stats
					del code[line_index]
					in_pycode = False
					indent = 0
					pycode = ""
				else:
					pycode += code[line_index].expandtabs(4)[indent:] + '\n'
					del code[line_index]
					if line_index == len(code):
						raise SyntaxError("EOF while scanning python code literal")
			else:
				if code[line_index].lstrip(" \t").rstrip(" \t") == "```":
					in_pycode = True
					indent = code[line_index].expandtabs(4).find('`')
					del code[line_index]
				else:
					line_index += 1
					
		for l in code:
			this.commands += l.lstrip(" \t").rstrip(" \t") + '\n'
		return this
	
	# read sub blocks in folder object
	in_pycode = False
	indent = 0
	pycode = ""
	
	block_stack = 0
	declare_name = ""
	block_content = []
	this_block = None
	
	line_index = 0
	while line_index < len(code):
		if in_pycode:
			if code[line_index].lstrip(" \t").rstrip(" \t") == "```":
				parsed_pycode = parse_code(pycode).split('\n')
				for i in range(len(parsed_pycode)):
					code.insert(line_index + 1, parsed_pycode[len(parsed_pycode) - i - 1])
				# reset stats
				in_pycode = False
				indent = 0
				pycode = ""
			else:
				pycode += code[line_index].expandtabs(4)[indent:] + '\n'
				if line_index == (len(code) - 1):
					raise SyntaxError("EOF while scanning python code literal")
		else:
			this_line = code[line_index].replace('\t', '')
			# parsing contents by lines
			splitted_line = split_by_chars(this_line)
			# not an empty row or comment
			if len(splitted_line) > 0 and this_line[0] != '#':
				if block_stack > 0:
					end_char = this_line.lstrip().rstrip()
					if end_char == '{':
						block_stack += 1
					elif end_char == '}':
						block_stack -= 1
					
					# copy this line to block_content (without the last '}')
					if block_stack == 0:
						if not this_block.virtual:
							this.items[declare_name] = read_block(block_content, this_block, namespaces)
						else:
							this_block.unparsed = block_content
							this.items[declare_name] = this_block
							
						# reset content
						block_content = []
					else:
						block_content.append(code[line_index])
					
				elif splitted_line[0] == "folder" or splitted_line[0] == "func":
					declare_name, var, end_char = parse_definition(this_line, namespaces)
					
					if end_char == None:
						this_block = var
						block_stack += 1
						
						# preview and ignore the next line
						line_index += 1
						if code[line_index].lstrip(" \t").rstrip(" \t") != '{':
							raise SyntaxError(code[line_index].lstrip(" \t"))
					elif end_char == ';':
						this.items[declare_name] = var
					else:
						raise SyntaxError(this_line)
						
				elif splitted_line[0] == "```":
					in_pycode = True
					indent = code[line_index].expandtabs(4).find('`')
					
				else:
					raise SyntaxError(this_line)
		
		line_index += 1
	
	return this

def parse_definition(line, namespaces):
	argv = []
	is_virtual = False
	end_char = None
	
	line = line.rstrip()
	if line[-1] == ';':
		sep_line = split_by_chars(line[:-1], local_sign = "()", parse_string = True)
		end_char = line[-1]
	elif line[-1] == ')' or line[-1] == 'l':
		sep_line = split_by_chars(line, local_sign = "()", parse_string = True)
	else:
		raise SyntaxError(line)
	
	# parse variable type
	if sep_line[0] == "namespace" or sep_line[0] == "folder":
		folder_var = True
		var = Folder()
	elif sep_line[0] == "func":
		folder_var = False
		var = Function()
	else:
		raise SyntaxError(line)
	
	# parse name and arguments
	declare_name = legal_name(sep_line[1])
	if isinstance(sep_line[2], list):
		for arg in sep_line[2]:
			argv.append(legal_name(arg))
	else:
		raise SyntaxError(line)
	
	# have other contents
	if len(sep_line) > 3:
		if sep_line[3] == "from":
			object_name = ""
			# template namespace
			if isinstance(sep_line[4], str) and isinstance(sep_line[5], list):
				try:
					object_name += sep_line[4]
					template = namespaces[sep_line[4]]
				except KeyError:	
					raise KeyError("object %s not found" %object_name)
				
				if len(template.argv) != len(sep_line[5]):
					raise ValueError("wrong number of arguments passed to " + object_name)
				elif template.virtual:
					template = read_block(template.unparsed, template.copy(), namespaces, sep_line[5], template.argv)
					template.unparsed = []
			else:
				raise SyntaxError(line)
				
			parsing_index = 6
			while parsing_index < len(sep_line):
				# every object should follow up with an argument
				if parsing_index == (len(sep_line) - 1):
					raise SyntaxError(line)
				# virtual setting
				elif sep_line[parsing_index] == "as" and parsing_index == (len(sep_line) - 2):
					if sep_line[parsing_index + 1] == "virtual":
						is_virtual = True
						break
					else:
						raise SyntaxError(line)
				# read sub objects as template
				else:
					if isinstance(sep_line[parsing_index], str) and isinstance(sep_line[parsing_index + 1], list):
						# must use '.' to concatenate sub objects
						if sep_line[parsing_index][0] != '.':
							raise SyntaxError(line)
						
						try:
							object_name += sep_line[parsing_index]
							template = template.items[sep_line[parsing_index][1:]]
						except KeyError:	
							raise KeyError("object %s not found" %object_name)
						
						if len(template.argv) != len(sep_line[parsing_index + 1]):
							raise ValueError("wrong number of arguments passed to " + object_name)
						elif template.virtual:
							template = read_block(template.unparsed, template.copy(), namespaces, sep_line[parsing_index + 1], template.argv)
							template.unparsed = []
					else:
						raise SyntaxError(line)
						
				parsing_index += 2
			
			# inconsistent variable type
			if (folder_var and isinstance(template, Function)) or (not folder_var and isinstance(template, Folder)):
				raise TypeError("type of '%s' is not compatible with '%s'" % (object_name, sep_line[0]))
			
			var = template.copy()
			
		elif sep_line[3] == "as":
			if sep_line[4] == "virtual":
				is_virtual = True
			else:
				raise SyntaxError(line)
		else:
			raise SyntaxError(line)
		
	if len(argv) > 0 and not is_virtual:
		raise ValueError("Arguments can not be assigned to non virtual objects\n  " + line)
	
	var.name = declare_name
	var.virtual = is_virtual
	var.argv = argv
	return declare_name, var, end_char

def add_namespace(name, namespace, namespaces):
	if name in namespaces.keys() and not namespaces[name].virtual:
		raise NameError("namespace '" + name + "' already defined")
	
	namespaces[name] = namespace
	
variable_types = ["namespace", "folder", "func"]
def read_script(script, this_dir, read_as_virtual = False):
	search_path = [this_dir] + module_path
	
	tags = {"tick": [], "load": []}
	namespaces = {}
	description = ""

	block_stack = 0
	declare_name = ""
	block_content = []
	this_block = None
	
	in_pycode = False
	pycode = ""
	
	line_index = 0
	while line_index < len(script):
		# parsing python codes
		if in_pycode:
			if script[line_index].lstrip(" \t").rstrip(" \t") == "```":
				parsed_pycode = parse_code(pycode).split('\n')
				for i in range(len(parsed_pycode)):
					script.insert(line_index + 1, parsed_pycode[len(parsed_pycode) - i - 1])
				# reset stats
				in_pycode = False
				pycode = ""
			else:
				pycode += script[line_index] + '\n'
				if line_index == (len(script) - 1):
					raise SyntaxError("EOF while scanning python code literal")
		else:
			this_line = script[line_index].replace('\t', '')
			# parsing contents by lines
			splitted_line = split_by_chars(this_line)
			# not an empty row or comment
			if len(splitted_line) > 0 and this_line[0] != '#':
				# read block contents
				if block_stack > 0:
					end_char = this_line.lstrip().rstrip()
					if end_char == '{':
						block_stack += 1
					elif end_char == '}':
						block_stack -= 1
					
					# copy this line to block_content (without the last '}')
					if block_stack == 0:
						if not this_block.virtual:
							namespaces[declare_name] = read_block(block_content, this_block, namespaces)
						else:
							this_block.unparsed = block_content
							namespaces[declare_name] = this_block
						
						# reset content
						block_content = []
					else:
						block_content.append(script[line_index])
						
					
					
				# read description
				elif this_line[:11] == "description":
					if this_line[11:].lstrip()[0] == '=':
						description = split_by_chars(this_line[(this_line.find('=') + 1):], parse_string = True)[0]
					else:
						raise SyntaxError(this_line)
				
				
				
				# import module
				elif splitted_line[0] == "import":
					if len(splitted_line) < 2:
						raise SyntaxError(this_line)
						
					virtual_namespace = len(splitted_line) >= 4 and splitted_line[-2] == "as" and splitted_line[-1] == "virtual"
					for i in range(1, len(splitted_line)):
						# 'as' and 'virtual' are not module names
						if virtual_namespace and i == (len(splitted_line) - 2):
							break
						
						imported_script, imported_from = find_lib(splitted_line[i], search_path)
						junk_description, imported, imported_tags = read_script(imported_script, imported_from, virtual_namespace)
						if virtual_namespace:
							# set namespaces as virtual
							for key in imported.keys():
								imported[key].virtual = True
							# ignore tags
							imported_tags = {}
						else:
							# ignore tags of originally virtual namespaces
							imported_namespaces = list(imported.keys())
							ignore_namespaces = []
							for key in imported_namespaces:
								if imported[key].virtual:
									ignore_namespaces.append(key)
							
							for tag_key in imported_tags.keys():
								tag_index = 0
								while tag_index < len(imported_tags[tag_key]):
									if imported_tags[tag_key][tag_index].lstrip('"').rstrip('"').split(':')[0] in ignore_namespaces:
										del imported_tags[tag_key][tag_index]
									else:
										tag_index += 1
						
						# check duplicated namespaces
						# for key in imported.keys():
							# if key in namespaces.keys() and namespaces[key].virtual == False:
								# raise NameError("namespace " + key + " already defined")
						
						namespaces = merge_two_dicts(namespaces, imported)
						# append tags
						for key in imported_tags.keys():
							for tag in imported_tags[key]:
								tags[key].append(tag)
					
					
					
				# from module import namespaces
				elif splitted_line[0] == "from":
					if len(splitted_line) < 4 or splitted_line[2] != "import":
						raise SyntaxError(this_line)
						
					virtual_namespace = splitted_line[-2] == "as" and splitted_line[-1] == "virtual"
					
					imported_script, imported_from = find_lib(splitted_line[1], search_path)
					junk_description, imported, imported_tags = read_script(imported_script, imported_from, virtual_namespace)
					
					# delete unneeded namespaces
					imported_namespaces = list(imported.keys())
					ignore_namespaces = []
					for key in imported_namespaces:
						if virtual_namespace:
							if key not in splitted_line[3:-2]:
								imported.pop(key)
							else:
								# set namespaces as virtual
								imported[key].virtual = True
							ignore_namespaces.append(key)
						else:
							if key not in splitted_line[3:]:
								imported.pop(key)
								ignore_namespaces.append(key)
							else:
								if imported[key].virtual:
									ignore_namespaces.append(key)
								
					# ignore tags of virtual and not imported namespaces
					for tag_key in imported_tags.keys():
						tag_index = 0
						while tag_index < len(imported_tags[tag_key]):
							if imported_tags[tag_key][tag_index].lstrip('"').rstrip('"').split(':')[0] in ignore_namespaces:
								del imported_tags[tag_key][tag_index]
							else:
								tag_index += 1
												
					# check duplicated namespaces
					for key in imported.keys():
						if key in namespaces.keys() and namespaces[key].virtual == False:
							raise NameError("namespace " + key + " already defined")
					
					namespaces = merge_two_dicts(namespaces, imported)
					# append tags
					for key in imported_tags.keys():
						for tag in imported_tags[key]:
							tags[key].append(tag)
					
					
					
				# define a namespace (blocks are separated by {})
				elif splitted_line[0] == "namespace":
					declare_name, var, end_char = parse_definition(this_line, namespaces)
					var.is_namespace = True
					var.virtual = var.virtual or read_as_virtual
					
					if end_char == None:
						this_block = var
						block_stack += 1
						
						# preview and ignore the next line
						line_index += 1
						if script[line_index].lstrip(" \t").rstrip(" \t") != '{':
							raise SyntaxError(script[line_index].lstrip(" \t"))
					elif end_char == ';':
						add_namespace(declare_name, var, namespaces)
					else:
						raise SyntaxError(this_line)
				
				
				
				# python codes to generate contents
				elif splitted_line[0] == "```":
					in_pycode = True
				
				
				
				# add minecraft tags
				elif splitted_line[0] == "tag":
					if splitted_line[1] == "tick" or splitted_line[1] == "load":
						line_index += 1
						if script[line_index].lstrip(" \t").rstrip(" \t") != '{':
							raise SyntaxError(script[line_index].lstrip(" \t"))
						
						line_index += 1
						while line_index < len(script):
							tag_content = script[line_index].lstrip(" \t").rstrip(" \t")
							# not an empty line or comment
							if not (len(tag_content) == 0 or tag_content[0] == '#'):
								if tag_content == '}':
									break
								else:
									# fix '"' mark
									if tag_content[0] != '"':
										tag_content = '"' + tag_content
									if tag_content[-1] != '"':
										tag_content += '"'
										
									tags[splitted_line[1]].append(tag_content)
									if line_index == (len(script) - 1):
										raise SyntaxError("EOF while scanning tag literal")
									
							line_index += 1
					else:
						raise SyntaxError(this_line)
					
				
				
				# unknown command
				else:
					raise SyntaxError(this_line)
					
		line_index += 1
		
	return description, namespaces, tags

###########################################
#            normal functions             #
# ======================================= #
#             user functions              #
###########################################

def create_project(proj_name):
	if os.path.isdir(proj_name):	
		return "Destination folder '%s' already exists, please try again with another name." %proj_name
	
	os.mkdir(proj_name)
	os.mkdir(proj_name + "\\build")
	os.mkdir(proj_name + "\\data")
	shutil.copyfile(install_path + "samp\\template.dpl", proj_name + "\\__main__.dpl")
	
	return "Datapack project '%s' created!" %proj_name

def build_datapack(proj_path):
	# fix path format
	if proj_path[-1] == '\\' or proj_path[-1] == '/':
		proj_path = proj_path[:-1]
		
	if not os.path.isfile(proj_path + "\\__main__.dpl"):
		return "No such file or directory:\n  '%s'" %proj_path + "\\__main__.dpl"
	
	global PROJ_DIR
	PROJ_DIR = proj_path
	
	datapack_name = os.path.basename(proj_path)
	with open(proj_path + "\\__main__.dpl", "r", encoding='UTF-8') as script:
		description, namespaces, tags = read_script(script.read().splitlines(), proj_path)
	
	if not os.path.isdir(proj_path + "\\build"):
		os.mkdir(proj_path + "\\build")
	
	if os.path.isdir(proj_path + "\\build\\" + datapack_name):
		user_response = str(input("Datapack '" + datapack_name + "' already exists.\nDo you want to replace it (y/n)? ")).lower()
		while user_response not in ['y', 'n']:
			user_response = str(input("'%s' was not one of the expected responses: y, n\nDo you want to replace it (y/n)? " %user_response)).lower()
		
		if user_response == 'y':
			shutil.rmtree(proj_path + "\\build\\" + datapack_name)
		else:
			return "Build cancelled."

	os.mkdir(proj_path + "\\build\\" + datapack_name)
	os.mkdir(proj_path + "\\build\\" + datapack_name + "\\data")
		
	# generate pack.mcmeta
	with open(proj_path + "\\build\\" + datapack_name + "\\pack.mcmeta", "w", encoding="utf-8") as pack:
		pack.write('{\n\t"pack":\n\t{\n\t\t"pack_format": 1,\n\t\t"description": "%s"\n\t}\n}' %description)
		
	build_dir = proj_path + "\\build\\" + datapack_name + "\\data\\"
	# recursive build
	try:
		for n in namespaces.keys():
			namespaces[n].build(build_dir, namespaces[n].name + ':')
	except ValueError as err:
		shutil.rmtree(proj_path + "\\build\\" + datapack_name)
		return "ValueError: " + err.args[0] + "\nBuild failed!"
	
	# build tags
	if not os.path.isdir(build_dir + "minecraft"):
		os.mkdir(build_dir + "minecraft")
	if not os.path.isdir(build_dir + "minecraft\\tags"):
		os.mkdir(build_dir + "minecraft\\tags")
	if not os.path.isdir(build_dir + "minecraft\\tags\\functions"):
		os.mkdir(build_dir + "minecraft\\tags\\functions")
	
	for key in tags.keys():
		exist_tags = set()
		tag_order = []
		for tag in tags[key]:
			if tag not in exist_tags:
				tag_order.append(tag)
				exist_tags.add(tag)
		with open(build_dir + "minecraft\\tags\\functions\\" + key + ".json", "w", encoding="utf-8") as f:
			f.write('{\n\t"values":[\n\t\t%s\n\t]\n}' %",\n\t\t".join(tag_order))
	
	# copy side packages
	folder_copy(proj_path + "\\data\\", build_dir)
	
	return "Build completed!"
	
def install_module(module_name):
	return "Function not implemented yet."
	
def uninstall_module(module_name):
	remove_path = []
	for path in module_path:
		if os.path.isfile(path + module_name + ".dpl"):
			remove_path.append(path + module_name + ".dpl")
		elif os.path.isfile(path + module_name + "\\__main__.dpl"):
			remove_path.append(path + module_name)
	
	if len(remove_path) == 0:
		return module_name + " is not installed."

	for path in remove_path:
		print("Will remove:\n  " + path)
	user_response = str(input("Continue (y/n)? ")).lower()
	while user_response not in ['y', 'n']:
		user_response = str(input("'%s' was not one of the expected responses: y, n\nContinue (y/n)? " %user_response)).lower()
	
	if user_response == 'y':
		for path in remove_path:
			try:
				os.remove(path)
			except OSError:
				shutil.rmtree(path)
		return "%s uninstalled!" %module_name
		
	return "Uninstallation cancelled."
	
def help():
	print("Use 'mcdp create <datapack name>' to create a new datapack project")
	print("Use 'mcdp make <project directory>' to build a datapack")
	print("Use 'mcdp install <module name>' to install a module from the internet")
	print("Use 'mcdp uninstall <module name>' to uninstall a module")
	
	

if __name__ == "__main__":
	if len(sys.argv) < 3:
		if len(sys.argv) > 1:
			print("Unknown command.")
		help()
	else:
		# file name or path may have spaces
		script_name = ' '.join(sys.argv[2:])
		if sys.argv[1][0].lower() == "c":
			print(create_project(script_name))
			
		elif sys.argv[1][0].lower() == "m":
			print(build_datapack(script_name))
			
		elif sys.argv[1][0].lower() == "i":
			print(install_module(script_name))
			
		elif sys.argv[1][0].lower() == "u":
			print(uninstall_module(script_name))
		else:
			print("Unknown command.")
			help()