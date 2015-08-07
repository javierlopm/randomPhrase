#!/usr/bin/perl

use Tie::File;
my @records;
tie @records, 'Tie::File', "diccionario.sql";

@culito = @records[0];

my $counter = 0;

foreach $line ( @records ) { 
	my @newline = split('×',$line);

	
	my $result = "INSERT INTO DICTIONARY VALUES(".$counter.",\'".@newline[0]."\');";
	
	my $final  = "";
	
	foreach $type (split //,@newline[1]){
		$insertstatement = "INSERT INTO PART_OF_SPEECH VALUES(".$counter.",\'".$type."\');";
		$final = $final . " " .$insertstatement;
	}
	
	$counter++;
	
	$finalstatemente = $result . $final;
	$line = $finalstatemente;

} 

untie @records;