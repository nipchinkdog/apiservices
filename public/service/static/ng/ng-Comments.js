demoApp.controller('ApiCommentsController', function($scope, $state, $stateParams, ApiGetFactory, ApiPostFactory){		
	
	//#! ****************************************************************
	//#! Listing ******************************************
	//#! ****************************************************************
	$scope.postid = $stateParams.id;
	$scope.loadFetchData = function(){
		var url = '/api/comm/comments/showById/'+ $scope.postid;
		ApiGetFactory.get(url).then(function(data) {
			$scope.postcomments = data[0].comments;
			$scope.postheader = data[0].posts;
			$scope.postcommentscount = $scope.postcomments.length;
	    });
    };

	$scope.loadApiCommentsCtrl = function(){
		$('.comm-modal-wrpp-comments').show();	
		$('.comm-side-modal-wrpp-close').on('click', function(){
			$('.comm-modal-wrpp').hide();
			$('.comm-modal-wrpp-comments').hide();	
		});
 	};

	//# init
	$scope.postheader = [];
	$scope.postcomments = [];
	$scope.loadApiCommentsCtrl();
	$scope.loadFetchData();
	$scope.commentcount = $scope.postcomments.length;
	
	
	//#! ****************************************************************
	//#! Posting ******************************************
	//#! ****************************************************************
	$scope.formData = {};
	$scope.formData.posts = $scope.postid;

	$scope.saveFetchData = function(){
		console.log($scope.formData);
		var url = '/api/comm/comments/writeComments/';
		ApiPostFactory.post(url, $scope.formData).then(function(data) {
	        $scope.postcomments = $scope.postcomments.concat(data.data);
	        $scope.postcommentscount = $scope.postcomments.length;
	    });
	};
	
	$scope.loadApiCommentsSubmit = function(){
		$scope.saveFetchData();
	};
	

	
});