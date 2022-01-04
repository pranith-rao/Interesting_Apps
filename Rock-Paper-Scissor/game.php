<?php
if (!isset($_GET['name']) || strlen($_GET['name']) < 1){
  echo "Name Parameter missing";
  return;}

if (isset($_POST['logout'])){
  header("location:index.php");
  return;
}

$names = array('Rock','Paper','Scissors');
$human = isset($_POST["human"]) ? $_POST['human']+0 : -1;
$computer = rand(0,2);
function check($human,$computer){
  if($human == $computer){
    return "Tie";
  }
  else if($human == 0 AND $computer == 2 ){
      return "You Win";
  }
  else if($human == 0 AND $computer == 1 ){
      return "You lose";
  }
  else if($human == 1 AND $computer == 2 ){
      return "You lose";
  }
  else if($human == 1 AND $computer == 0 ){
      return "You Win";
  }
  else if($human == 2 AND $computer == 0 ){
    return "You Lose";
  }
  else if($human == 2 AND $computer == 1 ){
    return "You Win";
  }
  return false;
}
$result = check($human,$computer );
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Pranith Rao-Rock Paper Scissors</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Rock Paper Scissors</h1>
  <?php
  if (isset($_REQUEST['name'])){
    echo "<p>Welcome:";
    echo htmlentities($_REQUEST['name']);
    echo "</p>\n";
  } ?>
  <form method="post">
  <div><select name="human">
    <option value="-1">Select</option selected>
    <option value="0">Rock</option>
    <option value="1">Paper</option>
    <option value="2">Scissors</option>
    <option value="3">Test</option>
  </select>
  <button name="play">Play</button>
  <button name="logout">Logout</button>
<pre>
<?php
if ($human == -1){
    print "Please select a strategy and press Play.\n";
  }
  else if($human == 3){
    for($c=0;$c<3;$c++){
      for($h=0;$h<3;$h++){
        $r=check($c,$h);
        echo "Human=$names[$h] Computer=$names[$c] Result=$r\n";
      }
    }
  }
  else {
    print"Your Play=$names[$human] Computer Play=$names[$computer] Result=$result\n";
    }
?>
</pre>
</div>
</form>
</body>
</html>
