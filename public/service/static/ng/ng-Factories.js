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
        post: function(url, formData) {
			return $http({
				method : 'POST',
				url : url,
				data : formData
			}).success(function(data){
				return data;
			}).error(function(data){
				return data;
			});
       }
    };
});

