function MAIN()
{
	logwrite = new promptClass(document.getElementById('output'));
	socket = new websocketTransmitter('ws://localhost:9999/');
	
	socket.testWebSocket();
}
