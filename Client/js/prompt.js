function promptClass(output)//выводит в консоль по write(text)
{
	var that = this;

	this.write = function(text)
	{
		console.log(text);
		var pre = document.createElement("p");
		pre.style.wordWrap = "break-word";
		pre.innerHTML = text;
		output.appendChild(pre);
	}

	return this;
}