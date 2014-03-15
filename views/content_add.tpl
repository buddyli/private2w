<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8" />
<title>添加内容</title>
<meta name="format-detection" content="telephone=no" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-touch-fullscreen" content="yes">
<meta name="viewport"
	content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no" />
<link rel="stylesheet" media="screen" type="text/css"
	href="/static/css/active.css" />
<script type="text/javascript" src="/static/js/json2s.js"></script>
<script type="text/javascript" src="/static/js/jquery-1.8.3.min.js"></script>
<script type="text/javascript">
function changeItem(id){
	$.post('selectItems', {'typeId': id}, function(json){
		$('#cascade_items').html('');
		for(var i=0; i<json.length; i++){
			var p = "<div><p name="+json[i][1]+">"+json[i][1]+":<input type='text' name='item_"+json[i][0]+" id='item_"+json[i][0]+"'/>";
			if (json[i][2] == 1)
				 p += "索引:<input type='checkbox' name='item_indexed_'"+json[i][0]+"' id='item_indexed_'"+json[i][0]+"/>";
			else
				p += "索引:<input type='checkbox' name='item_indexed_'"+json[i][0]+"' id='item_indexed_'"+json[i][0]+" checked='checked'/>";
			p += "</p></div>";
			$('#cascade_items').append(p);
		}
	}, 'json');
}

function Item(attrName, attrValue, indexed){
	this.attrName = attrName;
	this.attrValue = attrValue;
	this.indexed = indexed;
}

$(function(){
	$("#types").change(function(){
		// alert('===============')
		typeId = $(this).val();
		if (typeId == -1){

		}else{
			changeItem(typeId);
		}
	});

	$('#frm_add_content').submit(function(){
		var val = '[';
		var tmp = $("div#cascade_items div");
		var num = 0;
		var array = new Array();

		for(var i=0; i<tmp.length; i++){
			num++;
			var input = $("input[name^='item_']", tmp[i]).val();
			var text = $("p", tmp[i]).attr('name');
			var indexed = $("input[name^='item_indexed_']", tmp[i]).prop('checked');

			var indexedStr = 0;
			if (!indexed){//没有选中时，再将状态置为未选中
				indexedStr = 1;
			}

			var item = new Item(text, input, indexedStr);
			array[i] = item;
		}

		alert(JSON.stringify(array));
		$("#itemValues").val(JSON.stringify(array));
		// return false;
	})
})
</script>
</head>
<body>
	<div class="box">
		<h1>添加内容</h1>
		<form name="frm_add_content" id="frm_add_content" action="add_content" method="post">
			<table>
				<tr>
					<td>名称：<input name="name" id="name">&nbsp;&nbsp;
						索引：<input type="checkbox" name="indexed" id="indexed">
						<input type="hidden" name="itemValues" id="itemValues">
					</td>
				</tr>
				<tr>
					<td>
					类型：<select name="types" id="types">
					<option value="-1">选择类型</option>
					% for type in types:
						<option value="{{type.id}}">{{type.name}}</option>
					% end
					</select>
					</td>
				</tr>
				<tr>
					<td><div id="cascade_items"></div></td>
				</tr>
				<tr>
					<td><input type="submit" value="提交"></td>
				</tr>
			</table>
		</from>
	</div>
</body>
</html>
