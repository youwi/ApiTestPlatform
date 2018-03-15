/**
 * by www
 * @returns {{}}
 * @constructor
 * init(option):
//在指定DIV中生成一个表格。
	option //是一个配置对象，属性列表如下：
	id://需要设置为表格的Div的ID。
	header://一个存放表头列表的数组，如：['ID','姓名','年龄','性别','爱好']
	data://一个存放表格数据的二维数组，如：
	[
	  [1,'张三',24,'男','登山'],
	  [2,'李四',22,'男','画画'],
	  [3,'王五',43,'男','看电视'],
	  [4,'赵六',37,'男','敲代码'],
	  [5,'小玉',19,'女','读书']
	]
	title://表格的标题(可选，默认不显示标题)
	titleColor://标题颜色(可选，默认是黑色)
	titleSize://标题大小(可选，默认大小是16px)
	headerColor://表头字体颜色(可选，默认是黑色)
	headerSize://表头字体大小(可选，默认大小是16px)
	headerBgColor://表头背景颜色(可选)
	color://表格字体颜色(可选，默认是黑色)
	size://表格字体大小(可选，默认大小是16px)
	rowHeight://表格每一行的高度(可选)
	columnWidth://一个数字数组，每个数字代表表格每一列的宽度百分比(可选)
	evenBgColor://索引为偶数的行背景颜色(可选)
	oddBgColor://索引为奇数的行背景颜色(可选)
	align://表格对齐方式(可选，只能是'center','left','right'的其中一个)
	getValue(id,row,column)：//获取指定表格中第row行第column列的数据。
	setValue(id,row,column,value)：//设置指定表格中第row行第column列的数据。
	getValues(id)：//获取指定表格中的数据，以一个二维数组的形式返回。
	addRow(id,data)：//在指定的表格中添加一行新的数据，data是一个存放一行数据的数组。
	deleteRow(id,row)：//从指定的表格中删除第row行的数据。
	getRowCount(id)：//获取指定表格的记录数。
	render(id)://重新绘制表格。
 */

function Table() {
	var TClass = {};
	var Tool = {};
	var DataStore = {};
	var Option = {};
	Tool.createHeader = function(htmls, data) {
		htmls.push('<tr>');
		for (var i in data) {
			htmls.push('<th>' + data[i] + '</th>');
		}
		htmls.push('</tr>');
	};
	Tool.createRow = function(htmls, data) {
		htmls.push('<tr>');
		for (var i in data) {
			htmls.push('<td>' + data[i] + '</td>');
		}
		htmls.push('</tr>');
	};
	Tool.render = function(id, tag) {
		var htmls = [];
		var option = Option[id];
		if (option['title'] != null) {
			htmls.push('<div class="title">' + option['title'] + '</div>');
		}
		htmls.push('<table>');
		Tool.createHeader(htmls, DataStore[id]['header']);
		for (var i in DataStore[id]['data']) {
			Tool.createRow(htmls, DataStore[id]['data'][i]);
		}
		htmls.push('</table>');
		tag.empty().append(htmls.join(''));
		Tool.setStyle(id, tag);
	};
	Tool.setStyle = function(id, tag) {
		var option = Option[id];
		tag.find('.title').css({
			'font-weight': 'bold',
			'text-align': 'center',
			'color': option['titleColor'],
			'font-size': option['titleSize']
		});
		tag.find('table').css({
			'width': '100%'
		});
		tag.find('th').css({
			'color': option['headerColor'],
			'background-color': option['headerBgColor'],
			'font-size': option['headerSize'],
			'padding': "0 5px"

		});
		tag.find('tr td').css({
			'color': option['color'],
			'font-size': option['size'],
			'text-align': option['align'],
			'padding': "0 5px"
		});
		tag.find('tr:even td').css({
			'background-color': option['evenBgColor']
		});
		tag.find('tr:odd td').css({
			'background-color': option['oddBgColor']
		});
		if (option['rowHeight'] != null) {
			tag.find('tr').find('th:eq(0)').css('height', option['rowHeight']);
			tag.find('tr').find('td:eq(0)').css('height', option['rowHeight']);
		}
		if (option['columnWidth'] != null) {
			var td = tag.find('tr').find('th');
			$.each(td,
			function(i) {
				$(this).css('width', option['columnWidth'][i] + '%');
			});
		}
	};
	Tool.getValue = function(value, defalutValue) {
		if (typeof value == 'undefined') {
			return defalutValue;
		} else {
			return value;
		}
	};
	TClass.init = function(option) {
		var id = option['id'];
		var tag = $('#' + id);
		var header = option['header'];
		var data = option['data'];
		DataStore[id] = {
			header: header,
			data: data
		};
		Option[id] = {
			title: Tool.getValue(option['title'], null),
			titleColor: Tool.getValue(option['titleColor'], 'white'),
			titleSize: Tool.getValue(option['titleSize'], 16),
			headerColor: Tool.getValue(option['headerColor'], 'white'),
			headerBgColor: Tool.getValue(option['headerBgColor'], '#11251c'),
			headerSize: Tool.getValue(option['headerSize'], 16),
			color: Tool.getValue(option['color'], 'white'),
			size: Tool.getValue(option['size'], 16),
			align: Tool.getValue(option['align'], 'left'),
			evenBgColor: Tool.getValue(option['evenBgColor'], '#11251c'),
			oddBgColor: Tool.getValue(option['oddBgColor'], '#11251c'),
			rowHeight: Tool.getValue(option['rowHeight'], 34),
			columnWidth: Tool.getValue(option['columnWidth'], null)
		};
		Tool.render(id, tag);
	};
	TClass.getValue = function(id, row, column) {
		return DataStore[id]['data'][row - 1][column - 1];
	};
	TClass.setValue = function(id, row, column, value) {
		DataStore[id]['data'][row - 1][column - 1] = value;
	};
	TClass.getValues = function(id) {
		return DataStore[id]['data'];
	};
	TClass.addRow = function(id, data) {
		DataStore[id]['data'].push(data);
	};
	TClass.deleteRow = function(id, row) {
		DataStore[id]['data'].splice(row - 1, 1);
	};
	TClass.getRowCount = function(id) {
		return DataStore[id]['data'].length;
	};
	TClass.render = function(id) {
		Tool.render(id, $('#' + id));
	};
	return TClass;
}