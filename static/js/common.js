/**
 * 페이지 네비게이션
 */
var pageNavi = function(pageIndex, pageUnit, pageSize, totalCnt) {
	var pageTotal = Math.ceil(totalCnt / pageUnit);
	var co = Math.ceil(pageIndex / pageSize);
	
	startPage = ((co-1) * pageSize) + 1;
	endPage = startPage + pageSize - 1;
	
	var html = new Array();
	html.push('<div class="ui pagination menu">');
	
  	if(pageIndex > pageSize) {
  		var prePage = endPage - pageSize; 
  		html.push('<a class="icon item" onclick="return fn_egov_link_page(1);"><i class="left angle double icon"></i></a>');
  		html.push('<a class="icon item" onclick="return fn_egov_link_page('+prePage+');"><i class="left chevron icon"></i></a>');	
  	}
    
	// 페이지
	if(pageTotal < endPage) {
		endPage = pageTotal;
	}
		
	for(var i=startPage; i<=endPage; i++) {
		if(i == pageIndex) {
			html.push('<a class="active item">' + i + '</a>');
		} else {
			html.push('<a class="item" onclick="return fn_egov_link_page('+i+');">' + i + '</a>');
		}
	}
	
	if(endPage < pageTotal) {
		var nextPage = endPage + 1;
		html.push('<a class="icon item" onclick="return fn_egov_link_page('+nextPage+');"><i class="right chevron icon"></i></a>');
		html.push('<a class="icon item" onclick="return fn_egov_link_page('+pageTotal+');"><i class="double angle right icon"></i></a>');
	}
    
  	html.push('</div>');
  	
  	return html.join('');
}

function fn_egov_link_page(pageIndex) {
	location.href = '/main?pageIndex='+pageIndex;
}
