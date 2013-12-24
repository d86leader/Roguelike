function asciiRender(c)//c for canvas 2d context
{
	var that = this;

	this.drawMap = function(map)
	{
		if(typeof map != "object")
			throw {message: 'не то суешь!'}

		var yl = map.length;
		var xl = map[1].length;
		var w = canvas.width / xl;

		c.font = w + 'px Arial';

		c.fillStyle = "#ffffff";
		c.fillRect(0,0,canvas.width,canvas.height);

		var counterx = 0;
		var countery = 0;
		for(var i1 = 0; i1 < yl; i1++)
		{
			for(var i2 = 0; i2 < xl; i2++)
			{
				c.fillStyle = '#000000'
				c.fillText(map[i1][i2].char, counterx, countery);
				countery+= w;
			}
			counterx+= w;
		}
	}

	return this;
}