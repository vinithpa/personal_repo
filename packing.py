'''
This script will tell you what and how much to pack!
'''

days = 5

summer = {

	'change_daily': 
	{
		'briefs':0,
		'undershirt':0
	},

	'change_every_other': 
	{
		'polo_shirt':0, 
		'shorts':0,
		'socks':0,
		'night_shirts':0, 
		'athletic_shorts':0, 
		'night_pants':0, 
		'jeans/chinos':0, 
		'swimwear':0, 
		'sweater':0,
		'athletic_shirts':0, 
	},

	'formal_wear':
	{
		'black_shoes':0,
		'suit':0,
		'suit_pant':0, 
		'dress_shirt':0,
		'kurta':0,
		'kurta_scarf':0,
		'kurta_sandals':0,
		'tie':0, 
	},

	'toiletries': 
	{
		'toothbrush':0, 
		'tongue':0, 
		'deodorant':0, 
		'soap':0, 
		'loofah':0, 
		'contacts/glasses':0, 
		'toothpaste':0, 
		'lotion/vaseline':0,
		'balm':0
	},

	'accessories': 
	{ 
		'brown_belt':0,
		'black_belt':0,
		'sunglasses':0,
		'hat':0,
		'watch':0,
		'lock':0,
		'boat_shoes':0, 
		'sandals':0, 
		'umbrella':0, 
		'laundry_bag':0, 
		'sneakers':0, 
		'jacket':0,
		'gloves':0,
		'winter_cap':0,
		'knapsack':0
	},

	'electronics': 
	{
		'headphones/earbuds':0,
		'phone_charger':1,
		'laptop_charger':1,
		'rechargeable_batteries':0,
		'car_charger':1
	},

	'documentation': 
	{
		'passport':0,
		'global_entry':0,
	}	

}

for category,item in summer.iteritems():

	print ''
	print '----------------'
	print category
	print '----------------'

	for item, volume in item.iteritems():
		if volume == 0: continue
		if category == 'change_daily': 
			volume = volume * days
		if category == 'change_every_other': 
			volume = volume * days/2
		print '%s: %s' % (item, volume)

print ''