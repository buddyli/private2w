<%inherit file="../system_base.tpl"/>

<%block name="content">
<div id="content"> <!-- Content begins here --> 
    <div class="box"> <!-- Box begins here -->
        <!--Standard form within a fieldset tag;-->
        <form method="post" action="/add_pic" enctype="multipart/form-data"><!-- Form -->
            <fieldset><legend>添加图片</legend>
                <div class="input_field">
                    <label for="b">选择</label>
                    <input type="file" name="file" id="file">
                    <span class="field_desc"> * Required</span>
                </div>
                <div class="input_field">
                    <label for="b">描述</label>
                    <input type="text" name="describe" id="describe">
                    <span class="field_desc"> Optional</span>
                </div>           
                <input class="submit" type="submit" value="提交" />
            </fieldset>
        </form><!-- /Form -->
    </div> <!-- END Box-->
</div> <!-- END Content -->
</%block>