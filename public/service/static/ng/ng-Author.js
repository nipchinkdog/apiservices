//#! controller
demoApp.controller('ApiAuthorController', function($scope, $state, $stateParams, ApiGetFactory, ApiPostFactory, ApiDeleteFactory){	

	$scope.idPara = $stateParams.idPara;

	$scope.loadFetchDataAuthor = function(){
		var url = '/api/comm/posts/showById/' + $scope.page + '/' + $scope.limit + '/' + $scope.idPara + '/posts';
		ApiGetFactory.get(url).then(function(data) {
	        $scope.postsAuthor = data;
	    });
    };

	$scope.loadFetchData = function(){
		var url = '/api/comm/posts/showByAuthor/' + $scope.page + '/' + $scope.limit + '/' + $scope.idPara + '/author';
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
	$scope.postsAuthor = [];
	$scope.loadFetchData();
	$scope.loadFetchDataAuthor();
});

