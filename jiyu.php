<?php
echo "OK!\n";
//----------変更----------
$dsn = 'mysql:host=localhost:3306;dbname=trvvdmle_jiyu;charset=utf8mb4';
$username = 'trvvdmle_jiyu';
$password = 'Sakagamipaopao0628';
//------------------------
try {
    $pdo = new PDO($dsn,$username,$password);
    	// 静的プレースホルダを指定
	$pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
	// DBエラー発生時は例外を投げる設定
	$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}catch (PDOException $e) {
    echo $e->getMessage();
    exit;
}
$data=$_GET;
$sql = "INSERT INTO `data` (`full_black`, `full_red`, `full_hai`, `min_black`, `min_red`, `min_hai`, `son_h`, `son_l`) VALUES ('".$data["full_black"]."', '".$data["full_red"]."', '".$data["full_hai"]."', '".$data["min_black"]."', '".$data["min_red"]."', '".$data["min_hai"]."', '".$data["son_h"]."', '".$data["son_l"]."')";
$res = $pdo->query($sql);
echo $res;
