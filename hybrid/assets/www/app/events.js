App.Events = (function(lng, app, undefined) {

	lng.ready(function() {
		// App.Services.mockProfiles();
		// lng.View.Aside.show('#kitchen-sink', '#kitchen-sink-scroll');
		// lng.View.Element.progress('.progress', 10, true, 'Downloading
		// 1/5...');
	});

	lng.dom('article#celebrity-list a').tap(function(event) {
		App.Services.searchCelebrities($$('article#celebrity-list input').val());
	});

})(LUNGO, App);