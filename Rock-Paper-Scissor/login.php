<?php
 if (isset($_POST['cancel'])){
   header("Location:index.php");
   return;
 }
 $salt = 'XyZzy12*_';
 $stored_hash = '1a52e17fa899cf40fb04cfc42e6352f1';
 $result = false;
 if ( isset($_POST['who']) && isset($_POST['pass']) ) {
    if ( strlen($_POST['who']) < 1 || strlen($_POST['pass']) < 1 ) {
        $result = "User name and password required";
    } else {
        $check = hash('md5', $salt.$_POST['pass']);
        if ( $check == $stored_hash ) {
            header("Location: game.php?name=".urlencode($_POST['who']));
            return;
        } else {
            $result = "Incorrect password";
        }
    }
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Pranith Rao's Login Page</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<div>
<h1>Please Login In</h1>
<?php
  if($result!=false);{
    echo('<p style="color: red;">'.htmlentities($result)."</p>\n");
  } ?>
<form method="post">
<label for="who">User Name</label>
<input type="text" name="who" size="20"/><br/>
<label for="pass">Password</label>
<input type="password" name="pass" size="20"/><br/>
<button type="submit">Log In</button>
<button type="submit" name="cancel">Cancel</button>
<p>For a password hint, view source and find a password hint in the HTML comments.</p>
<!-- Hint: The password is the three character name of the
programming language used in this class (all lower case)
followed by 123. -->
</div>
</body>
</form>
</html>
