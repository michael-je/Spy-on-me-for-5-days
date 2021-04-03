import secrets

import asyncio
from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, SetCurrentSceneRequest

loop = asyncio.get_event_loop()

async def send_command(command):

	async with OBSWS('localhost', 4444, secrets.obs_wss_pass) as obsws:

		response = await obsws.require(SetCurrentSceneRequest(scene_name=f"scene_{command}"))
		if response.status == ResponseStatus.OK:
			print("Scene set")
		else:
			print("error:", response.error)


def main(*args):
	cmd_info, *_ = args
	command = cmd_info[0]
	print("obs_main: ", command)
	loop.run_until_complete(send_command(command))


def close_loop():
	loop.close()
