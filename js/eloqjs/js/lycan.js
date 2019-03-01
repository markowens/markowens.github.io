// lycanthrope (eloquent java)

let journal = [];

function addEntry(events, squirrel) {
	journal.push({events, squirrel});
}

function phi2(table) {
  return (table[3] * table[0] - table[2] * table[1]) /
    Math.sqrt((table[2] + table[3]) *
              (table[0] + table[1]) *
              (table[1] + table[3]) *
              (table[0] + table[2]));
}

function phi(table) {
	return (table[3] * table[0] - table[2] * table[1]) /
	Math.sqrt((table[2] + table[3]) * 
			  (table[0] + table[1]) *
			  (table[1] + table[3]) *
			  (table[0] * table[2]));
}



function main() {
	addEntry(["work", "touched tree", "pizza", "running", "television"], false);
	addEntry(["work", "ice cream", "cauliflower", "lasagna", "touched tree", 
		"brushed teeth"], false);
	addEntry(["weekend", "cycling", "break", "peanuts", "beer"], true);
	
}


console.log(phi([76, 9, 4, 1]));
console.log(phi2([76, 9, 4, 1]));
console.log(phi([76, 9, 4, 1]));
console.log(phi2([76, 9, 4, 1]));
//main();