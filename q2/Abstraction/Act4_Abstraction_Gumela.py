from abc import ABC, abstractmethod

class Sensor(ABC):
  """Abstract Blueprint for all laboratory sensors."""

  def __init__(self, sensor_name):
    self.sensor_name = sensor_name

  @abstractmethod
  def get_reading(self):
    """Contract method that all child sensors must implement."""
    pass


class PHSensor(Sensor):

  def __init__(self, sensor_name="pH Sensor", ph_value=7.2):
    super().__init__(sensor_name)
    self.ph_value = ph_value

  def get_reading(self):
    if self.ph_value < 7.0:
      status = "Acidic"
    elif self.ph_value > 7.0:
      status = "Basic/Alkaline"
    else:
      status = "Neutral"
    return f"{self.ph_value} pH ({status})"


class TempSensor(Sensor):

  def __init__(self, sensor_name="Temperature Sensor", temp_celsius=24.5):
    super().__init__(sensor_name)
    self.temp_celsius = temp_celsius

  def get_reading(self):
    return f"{self.temp_celsius}°C"

if __name__ == "__main__":
  print("--- Lab Inventory System ---")

  sensors = [PHSensor(ph_value=7.2),TempSensor(temp_celsius=24.5),]

  for sensor in sensors:
    print(f"[{sensor.sensor_name}] Reading: {sensor.get_reading()}")

  print("----------------------------")

# my_sensor = Sensor("Generic Sensor")