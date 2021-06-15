SOURCE_CONNECTION_STRING = 'SOURCE'
TARGET_CONNECTION_STRING = 'TARGET'

HTML_RANDOM_TEMPLATE = """
    <div style='padding:5px;background-color:#E1E2E1;
                border-radius: 8px 34px 9px 26px;
    -moz-border-radius: 8px 34px 9px 26px;
    -webkit-border-radius: 8px 34px 9px 26px;
    border: 2px ridge #000000;'>
    <img src="right.jpg" alt="Snow" style="width:100%">
    <p>{}  <img></p>
    <p>{}</p>
    <p>{}</p>
    </div>
"""

HTML_HEADER_TEMPLATE = '''
    <link rel="stylesheet"
          href="https://fonts.googleapis.com/css?family=Tangerine">
    <div style="font-family: 'Tangerine';font-size:48px;"><center><b>Data Comparison</b></center></div>
    <hr>
'''


HTML_SIDEBAR_TEMPLATE = """
    <style>
        .css-1aumxhk {
        background-color: #1e81b0;
        background-image: none;
        color: #eeeee4
        }
    </style>
"""

HTML_SIDEBAR_BUTTON_TEMPLATE = """
<style>
    .stButton>button {
    color: #21130d;
    background-color: #eeeee4;
    }
</style>
"""

HTML_SIDEBAR_DIV_CENTER_TEMPLATE = """
    <style>
        .css-hx4lkt {
        left: 0px; 
        right: 0px; 
        bottom: 0; 
        top: 0px; 
        padding: 1rem 1rem 1rem;
        }
    </style>
"""

HTML_SIDEBAR_DIV_WIDE_TEMPLATE = """
    <style>
        .css-18c15ts {
        left: 0px; 
        right: 0px; 
        bottom: 0; 
        top: 0px; 
        padding: 1rem 1rem 1rem;
        }
    </style>
"""

HTML_SUMMARY_FONT_IMAGE_TEMPLATE = """
    <style>
        .container {
            display: flex;
        }
        .logo-text {
            font-weight:bold !important;
            font-size:12px !important;
            color: #f9a01b !important;
            padding-top: 5px !important;
        }
        .logo-img {
            float:right;
            width:20px;
            height:20px;
        }
    </style>
"""

HTML_EXPAND_HEADER_TEMPLATE = """
    <style>
        .streamlit-expanderHeader{
            color:#063970
        }
    </style>
"""

HTML_SUMMARY_STATS_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Row count match:</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""

HTML_ROWCOUNT_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Row count match:</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""

HTML_COLCOUNT_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Column count match:</p>&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""

HTML_COLNAME_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Column name match:</p>&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""

HTML_DATATYPE_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Data type match:</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""

HTML_NULL_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Null type match:</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""

HTML_PK_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Primarykey match:</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""

HTML_FK_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Foreignkey match:</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""

HTML_IDX_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Index match:</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""
HTML_TRIGGER_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Triggers match:</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""

HTML_VIEWS_TICK_IMAGE_TEMPLATE = """
    <div class="container">
        <p class="logo-text">Views match:</p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img class="logo-img" src="data:image/png;base64,{}">
    </div>
"""
