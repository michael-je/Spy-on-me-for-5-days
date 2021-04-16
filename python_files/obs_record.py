import cfg
import secrets
import utilities

from time import sleep
import asyncio
from obswsrc import OBSWS
from obswsrc.requests import ResponseStatus, StartRecordingRequest, StopRecordingRequest

loop = asyncio.get_event_loop()


async def start_stop_recording():

	try:
		# Start recording initially
		async with OBSWS('localhost', 4444, secrets.obs_wss_pass) as obsws:
			response = await obsws.require(StartRecordingRequest())
			if response.status == ResponseStatus.OK:
				print("OBS Has started recording")
			else:
				print("OBS recording error:", response.error)

		while True:
			async with OBSWS('localhost', 4444, secrets.obs_wss_pass) as obsws:
							
				sleep(cfg.obs_recording_time_split)

				# Stop recording
				response = await obsws.require(StopRecordingRequest())
				if not response.status == ResponseStatus.OK:
					print("OBS recording error:", response.error)

				sleep(0.8)

				# Start recording
				response = await obsws.require(StartRecordingRequest())
				if not response.status == ResponseStatus.OK:
					print("OBS recording error:", response.error)

				print("OBS record split")

	except KeyboardInterrupt:
		async with OBSWS('localhost', 4444, secrets.obs_wss_pass) as obsws:
			response = await obsws.require(StopRecordingRequest())
			if not response.status == ResponseStatus.OK:
				print("OBS recording error:", response.error)
		return
			


def main():
	loop.run_until_complete(start_stop_recording())
	print("OBS has finished recording")


if __name__ == "__main__":
	main()