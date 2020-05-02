import os, json, requests, random, io, zipfile, shutil, errno

def _7_(config, name):
	_9_ = None
	if name in config:
		if config[name] is not None:
			config[name] = config[name].strip()
			if config[name] != '':
				_9_ = config[name]
	while True:
		value = input(name + (':' if _9_ is None else '[%s]:'%_9_ ))
		if value is None and _9_ is not None: return
		value = value.strip()
		if value == '' and _9_ is not None: return
		if value != '':
			config[name] = value
			return

def _6_(args, save=False):
	path = os.path.split(__file__)[0]
	_1_ = os.path.join(path, 'config.json')
	if os.path.isfile(_1_):
		with open(_1_) as fp:
			config = json.load(fp)
	else:
		config = {}
	for arg in args:
		_7_(config, arg)
	if save:
		with open(_1_, 'w') as fp:
			json.dump(config, fp)
	return config

def _10_(k, _0_ ='abcdefghijklmnopqrstuvwxyz'):
	return ''.join([_0_[random.randint(0,len(_0_)-1)] for i in range(k)])

def _13_(_14_, object, method, **kwargs):
	_14_ = _14_ or 'localhost'
	data = {'object':object, 'method':method, 'data':json.dumps(kwargs)}
	response = requests.post('http://%s/ajax'%_14_, data=data, verify=False)
	return json.loads(response.content)

def login(_11_, user, pwd, app='__update__'):
	app_secret = _10_(16)
	response = _13_(_11_, 'login', 'login_with_pwd', user=user, pwd=pwd, app=app, app_secret=app_secret)
	if 'error' in response: return None
	response['app_secret'] = app_secret + response['app_secret']
	return response

def makedirs(path):
	try:
		os.makedirs(path)
	except OSError as exception:
		assert exception.errno == errno.EEXIST

def _12_(filename, _15_):
	makedirs(os.path.split(filename)[0])
	with _15_.open(filename, 'r') as _4_:
		with open(filename, 'wb') as _5_:
			_5_.write(_4_.read())

def _2_(config):
	_14_, app, pwd = config['root_server'], config['app'], config['password']
	user_info = login(_14_, app, pwd)
	data = {'user_info':json.dumps(user_info)}
	response = requests.post('http://%s/ui/update.zip?v=%s'%(_14_,_10_(16)), data=data, verify=False)
	if isinstance(response, dict):
		if 'error' in response:
			print('ERROR', response['error'])
		else:
			print('RESPONSE', response)
		return
	if os.path.isdir(os.path.join('servo', 'core')):
		shutil.rmtree(os.path.join('servo', 'core'))
	_8_ = os.path.isdir('user_db')
	if _8_:
		print('To update the user_db, remove it and run this program again,')
	with zipfile.ZipFile(io.BytesIO(response.content), "r", zipfile.ZIP_DEFLATED) as _15_:
		for info in _15_.infolist():
			_3_ = info.filename.split(os.sep)[0]
			if _3_ == 'servo':
				_12_(info.filename, _15_)
			elif _3_ == 'user_db':
				if not _8_:
					_12_(info.filename, _15_)
			elif _3_ == 'web':
				_12_(info.filename, _15_)
			else:
				print('Ignore:', info.filename)


if __name__ == '__main__':
	config = _6_(['root_server', 'app', 'password'], True)
	_2_(config)


