function add_zero(number) {
	if (number < 10) {
		return '0' + number.toString();
	} else {
		return number.toString();
	}
}

window.setInterval(function () {
	var current_date = new Date();
	var hours = current_date.getHours();
	var minutes = current_date.getMinutes();
	var seconds = current_date.getSeconds();

	document.getElementById('hours').innerHTML = add_zero(hours);
	document.getElementById('minutes').innerHTML = add_zero(minutes);
	document.getElementById('seconds').innerHTML = add_zero(seconds);
}, 1000);
