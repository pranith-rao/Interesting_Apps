function add_zero(number) {
	if (number < 10) {
		return '0' + number.toString();
	} else {
		return number.toString();
	}
}
var isRunning = false,
	start_time,
	current_time,
	elapsed_time = 0,
	start_watch,
	hours,
	minutes,
	seconds,
	remainder;
document.getElementById('start_stop').onclick = function () {
	if (!isRunning) {
		isRunning = true;
		if (elapsed_time == 0) {
			start_time = new Date().getTime();
		} else {
			start_time = new Date().getTime() - elapsed_time;
		}
		start_watch = window.setInterval(function () {
			current_time = new Date().getTime();
			elapsed_time = current_time - start_time;
			hours = Math.floor(elapsed_time / 86400000);
			remainder = elapsed_time - hours * 86400000;
			minutes = Math.floor(remainder / 60000);
			remainder -= minutes * 60000;
			seconds = Math.floor(remainder / 1000);
			remainder -= seconds * 1000;
			document.getElementById('stopwatch').innerHTML =
				add_zero(hours) + ':' + add_zero(minutes) + ':' + add_zero(seconds) + ':' + add_zero(remainder);
		}, 10);
	} else {
		isRunning = false;
		window.clearInterval(start_watch);
	}
};
document.getElementById('reset').onclick = function () {
	start_time = new Date().getTime();
	if (!isRunning) {
		elapsed_time = 0;
		document.getElementById('stopwatch').innerHTML = '00:00:00 000';
	}
};
