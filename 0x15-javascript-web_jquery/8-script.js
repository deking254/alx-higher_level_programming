jQuery.get('https://swapi-api.alx-tools.com/api/films/?format=json').then((res)=>{
	a = jQuery.find('UL#list_movies')[0].innerHTML ; 
	for (let index = 0; index < res.results.length; index++) {
        	a = a + "<li>" + res.results[index].title + "</li>   \n";
		jQuery.find('UL#list_movies')[0].innerHTML = a;
	}
})
