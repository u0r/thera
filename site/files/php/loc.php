<?php
$lat = $_POST['LAT'];
$lon = $_POST['LON'];

$data = array(
    'status' => 'ok',
    'lat' => $lat,
    'lon' => $lon
);

$josndata = json_encode($data);
$file = fopen('../info/out.txt', 'w');
fwrite($file, $josndata); fclose($file);
?>