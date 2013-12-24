function MAIN(server)
{
	logwrite = new promptClass(document.getElementById('output'));
	socket = new websocketTransmitter(server, 80);
	socketStack = new stack();
	asciirender = new asciiRender(canvas.getContext('2d'));
	mapconverter = new converter();

	c = canvas.getContext('2d');
	c.strokeRect(0,0,500,500);
	
	socket.startWebSocket();

	//допустим, существует объект с парами моб/препятсвие : графика для всех режимов отображения
}
