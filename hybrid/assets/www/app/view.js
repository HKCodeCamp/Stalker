App.View = (function(lng, app, undefined) {

	lng.View.Template
			.create(
					'news-item',
					'<li class="selectable "><img src="assets/images/avatars/{{image}}.jpg">\
					<div class="onright">{{date}}</div>{{celebrity_name}}<small>was\
					{{comment}} at {{location}}</small></li>');

	lng.View.Template
			.create('celebrity-item',
					'<li class="selectable">\
                    {{celebrity_name}}\
					</li>');

	return {
	}

})(LUNGO, App);