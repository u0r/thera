if(navigator.geolocation)
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
        url:'/files/php/loc.php',
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
        url:'/files/php/error.php',
        data:{
            DEN:den,
            UNA:una,
            TIME:time,
            UNK:unk}
        });
}