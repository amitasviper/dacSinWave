This python program generates a sin wave using Beaglebone Black and MCP7425(DAC). MCP7425 is connected to Beaglebone Black using the i2c interface.
Connect the Beaglebone to the DAC using following pin layout

	>>Beaglebone		MCP7425

	>>  P9_19 -------------> SCL
	>>  P9_20 -------------> SDA
	>>  P9_3  -------------> VCC
	>>  P9_1  -------------> GND

and connect the OUT and GND of MCP7425 to the oscilloscope inputs.

Now to check the address at which your DAC is connected. Run the following command:
	
	>> i2cdetect -y -r 1

Note the adress from the above output and edit the address at line no 14 in sinWaveMCP.

Now run the program using following command:

	>> python sinWaveMCP.py

You will observe the waveform on the oscilloscope and you can also change the frequency of the sin wave by giving input to the program.
