<?php
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
    $file = fopen('../info/error_out.txt', 'w');
    fwrite($file, $jsondata); fclose($file);
}
elseif(isset($una))
{
    $data = array(
        'status' => 'error',
        'error' => $una
    );
    $jsondata = json_encode($DATA);
    $file = fopen('../info/error_out.txt', 'w');
    fwrite($file, $jsondata); fclose($file);
}
elseif(isset($time))
{
    $data = array(
        'status' => 'error',
        'error' => $time
    );
    $jsondata = json_encode($data);
    $file = fopen('../info/error_out.txt', 'w');
    fwrite($file, $jsondata); fclose($file);
}
elseif(isset($unk))
{
    $data = array(
        'status' => 'error',
        'error' => $unk
    );
    $jsondata = json_encode($data);
    $file = fopen('../info/error_out.txt', 'w');
    fwrite($file, $jsondata); fclose($file);
}
else
{
    $data = array(
        'status' => 'error',
        'error' => $sup
    );
    $jsondata = json_encode($data);
    $file = fopen('../info/error_out.txt', 'w');
    fwrite($file, $jsondata); fclose($file);
}
?>