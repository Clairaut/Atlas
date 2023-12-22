import numpy as np
import spiceypy as spice
from datetime import timedelta
import traceback

class SpiceEphemeris:
	def __init__(self):
		# SPICE Kernels
		self.frame = 'J2000'
		self.pck = '../pck/pck.tpc'
		self.leap = '../leap/leap.tls'

		# Celestial Kernels
		self.celestials = '../bsp/de440s.bsp'

	def ecliptic(self, t, location, kernel, observer, target):
		try:
			# Loading kernels
			spice.furnsh(self.leap)
			spice.furnsh(self.pck)
			spice.furnsh(self.celestials)
			if kernel:
				spice.furnsh(kernel)

			# Retrograde time
			t_f = t + timedelta(days=2)

			# Converting to ephemeris time
			et = spice.str2et(str(t))
			et_f = spice.str2et(str(t_f))

			# Observer's topological point
			if location is not None:
				observer_geo = spice.georec(location.longitude, location.latitude, 0, 6371, (1 / 298.26))
				observer_matrix = spice.pxform('IAU_EARTH', 'ECLIPJ2000', et)
				observer_state = np.dot(observer_matrix, observer_geo[0:3])

			# Position and velocity vectors of target
			target_state, _ = spice.spkezr(target, et, 'ECLIPJ2000', 'LT+S', observer)
			target_state_f, _ = spice.spkezr(target, et_f, 'ECLIPJ2000', 'LT+S', observer)
			if location:
				target_state = target_state[0:3] - observer_state
				target_state_f = target_state_f[0:3] - observer_state

			# Converting cartesian to spherical coords
			r, lon, lat = spice.reclat(target_state[0:3])
			_, lon_f, _ = spice.reclat(target_state[0:3])

			# Checking if in retrograde
			retro = None
			if lon_f < lon:
				retro = True
			else:
				retro = False

			# Converting to degrees
			lon = np.degrees(lon)
			lon_retro = np.degrees(lon_f)
			lat = np.degrees(lat)

			# Unloading SPICE Kernels
			spice.unload(self.leap)
			spice.unload(self.pck)
			spice.unload(self.celestials)

			return r, lon, lat, retro

		except Exception as e:
			print(f"Error: {e}")
			traceback.print_exc()
			return None, None, None, None

	def orbit(self, t, kernel, observer, target, duration):
		try: 
			# Loading kernels
			spice.furnsh(self.leap)
			spice.furnsh(self.pck)
			spice.furnsh(self.celestials)
			if kernel:
				spice.furnsh(kernel)

			# Lunar cycle duration
			t_i = t - timedelta(days=duration)
			t_f = t + timedelta(days=duration)

			# Converting to ephemeris time
			et_i = spice.str2et(str(t_i))
			et_f = spice.str2et(str(t_f))

			# Partioning times
			times = np.linspace(et_i, et_f, 500)

			# Position and velocity vectors of target
			target_state, _ = spice.spkezr(target, times, 'ECLIPJ2000', 'LT+S', observer)

			# Target distances relative to observer
			distances = [np.linalg.norm(state[0:3]) for state in target_state]

			# Target longitudes and latitudes relative to observer
			longitudes = [np.degrees((spice.reclat(state[0:3])[2])) for state in target_state]
			latitudes = [np.degrees((spice.reclat(state[0:3])[2])) for state in target_state]

			# Index of maximum and minimum distances of target from observer
			apogee_index = np.argmax(distances)
			perigee_index = np.argmin(distances)
			
			# Position and velocity vectors of target at apogee and perigee
			apogee_state = target_state[apogee_index]
			perigee_state = target_state[perigee_index]

			# Cartesian to spherical coords
			apogee = spice.reclat(apogee_state[0:3])
			perigee = spice.reclat(perigee_state[0:3])

			# ASC and DSC nodes
			asc_node_index = None 
			dsc_node_index = None 
			min_diff = 360

			if longitudes:
				for i in range(len(latitudes) - 1):
					if longitudes[i - 1] < 0 and latitudes[i + 1] >= 0:
						asc_node_index = i
					if longitudes[i - 1] > 0 and latitudes[i + 1] <= 0:
						dsc_node_index = i

			if asc_node_index:
				asc_node_state = target_state[asc_node_index]
				asc_node = spice.reclat(asc_node_state[0:3])
			if dsc_node_index:
				dsc_node_state = target_state[dsc_node_index]
				dsc_node = spice.reclat(dsc_node_state[0:3])

			return apogee, perigee, asc_node, dsc_node

		except Exception as e:
			print(f"Error: {e}")
			traceback.print_exc()
			return None, None, None, None




