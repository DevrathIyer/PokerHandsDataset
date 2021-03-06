import json

fout = open('/content/hands_valid.json', 'w')
with open('/content/hands.json', 'r') as f:
    total = 0
    good = 0
    line = f.readline()
    while line:
        hand = json.loads(line)
        if len(hand['pots']) == 4:
            if hand['num_players'] == 2:
                if 'pocket_cards' in hand['players'][0]:
                    if all(('pos' in p) and
                           ('pocket_cards' in p) and
                           p['pocket_cards'] for p in hand['players']):
                        good += 1
                        hand['time'] = hand['_id'].split('_')[1]
                        hand['id'] = good
                        del hand['hand_num'], hand['_id']
                        fout.write(json.dumps(hand) + '\n')
        total += 1
        p = (total - good) / total
        print('{} processed, {} valid, {:.2%} dropped'.format(total, good, p), end='\r')
        line = f.readline()

fout.close()
print('\nFinished.')
