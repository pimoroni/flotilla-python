from .module import Module
import math


class Motion(Module):
    name = 'accelerometer'
    range_in_g = 2

    @property
    def x(self):
        """Acceleration due to gravity on X axis in Gs"""
        return (self.accelerometer_x / 32768.0) * self.range_in_g

    @property
    def y(self):
        """Acceleration due to gravity on Y axis in Gs"""
        return (self.accelerometer_y / 32768.0) * self.range_in_g

    @property
    def z(self):
        """Acceleration due to gravity on Z axis in Gs"""
        return (self.accelerometer_z / 32768.0) * self.range_in_g

    @property
    def accelerometer_x(self):
        """Acceleration due to gravity on X axis, raw"""
        if len(self.data) > 0:
            return int(self.data[0])
        return 0

    @property
    def accelerometer_y(self):
        """Acceleration due to gravity on Y axis, raw"""
        if len(self.data) > 1:
            return int(self.data[1])
        return 0

    @property
    def accelerometer_z(self):
        """Acceleration due to gravity on Z axis, raw"""
        if len(self.data) > 2:
            return int(self.data[2])
        return 0

    @property
    def heading(self):
        truncate = [math.copysign(min(math.fabs(x), 1.0), x) for x in (self.accelerometer_x, self.accelerometer_y, self.accelerometer_z)]
        try:
            pitch = math.asin(-1 * truncate[0])
            roll = math.asin(truncate[1] / math.cos(pitch)) if abs(math.cos(pitch)) >= abs(truncate[1]) else 0
 
            tiltcomp_x = self.magnetometer_x * math.cos(pitch) + self.magnetometer_z * math.sin(pitch)
            tiltcomp_y = self.magnetometer_x * math.sin(roll) + math.sin(pitch) + \
                         self.magnetometer_y * math.cos(roll) - self.magnetometer_z * math.sin(roll) * math.cos(pitch)

            tilt_heading = math.atan2(tiltcomp_y, tiltcomp_x)

            if tilt_heading < 0:
                tilt_heading += 2 * math.pi

            if tilt_heading > 2 * math.pi:
                tilt_heading -= 2 * math.pi

            tilt_heading_degrees = round(math.degrees(tilt_heading),2)

            return tilt_heading_degrees

        except Exception:
            return 0

    @property
    def magnetometer_x(self):
        if len(self.data) > 3:
            return int(self.data[3])
        return 0

    @property
    def magnetometer_y(self):
        if len(self.data) > 4:
            return int(self.data[4])
        return 0

    @property
    def magnetometer_z(self):
        if len(self.data) > 5:
            return int(self.data[5])
        return 0
