//#! config route
demoApp.config(function($stateProvider, $urlRouterProvider, $httpProvider) {

	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	
	$urlRouterProvider.otherwise("/posts");
	$stateProvider
		.state('posts', {
			url : '/posts',
			views : {
				'viewPosts' : {
					templateUrl: '/angular/tpl/posts/',
					controller: 'ApiPostsController'
				}
			}
		})
		.state('posts.comments', {
			url : '/:id',
			views : {
				'viewComments' : {
					templateUrl: '/angular/tpl/comments/',
					controller: 'ApiCommentsController'
				}
			}
		});

		
});