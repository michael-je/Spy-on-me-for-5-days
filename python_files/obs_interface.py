import secrets
import utilities

import asyncio
from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, SetCurrentSceneRequest

loop = asyncio.get_event_loop()

# store the current scene here, this is used when blurring/unblurring
current_scene = ''


def set_blur(state) -> None:
	"""
	Sets the state of blur in states.txt
	Also refreshes the scene if it is currently on scene_desktop or scene_desktop_blur
	"""
	if not state:
		utilities.set_state('blur', 0)
		print("blur off")
	else:
		utilities.set_state('blur', 1)
		print("blur on")

	global current_scene
	if current_scene == 'desktop' or current_scene == 'desktop_blur':
		set_scene('desktop')


def set_scene(scene_name) -> None:
	"""
	Sets OBS's scene to given scene. Performs a check to make sure to set it to corrrect desktop scene
	"""
	if scene_name == 'desktop' and utilities.get_state('blur'):
		scene_name = 'desktop_blur'
	
	global current_scene
	current_scene = scene_name
	loop.run_until_complete(send_command(scene_name))


async def send_command(scene_name):
	"""
	Sends the change scene command to OBS
	"""

	async with OBSWS('localhost', 4444, secrets.obs_wss_pass) as obsws:

		response = await obsws.require(SetCurrentSceneRequest(scene_name=f"scene_{scene_name}"))
		if response.status == ResponseStatus.OK:
			print(f"OBS: Scene set to {scene_name}")
		else:
			print("error:", response.error)


def main(*args) -> None:
	"""
	Handles incoming commands from call_interface_util.py
	"""
	cmd_info, *_ = args
	command = cmd_info[0]
	set_scene(command)


def close_loop() -> None:
	loop.close()


# set_scene('facecam')