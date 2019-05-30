<?php
    $ip = '127.0.0.1';
    $port = 5001;
    
    $problem = "";
    $pp = "";
    $get_data = "";
    if(!empty($_GET['problem']) && !empty($_GET['pp'])) {
        $problem = $_GET['problem'];
        $pp = $_GET['pp'];

        $get_data = "?problem=".urlencode($problem)."&pp=".urlencode($pp);
    }

    $ch = curl_init("http://".$ip.":".$port."/solution".$get_data);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    
    echo curl_exec($ch);
    curl_close($ch);
?>