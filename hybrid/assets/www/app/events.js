App.Events = (function(lng, app, undefined) {

	lng.ready(function() {
		App.Services.listNews();
	});

	lng.dom('article#celebrity a').tap(function(event) {
		App.Services.searchCelebrities($$('article#celebrity-list input').val());
	});

})(LUNGO, App);