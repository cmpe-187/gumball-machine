# gumball-machine

A virtual gumball machine.

## Test Cases

### NoCurrencyTestCases

These test cases focus on inserting no currency into the machine and attempting to dispense gumballs and returning change.

| Test Name             | Input Vector           | Expected Output                                           |
| --------------------- | ---------------------- | --------------------------------------------------------- |
| test_dispense_red     | <`dispense_red()`>     | "You need at least 5 cents to dispense a red gumball"     |
| test_dispense_yellow  | <`dispense_yellow()`>  | "You need at least 10 cents to dispense a yellow gumball" |
| test_return_my_change | <`return_my_change()`> | "There is no change to return"                            |

### ReturnValidCurrencyTestCases

These test cases focus on inserting valid currency into the machine and returning change.

| Test Name           | Input Vector                                | Expected Output                     |
| ------------------- | ------------------------------------------- | ----------------------------------- |
| test_return_nickel  | <`insert("nickel")`, `return_my_change()`>  | "Returning your change of 5 cents"  |
| test_return_dime    | <`insert("dime")`, `return_my_change()`>    | "Returning your change of 10 cents" |
| test_return_quarter | <`insert("quarter")`, `return_my_change()`> | "Returning your change of 25 cents" |

### ExactCurrencyTestCases

These test cases focus on inserting exact, valid currency into the machine and dispensing gumballs.

| Test Name                           | Input Vector                                                  | Expected Output             |
| ----------------------------------- | ------------------------------------------------------------- | --------------------------- |
| test_insert_nickel_dispense_red     | <`insert("nickel")`, `dispense_red()`>                        | "Enjoy your red gumball"    |
| test_insert_dime_dispense_yellow    | <`insert("nickel")`, `dispense_yellow()`>                     | "Enjoy your yellow gumball" |
| test_insert_nickels_dispense_yellow | <`insert("nickel")`, `insert("nickel")`, `dispense_yellow()`> | "Enjoy your yellow gumball" |

### InvalidCurrencyTestCases

These test cases focus on inserting invalid currency into the machine and attempting to dispense gumballs and returning change.

| Test Name                          | Input Vector                                                   | Expected Output                                     |
| ---------------------------------- | -------------------------------------------------------------- | --------------------------------------------------- |
| test_return_dollar                 | <`insert("dollar")`, `return_my_change()`>                     | "Returning your invalid currency of dollar"         |
| test_return_dollars                | <`insert("dollar")`, `insert("dollar")`, `return_my_change()`> | "Returning your invalid currency of dollar, dollar" |
| test_insert_dollar_dispense_red    | <`insert("dollar")`, `dispense_red()`>                         | "Returning your invalid currency of dollar"         |
| test_insert_dollar_dispense_yellow | <`insert("dollar")`, `dispense_yellow()`>                      | "Returning your invalid currency of dollar"         |

### MultipleGumballsExactCurrencyTestCases

These test cases focus on inserting exact, valid currency multiple gumballs.

| Test Name                            | Input Vector                                                                                                                                     | Expected Output                |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| test_insert_nickels_dispense_reds    | <`insert("nickel")`, `insert("nickel")`, `dispense_red()`, `dispense_red()`, `return_my_change()`>                                               | "There is no change to return" |
| test_insert_dime_dispense_reds       | <`insert("dime")`, `dispense_red()`, `dispense_red()`, `return_my_change()`>                                                                     | "There is no change to return" |
| test_insert_nickels_dispense_yellows | <`insert("nickel")`, `insert("nickel")`, `insert("nickel")`, `insert("nickel")`, `dispense_yellow()`, `dispense_yellow()`, `return_my_change()`> | "There is no change to return" |
| test_insert_dimes_dispense_yellows   | <`insert("dime")`, `insert("dime")`, `dispense_yellow()`, `dispense_yellow()`, `return_my_change()`>                                             | "There is no change to return" |
