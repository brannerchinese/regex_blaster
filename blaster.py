#!/usr/bin/python3
# blaster.py
# David Prager Branner

"""Game to improve regex skills.

Computer generates "attack" string and possibly "noncombatant" string.

User generates "defense" regex pattern; must match "attack" but not
"noncombatant".
"""

# For later:
#  1. Handle near-identical entries:
#   a. evaluate by edit-distance;
#   a. handle by repeating attack string; repeat defense barred;
#   b. handle by delaying efficacy, thus increasing risk of hit (San's
#      suggestion); this requires implementing timing.
#  2. Generate progressively more complex attack strings. There are presumably
#     ways to do this formulaically. We should also try to create noncombatant
#     strings and attack strings in such a way as to be difficult to
#     distinguish.
#  3. In future we may want multiple attack and/or noncombatant strings.
#  4. Invalid defense string may lead to score reduction or other penalties.
#  5. Evaluate quality of defense for more scores or greater level increase.
#  6. Figure damage (from hits); it may affect time of defense's effect..
#  7. In addition to near-identical entries, entries consisting only of literal
#     letters plus a few wild-cards should also be subject to penalty.

import re
import random
import string

def main():
    # Set up variables
    score = 0
    level = 1
    damage = 10
    defense_record = set()
    defeated_attacks = []
    martyred_noncombatants = []
    while damage > 0:
        defense = None
        # Generate "attack" string (must be matched to avoid hit)
        attack = generate_string()
        # Generate "noncombatant" string (must be matched to avoid score-loss)
        noncombatant = generate_string()
        while True:
            # Report battle state.
            print('''Score {:>4} Level {:>4} Damage {:>4} Attack {:>10} '''
                    '''Non-c {:>10}'''.
                    format(score, round(level, 1), damage, attack, 
                        noncombatant), end=' ')
            # Collect "defense" (user regex).
            defense = input('load: ')
            # Check defense against past regexes; invalidate if found.
            if defense in defense_record:
                print('This defense has already been used.')
                continue
            else:
                defense_record.add(defense)
                break
        # Test defense against "attack" and "noncombatant".
        print('here')
        attack_successful = False
        collateral_damage = False
        try:
            match = re.search(defense, attack).group()
        except AttributeError:
            match = None
        if attack == match:
            attack_successful = True
        try:
            match = re.search(defense, noncombatant).group()
        except AttributeError:
            match = None
        if attack == match:
            collateral_damage = True
        if attack_successful and not collateral_damage:
            # Defeat attack
            print('Successful defense without non-combatant casualties.')
            defeated_attacks.append(attack)
            score += 1 * level
            level += .1
        elif collateral_damage:
            print('Non-combatant casualties!')
            # Assess penalty
            score -= 1 * level
        if not attack_successful:
            print('Defense failed!')
            # Hit increases damage
            damage -= 1

def generate_string():
    return ''.join([random.choice(string.ascii_letters) for i in range(5)])