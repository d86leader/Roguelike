function websocketTransmitter(wsUri)
{
	var that = this;

	this.testWebSocket = function()
	{
		websocket = new WebSocket(wsUri);
		websocket.onopen = function(evt) { that.onOpen("80") }; 
		websocket.onclose = function(evt) { that.onClose(evt) }; 
		websocket.onmessage = function(evt) { that.onMessage(evt) }; 
		websocket.onerror = function(evt) { that.onError(evt) };
	}
	this.onOpen = function(msg)
	{
		log("CONNECTED("+websocket.readyState+")");
		that.doSend(msg);
	}
	this.onClose = function(evt)
	{
		log("DISCONNECTED("+websocket.readyState+")");
	}  
	this.onMessage = function(evt)
	{
		log('<span style="color: blue;">RESPONSE('+websocket.readyState+'): ' + evt.data);
		//websocket.close();
	}
	this.onError = function(evt)
	{
		log('<span style="color: red;">ERROR('+websocket.readyState+'): ' + evt.data);
	}  
	this.doSend = function(message)
	{
		log("SENT("+websocket.readyState+"): " + message);
		websocket.send(message);
	}
	function log(message)
	{
		logwrite.write(message)
	}

	return this;
}