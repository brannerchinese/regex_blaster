## Regex Blaster

An arcade game to practice regular expressions.

---

### To do

 1. Item gradually fading into or out of view. Useful for hits.

 1. Display attack/noncombatant string and strings.

 1. Apply regex to attack string and non-combatant strings, showing partial matches in real time.

 1. Handle failed attack and non-combatant strings.

 1. Multiple attack and/or noncombatant strings. More points for multiple matches at once.

 1. Set background color: automatically black for now.

 1. User corrects regex offered by machine.

 1. Handle near-identical defenses:

  2. evaluate by edit-distance vis-à-vis all previous defenses; average  string-length minus edit-distance may be more useful than edit-distance alone.
  2. handle by repeating attack string; repeat defense barred;
  2. handle by delaying efficacy, thus increasing risk of hit (San's  suggestion); this requires implementing timing.

 1. Generate progressively more complex attack strings. There are presumably ways to do this formulaically. We should also try to create noncombatant strings and attack strings in such a way as to be difficult to distinguish.

 1. Invalid defense string may lead to score reduction or other penalties.

 1. Evaluate quality of defense for more scores or greater level increase.

 1. Figure damage (from hits); it may affect time of defense's effect..

 1. For more complex attacks, it may be interesting to repeat them just in order to see how many different defenses the user can supply. Keep repeating until user fails — or even a little after that.

 1. If \w appears a lot, add whitespace.

### Versions

 * 06 Control window size. Move message to `rjust()`.

 * 05 Color and label different sub-windows. Trap delete and CR control chars.

 * 04 Set up different sub-windows. Separate Timer class. Defense line.

 * 03 Get styled text working; no display delay on startup..

 * 02 Set up and close curses in special functions; always trap ctrl-c.

 * 01 Open window; close on two backticks.


[end]
