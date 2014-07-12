//#! directive : upvote
demoApp.directive('dirCounterpick', function($timeout) {
  return {
    link: function(scope, element, attrs) {
      element.bind('click', function() {
        $timeout(function() {

			//#! open modal	
			var postid =  attrs.dirCounterpick;
			var heroes = element.attr('data').split(',');
			$('#postid').val(postid);
			$.each(heroes,function(k, v){
				$('#comm-hero-pick-'+v).hide();
			});			
			$('#comm-modal-posts').fadeIn('fast').show();	
			$('.comm-preload-img-lazy').lazyload({
			    effect : "fadeIn",
			    threshold : 3
			});
			
			// check if login user
			/*
			iflogin = $('#comm-auth-verification').attr('data');
			if(iflogin == '0'){
				
				$('#comm-modal-signin').fadeIn('fast').show();	
				$('#comm-modal-signin').on('click', function(){
					$(this).hide();	
				});
													
			}else{

				//#! open modal	
				var postid =  attrs.dirCounterpick;
				var heroes = element.attr('data').split(',');
				$('#postid').val(postid);
				$.each(heroes,function(k, v){
					$('#comm-hero-pick-'+v).hide();
				});			
				$('#comm-modal-posts').fadeIn('fast').show();	
				$('.comm-preload-img-lazy').lazyload({
				    effect : "fadeIn",
				    threshold : 3
				});
				
			}
			*/
			
        });
      });
    }
  };
});

//#! directive : counter pick
demoApp.directive('dirUpvote', function($timeout) {
  return {
    link: function(scope, element, attrs) {
		element.bind('click', function() {
        $timeout(function() {


			// check if login user
			iflogin = $('#comm-auth-verification').attr('data');
			if(iflogin == '0'){
				
				$('#comm-modal-signin').fadeIn('fast').show();	
				$('#comm-modal-signin').on('click', function(){
					$(this).hide();	
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