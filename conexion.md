# Conexión de MCP3204 con Jetson Nano 4 Gb

Los pines de la Jetson Nano están orientados de la siguiente forma:

![Image text](Jetson%20nano%20pines.png)

Y los pines de el convertidor MCP3204 son:
![Image text](MCP3204%20pines.png)

La forma en que se conecta el MCP3204 con la comunicación serial es:

- VDD y Vref al pin 1 de Jetson (3.3 V)
- AGND a cualquier pin de tierra en la tarjeta 
- CLK al pin 23 de Jetson Nano
- Dout (MISO) al pin 21 de la Jetson Nano
- Din (MOSI) al pin 19
- CS/SHDN al pin 24
- DGND a cualquier pin de GND de la Jetson Nano 