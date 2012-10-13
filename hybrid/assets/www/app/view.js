App.View = (function(lng, app, undefined) {

	lng.View.Template
			.create('celebrity-item',
					'<li class="selectable">\
                    {{celebrityname}}\
					</li>');

	return {

	}

})(LUNGO, App);