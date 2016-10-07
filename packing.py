import argparse

parser = argparse.ArgumentParser(description='Inputs for creating a vacation packing checklist')
parser.add_argument('event', type=str, help='indicator of event you\'re going to')
parser.add_argument('days', type=int, help='number of days you\'re traveling')
args = parser.parse_args()
event = args.event
days = args.days

categories = {

    'change_daily':
    {
        'briefs': 1,
        'undershirt': 1
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

    'toiletries':
    {
        'toothbrush': 1,
        'tongue': 1,
        'deodorant': 1,
        'soap': 1,
        'loofah': 1,
        'contacts/glasses': 1,
        'toothpaste': 1,
        'lotion/vaseline': 1,
        'balm': 1
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
        'passport_holder': 1,
        'medicines': 1,
        'water_bottle': 1
    },

    'electronics':
    {
        'headphones/earbuds': 1,
        'camera/camera_charger/cards': 1,
        'phone_charger': 1,
        'laptop_charger': 1,
        'backup_cellphone': 1,
        'rechargeable_batteries': 1,
        'car_charger': 1,
        'car_phone_stand': 1,
        'luggage_scale': 1,
        'laptop': 1,
        'at&t_intl_plan': 1,
        'ipad': 1,
        'external_hd': 1
    },

    'documentation':
    {
        'passport': 1,
        'global_entry': 1,
        'luggage_tags': 1,
        'priority_pass': 1,
        'guidebook': 1,
        'cash': 1,
        'checks': 1
    }

}

if event = 'wedding':

    packing_categories = ['change_daily', 'change_every_other', 'toiletries', 'formal_wear']

elif event = 'beach':

    packing_categories = ['change_daily', 'change_every_other', 'toiletries']

elif event = 'domestic':

    packing_categories = ['change_daily', 'change_every_other', 'toiletries']

elif event = 'international':

    packing_categories = ['change_daily', 'change_every_other', 'toiletries']

for category, item in summer.iteritems():

    print ''
    print '----------------'
    print category
    print '----------------'

    for item, volume in item.iteritems():
        if volume == 0:
            continue
        if category == 'change_daily':
            volume = volume * days
        if category == 'change_every_other':
            volume = volume * days / 2
        print '%s: %s' % (item, volume)

print ''