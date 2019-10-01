from setuptools import setup, find_packages

setup(name='header_control',
      version='1.0.0',
      author='Casey Bruno',
      author_email='cabruno98@gmail.com',
      description='Library to set and maintain a certain header for a servo motor',
      license='MIT',
      url='https://github.com/kcydesu/header_control',
      dependency_links=['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.9.3','https://github.com/kcydesu/servo-pi','https://github.com/adafruit/Adafruit_Python_BNO055'],
      install_requires=['RPi.GPIO','servo_pi','Adafruit_BNO055'],
      packages=find_packages()
      )