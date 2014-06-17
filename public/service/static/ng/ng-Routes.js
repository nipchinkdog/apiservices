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
		.state('challenge', {
			url : '/ch/:idPara',
			views : {
				'viewSearch' : {
					templateUrl: '/angular/tpl/challenge/',
					controller: 'ApiChallengeController'
				}
			}
		})		
		.state('author', {
			url : '/ath/:idPara',
			views : {
				'viewSearch' : {
					templateUrl: '/angular/tpl/author/',
					controller: 'ApiAuthorController'
				}
			}
		})		
		.state('search', {
			url : '/se/:wordPara',
			views : {
				'viewSearch' : {
					templateUrl: '/angular/tpl/search/',
					controller: 'ApiSearchController'
				}
			}
		})
		.state('posts.comments', {
			url : '/co/:id',
			views : {
				'viewComments' : {
					templateUrl: '/angular/tpl/comments/',
					controller: 'ApiCommentsController'
				}
			}
		})
		.state('pages', {
			url : '/about',
			views : {
				'viewPosts' : {
					templateUrl: '/angular/tpl/about/',
					controller: ''
				}
			}
		});

		
});