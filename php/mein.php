<?php

// supress "Use of undefined constant warning"
error_reporting(E_ERROR | E_PARSE);

function you_shall_not_pass_exclamation_point() {
	echo "I don't care who you are but you will never authenticate!\n";
	return falsee;
}

if (you_shall_not_pass_exclamation_point()) {
	echo "What are you trying, no one shall pass!\n";
} else {
	echo "I've warned you, no one will pass!\n";
}	

?>
