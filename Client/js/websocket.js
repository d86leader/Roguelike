function websocketTransmitter(wsUri, port)
{
	var that = this;

	this.startWebSocket = function()
	{
		that.websocket = new WebSocket(wsUri);
		that.websocket.onopen = function(evt) { that.onOpen(port) }; 
		that.websocket.onclose = function(evt) { that.onClose(evt) }; 
		that.websocket.onmessage = function(evt) { that.onMessage(evt) }; 
		that.websocket.onerror = function(evt) { that.onError(evt) };

		setInterval()
	}
	this.onOpen = function(msg)
	{
		log("CONNECTED("+that.websocket.readyState+")");
		log(msg);
		that.doSend(msg);
	}
	this.onClose = function(evt)
	{
		log("DISCONNECTED("+that.websocket.readyState+")");
	}  
	this.onMessage = function(evt)
	{
		log('<span style="color: blue;">RESPONSE('+that.websocket.readyState+'): ' + evt.data);
		socketStack.push(JSON.parse(evt.data));
	}
	this.onError = function(evt)
	{
		log('<span style="color: red;">ERROR('+that.websocket.readyState+'): ' + evt.data);
	}  
	this.doSend = function(message)
	{
		that.websocket.send(message);
		log("SENT("+that.websocket.readyState+"): " + message);
	}
	function log(message)
	{
		logwrite.write(message)
	}

	return this;
}