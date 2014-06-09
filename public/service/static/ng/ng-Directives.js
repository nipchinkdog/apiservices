//#! directive : upvote
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

//#! directive : counter pick
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
			$('.comm-modal-wrpp').show();	
			$('.comm-selection-img-lazy').lazyload({
			    effect : "fadeIn",
			    threshold : 5
			});
					
        });
      });
    }
  };
});