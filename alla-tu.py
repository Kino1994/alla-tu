import random

def alla_tu_simulation(iterations=1000000, boxes=22, box_order=None, switch=True):
    if box_order is None and switch is True:
        raise ValueError("Please provide the box order in which the player can switch boxes.")
           
    wins = 0
           
    for _ in range(iterations):
        if box_order is None and switch is False:
            max_prize_box = random.randint(1, boxes)
            player_box = random.randint(1, boxes)
            if player_box == max_prize_box:
                wins = wins + 1
        else:
            i = boxes
            boxes_remaining = list(range(1, boxes + 1))
            openable_boxes = list(range(1, boxes + 1))
            max_prize_box = random.randint(1, boxes)
            player_box = random.randint(1, boxes)
            previous_box = player_box
            openable_boxes.remove(player_box)
            switched_boxes = [player_box]
            while len(boxes_remaining) > 1 and len(openable_boxes) > 0 and len(switched_boxes) < len(box_order):
                if i in box_order and previous_box != player_box:
                    selected_box = previous_box
                else:
                    selected_box = random.choice(openable_boxes)
                if selected_box == max_prize_box:
                    break
                else:
                    boxes_remaining.remove(selected_box)
                    openable_boxes.remove(selected_box)
                i = i - 1
                if i in box_order:
                    boxes_remaining.append(player_box)
                    openable_boxes.append(player_box)
                    previous_box = player_box
                    player_box = random.choice([box for box in boxes_remaining if box in openable_boxes and box not in switched_boxes])
                    switched_boxes.append(player_box)

            if player_box == max_prize_box:
                wins = wins + 1
                    
    
    return wins, iterations - wins, wins/iterations, 1 - (wins/iterations) 
    
results_case_no_switch = alla_tu_simulation(switch = False)
results_case1_switch = alla_tu_simulation(box_order=[16, 10, 4], switch=True)
results_case2_switch = alla_tu_simulation(box_order=[16, 11, 7, 4, 2], switch=True)
results_case3_switch = alla_tu_simulation(box_order=[19, 16, 13, 10, 7, 4], switch=True)
results_case4_switch = alla_tu_simulation(box_order=[19, 16, 13, 10, 7, 4, 2], switch=True)

print(results_case_no_switch)
print(results_case1_switch)
print(results_case2_switch)
print(results_case3_switch)
print(results_case4_switch)
