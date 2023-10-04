jQuery.getJSON('https://fourtonfish.com/hellosalut/?lang=fr').then((res)=> {
	jQuery.find('DIV#hello')[0].innerHTML = res.hello;
})
