App.Services = (function(lng, app, undefined) {

	lng.Service.Settings = {
			async : true,
			timeout : 1000
		};

	var root = 'http://istalkerapp.appspot.com/'
		
		
	var searchCelebrities = function(search) {
//		var url = root + 'search/' + search + '/';
		var url = root + 'list/';
		
		var data = {};
		lng.Service.json(url, data, function(response) {
			for (i in response) {
				var parameters = {
					el : '#celebrity-list',
					template : 'celebrity-item',
					data : response[i]
				};
				lng.View.Template.List.append(parameters);
			}
		});
	}

	return {
		searchCelebrities : searchCelebrities
	}

})(LUNGO, App);