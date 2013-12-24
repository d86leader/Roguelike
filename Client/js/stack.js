function stack()
{
	var that = this;

	this.s = [];

	this.push = function(val)
	{
		that.s[that.s.length] = val;
		return val;
	}
	this.pop = function(type)
	{
		if(type == 's')
			return that.s[that.s.length - 1];
		else if (type == 'q')
			return that.s[0]
	}
	this.drop = function(type)
	{
		if(that.s.length > 0)
		{
			if(type == 's')
			{
				var ret = that.s[that.s.length - 1];
				that.s.splice(that.s.length - 1, 1)
				return ret;
			}
			else if(type == 'q')
			{
				var ret = that.s[0];
				that.s.splice(0, 1)
				return ret;
			}
		}
		return null;
	}

	return this;
}