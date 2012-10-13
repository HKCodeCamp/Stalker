App.Services = (function(lng, app, undefined) {

	lng.Service.Settings = {
		async : true,
		timeout : 1000
	};

	var root = 'http://istalkerapp.appspot.com/'

	var listNews = function() {
		var url = root + 'list/';
		var data = {};

		lng.Service.json(url, data, function(response) {
			for (i in response) {
				response[i]['image'] = i;
				var parameters = {
					el : '#news',
					template : 'news-item',
					data : response[i]
				};
				lng.View.Template.List.append(parameters);
			}
		});
	}

	var searchCelebrities = function(search) {
		var url = root + 'search/' + search + '/';
		var data = {};

		lng.Service.json(url, data, function(response) {
			for (i in response) {
				var parameters = {
					el : '#celebrity',
					template : 'celebrity-item',
					data : response[i]
				};
				lng.View.Template.List.append(parameters);
			}
		});
	}

	return {
		listNews : listNews,
		searchCelebrities : searchCelebrities
	}

})(LUNGO, App);