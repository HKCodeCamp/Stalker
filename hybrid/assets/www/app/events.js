App.Events = (function(lng, app, undefined) {

	lng.ready(function() {
		App.Services.listNews();
	});

	lng.dom('article#celebrity a').tap(function(event) {
		App.Services.searchCelebrities($$('article#celebrity input').val());
	});

})(LUNGO, App);