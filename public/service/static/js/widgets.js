jQuery(document).ready(function($) {
	
	$('.doc_api_detail_wrapper').hide();
	
	// collapsed wrapper
	$('.doc_api_header_trigger').on('click', function(){
		parent = $(this).parents('.doc_api_get_method');
		$('.doc_api_detail_wrapper').slideUp('fast');
		parent.children('.doc_api_detail_wrapper').delay(200).fadeIn(300);
	});
		
	// prettyprint		
    prettyPrint();

});

