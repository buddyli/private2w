<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here -->        
    <div class="box"> <!-- Box begins here -->
        <h2>图片列表</h2>                           
        <!--Classical Table below, must be used with thead and tbody tags;-->
        <table cellspacing="0" cellpadding="0"><!-- Table -->
            <thead>
                <tr>
                    <th>路径</th>
                    <th>描述</th>
                    <th>录入时间</th>
                </tr>
            </thead>
                
            <tbody>
                %if data and 'items' in data:
                    % for item in data['items']:
                    <tr>
                        <td>
                           ${item['path'] if 'path' in item else '--'}
                        </td>
                        <td>${item['describe'] if 'describe' in item else '--'}</td>
                        <td>${item['addTimeStr'] if 'addTimeStr' in item else '--'}</td>
                       <!--<td>
                            <a class="edit" href="/to_modify_item?id=${item.id}">修改</a>
                        </td>
                        <td>
                            <a class="delete" href="/del_pic?id=${item.id}" onclick="javascript:return confirm('Yes or No?')">删除</a>
                        </td>-->
                    </tr>
                    % endfor
                %endif

            </tbody>
        </table><!-- END Table -->
        <div class="box">
            <!-- Page Navigation -->
            %if 'pagenation' in data:
            <ul class="paginator">
                %for p in data['pagenation']:
                <li class="${ 'current' if p == data['cur_page'] else ''}"><a href="/system/manager/list?page=${ p }${ '&_uniq=%s' % data['_uniq'] if '_uniq' in data else ''}">${ p }</a></li>
                %endfor
            </ul>
            %endif
        <!-- /Page Navigation -->
        </div>
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>