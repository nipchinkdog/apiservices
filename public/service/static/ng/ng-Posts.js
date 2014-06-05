//#! controller
demoApp.controller('ApiPostsController', function($scope, $state, ApiGetFactory, ApiPostFactory, ApiDeleteFactory){	

	$scope.loadFetchData = function(){
		var url = '/api/comm/posts/showByLimit/' + $scope.page + '/' + $scope.limit+ '/fetch';
		ApiGetFactory.get(url).then(function(data) {
			$scope.more = data.length === $scope.limit;
	        $scope.posts = $scope.posts.concat(data);
			iflogin = $('#comm-auth-verification').attr('data');
	    });
    };
    	
	$scope.loadApiPostsCtrl = function(){
		$scope.page += 1;
		$scope.loadFetchData();
	};

	$scope.loadhasMore = function() {
        return $scope.more;
	};
	
	$scope.PostApiVote = function(id){
		var url = '/api/comm/votes/writeVotes/' + id + '/upvote';
		ApiGetFactory.get(url).then(function(data) {
	    });
	};	

	$scope.DeleteApiVote = function(id){
		var url = '/api/comm/votes/writeVotes/' + id + '/unvote';
		ApiDeleteFactory.remove(url).then(function(data) {
	    });
	};
	

	//# init
	$scope.page = 1;
	$scope.limit = 5;
	$scope.more = true;
	$scope.posts = [];
	$scope.loadFetchData();
});

//#! directive
demoApp.directive('dirUpvote', function($timeout) {
  return {
    link: function(scope, element, attrs) {
      element.bind('click', function() {
        $timeout(function() {

			// check if login user
			iflogin = $('#comm-auth-verification').attr('data');
			if(iflogin == '0'){
				
				$('.comm-modal-wrpp-promts').show();	
				$('.comm-side-modal-wrpp-close').on('click', function(){
					$('.comm-modal-wrpp').hide();
					$('.comm-modal-wrpp-promts').hide();	
				});
													
			}else{

				// get current vote count
				vote = parseInt(element.parent().find('span').html());
	
				if (element.hasClass('comm-voted')){
					scope.DeleteApiVote(attrs.dirUpvote);
					element.parent().find('span').html(vote-1);
		          	element.removeClass('comm-voted');
				}else{
					scope.PostApiVote(attrs.dirUpvote);
		          	element.parent().find('span').html(vote+1);
		          	element.addClass('comm-voted');
				}
				
			}
			
        });
      });
    }
  };
});
