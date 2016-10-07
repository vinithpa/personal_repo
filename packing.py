import argparse
import pprint

def setup_parser():

    parser = argparse.ArgumentParser(description='Vacation packing checklist')
    parser.add_argument('--event', required = False, type=str, help='Event you\'re going to')
    parser.add_argument('--days', required = True, type=int, help='Number of travel days')
    return parser.parse_args()


args = setup_parser()
event = args.event
days = args.days


def looper(decompose_hash):

    for x, y in decompose_hash.iteritems():

        yield [x, y]


def hash_multiplier(input_hash, days):
    print ''
    output_hash = {}
    for a, b in input_hash.iteritems():

        output_hash[a] = b * days

    return output_hash


categories = {

    'necessary':
    {
        'daily':
        {
            'briefs': 1,
            'undershirt': 1
        },
        'once':
        {
            'toothbrush': 1,
            'tongue': 1,
            'deodorant': 1,
            'soap': 1,
            'loofah': 1,
            'contacts/glasses': 1,
            'toothpaste': 1,
            'lotion/vaseline': 1,
            'balm': 1,
            'headphones/earbuds': 1,
            'phone_charger': 1,
            'laptop_charger': 1,
            'cash': 1,
            'checks': 1,
            'laptop': 1,
            'keys': 1,
            'wallet': 1
        }
    },

    'change_every_other':
    {
        'polo_shirt': 1,
        'shorts': 1,
        'socks': 1,
        'athletic_shorts': 1,
        'jeans/chinos': 1,
        'swimwear': 1,
        'sweater': 1,
        'athletic_shirts': 1,
        'night_shirts': 1,
        'night_pants': 1,
    },

    'accessories':
    {
        'brown_belt': 1,
        'black_belt': 1,
        'sunglasses': 1,
        'hat': 1,
        'watch': 1,
        'lock': 1,
        'boat_shoes': 1,
        'sandals': 1,
        'umbrella': 1,
        'laundry_bag': 1,
        'sneakers': 1,
        'jacket': 1,
        'gloves': 1,
        'winter_cap': 1,
        'knapsack': 1,
        'pen': 1,
        'medicines': 1,
        'water_bottle': 1
    },

    'formal_wear':
    {
        'black_shoes': 1,
        'suit': 1,
        'suit_pant': 1,
        'dress_shirt': 1,
        'kurta': 1,
        'kurta_scarf': 1,
        'kurta_sandals': 1,
        'tie': 1,
    },

    'long_term_electronics':
    {
        'backup_cellphone': 1,
        'luggage_scale': 1,
        'at&t_intl_plan': 1,
        'ipad': 1,
        'external_hd': 1,
        'camera/camera_charger/cards': 1,
        'rechargeable_batteries': 1,
        'car_charger': 1,
        'car_phone_stand': 1,
    },

    'long_term_documentation':
    {
        'passport': 1,
        'passport_holder': 1,
        'global_entry': 1,
        'luggage_tags': 1,
        'priority_pass': 1,
        'guidebook': 1,

    }

}

necessary_daily = hash_multiplier(categories['necessary']['daily'], days)
pprint.pprint(necessary_daily)
necessary_once = hash_multiplier(categories['necessary']['once'], 1)
pprint.pprint(necessary_once)
every_other = hash_multiplier(categories['change_every_other'], days / 2)
pprint.pprint(every_other)
accessories = hash_multiplier(categories['accessories'], 1)
pprint.pprint(accessories)

if event == 'wedding':

    formal_wear = hash_multiplier(categories['formal_wear'], 1)
    pprint.pprint(formal_wear)

elif event == 'long_term':

    long_term_electronics = hash_multiplier(categories['long_term_electronics'], 1)
    pprint.pprint(long_term_electronics)
    long_term_documentation = hash_multiplier(categories['long_term_documentation'], 1)
    pprint.pprint(long_term_documentation)
