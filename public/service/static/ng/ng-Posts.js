//#! controller
demoApp.controller('ApiPostsController', function($scope, $state, ApiGetFactory, ApiPostFactory){	

	$scope.loadFetchData = function(){
		var url = '/api/comm/posts/showByLimit/' + $scope.page + '/' + $scope.limit;
		ApiGetFactory.get(url).then(function(data) {
			$scope.more = data.length === $scope.limit;
	        $scope.posts = $scope.posts.concat(data);
	    });
    };
    	
	$scope.loadApiPostsCtrl = function(){
		$scope.page += 1;
		$scope.loadFetchData();
	};

	$scope.loadhasMore = function() {
        return $scope.more;
	};
	
	$scope.loadApiVote = function(id, e){
		
		alert($(e).attr('class'));
		
		var url = '/api/comm/votes/writeVotes/' + id + '/';
		ApiGetFactory.get(url).then(function(data) {
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
          vote = parseInt(element.parent().find('span').html());
          element.parent().find('span').html(vote+1);
        });
      });
    }
  };
});