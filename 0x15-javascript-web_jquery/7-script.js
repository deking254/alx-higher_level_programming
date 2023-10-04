jQuery.get('https://swapi-api.alx-tools.com/api/people/5/?format=json').then((res) =>{
	jQuery.find('DIV#character')[0].innerHTML = res.name;
})
