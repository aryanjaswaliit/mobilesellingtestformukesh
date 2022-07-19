<?php
//this program is writte by aryan jaswla on 19 july 2022
$user=  $_REQUEST["user"];
$passw = $_REQUEST["passw"];

if ($user == "aryan")
{
	if($passw == "aryan"){
		echo "HEllo Aryan Jaswa 	you are  login";
	}else{
		echo "bad password";
	}
}else{
	echo "bad user id";
}
?>