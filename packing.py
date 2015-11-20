'''
This script will tell you what and how much to pack!
'''

days = 5

summer = {

	'change_daily': 
	{
		'briefs':1,
		'undershirt':0
	},

	'change_every_other': 
	{
		'polo_shirt':1, 
		'shorts':0,
		'socks':1,
		'night_shirts':0, 
		'athletic_shorts':0, 
		'night_pants':1, 
		'jeans/chinos':1, 
		'swimwear':1, 
		'sweater':1,
		'athletic_shirts':1, 
	},

	# 'formal_wear':
	# {
	# 	'black_shoes':0,
	# 	'suit':0,
	# 	'suit_pant':0,
	# 	'black_belt':0, 
	# 	'dress_shirt':0,
	# 	'kurta':0,
	# 	'kurta_scarf':0,
	# 	'kurta_sandals':0,
	# 	'tie':0,
	# 	'brown_belt':0, 

	# }

	'toiletries': 
	{
		'toothbrush':1, 
		'tongue':1, 
		'deodorant':1, 
		'soap':1, 
		'loofah':1, 
		'contacts/glasses':1, 
		'toothpaste':1, 
		'lotion/vaseline':1,
		'balm':1
	},

	'accessories': 
	{ 
		'sunglasses':1,
		'hat':1,
		'watch':1,
		'lock':0,
		'boat_shoes':0, 
		'sandals':0, 
		'umbrella':1, 
		'laundry_bag':1, 
		'sneakers':1, 
		'jacket':1,
		'gloves':1,
		'winter_cap':1
	},

	'electronics': 
	{
		'headphones/earbuds':1,
		'phone_charger':1,
		'laptop_charger':1,
		'rechargeable_batteries':0
	}

	# 'documentation': 
	# {
	# 	'passport':0
	# 	'global_entry':0,
	# }	

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