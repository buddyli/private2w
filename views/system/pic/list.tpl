<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here -->        
    <div class="box"> <!-- Box begins here -->
        <h2>图片列表</h2>                           
        <!--Classical Table below, must be used with thead and tbody tags;-->
        <table cellspacing="0" cellpadding="0"><!-- Table -->
            <thead>
                <tr>
                    <th>名称</th>
                    <th>索引</th>
                    <th>录入时间</th>
                    <th>操作</th>
                </tr>
            </thead>
                
            <tbody>
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