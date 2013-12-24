function converter()
{
	var that = this;

	this.cutoffMap = function(initObj)
	{
		if(initObj['map_dung'])
			return initObj['map_dung'];
		else
			throw {message: 'не то суешь!'};
	}

	return this;
}