from playsound import playsound
import hug

@hug.static('/static')
def my_static_dirs():
	return "."


@hug.static('/endpoints')
def sound_endpoints():
	return "/Sounds"


@hug.get('/bruh')
@hug.local()
def bruh():
	playsound('./Sounds/bruh.mp3')
	return {"played"}


@hug.get('/ded')
@hug.local()
def ded():
	playsound('./Sounds/ded.mp3')
	return {"played"}


@hug.get('/fail')
@hug.local()
def fail():
	playsound('./Sounds/fail.mp3')
	return {"played"}


@hug.get('/nice')
@hug.local()
def nice():
	playsound('./Sounds/nice.mp3')
	return {"played"}


@hug.get('/oof')
@hug.local()
def oof():
	playsound('./Sounds/oof.mp3')
	return {"played"}


@hug.get('/sad')
@hug.local()
def sad():
	playsound('./Sounds/sad.mp3')
	return {"played"}


@hug.get('/sadude')
@hug.local()
def sadude():
	playsound('./Sounds/sadude.mp3')
	return {"played"}


