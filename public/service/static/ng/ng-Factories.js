//#! Get Factory
demoApp.factory('ApiGetFactory', function($http) {
	return {
        get: function(url) {
			return $http.get(url).then(function (response) {
			     if (response.data.error) {
			         return null;
			     } else {
			         //console.log(response.data);
			         return response.data;
			     }
			});
       }
    };
});

//#! Post Factory
demoApp.factory('ApiPostFactory', function($http) {
	return {
        post: function(url, pdata) {
			return $http({
				method : 'POST',
				url : url,
				data : pdata
			}).success(function(data){
				return data;
			}).error(function(data){
				return data;
			});
       }
    };
});

//#! Post Factory
demoApp.factory('ApiDeleteFactory', function($http) {
	return {
        remove: function(url) {
			return $http({
				method : 'DELETE',
				url : url,
			}).success(function(data){
				return data;
			}).error(function(data){
				return data;
			});
       }
    };
});

