jQuery.find('#toggle_header')[0].onclick=function toggle() {
    if (this.className) {
        if (this.className == 'green') {
		this.className = 'red'}
	else {
		this.className='green';
	}
    } else {
        this.className = 'green';
    }
}
