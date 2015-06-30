''' Automatically compare campaigns '''

import os
import random
import datetime
import sys
import json
import math
import decimal
from sqlalchemy import create_engine

'''
Execute query through this function
'''

def executeEquateQuery(query):

    engine = create_engine('postgresql://equate_super:rnDfc9Zo0@equatepg.cogolo.net:5432/postgres')
    c = engine.connect() 
    trans = c.begin()
    rows = c.execute(query)
    trans.commit()
    return rows

''' 
The campaign class pulls out engagement data for Equate campaigns on specific days 
'''

class Campaign(object):

    def __init__(self, campaign_name, date_interval_1, date_interval_2, success, ci_percentage):

		self.campaign_name = campaign_name
		self.date_interval_1 = date_interval_1
		self.date_interval_2 = date_interval_2
		self.query_selection = ''' select json_extract_path_text, sum(sends), sum(deliveries), sum(opens), sum(clicks), sum(complaints) from va_campaign_performance_crunch where json_extract_path_text = '%s' and date >= '%s' and date <= '%s' group by 1''' % (self.campaign_name, self.date_interval_1, self.date_interval_2)
		self.success = success
		self.ci_percentage = ci_percentage

		'''
		Pull out data for identified success measure
		'''

		self.id_output = executeEquateQuery(self.query_selection)
		self.data_row = tuple(self.id_output)
		self.send_count = float(self.data_row[0][2])

		'''
		Create a function to calculate all relevant metrics prior to running CampaignComparison
		'''

		if self.success == 'open': self.success_count = float(self.data_row[0][4])
		if self.success == 'click': self.success_count = float(self.data_row[0][5])

		self.sr = self.success_count/self.send_count

		'''
		Generate 75/90/95/99 percent confidence interval for experiment
		'''

		if self.ci_percentage == 0.75: self.z_score = 1.15
		if self.ci_percentage == 0.90: self.z_score = 1.645
		if self.ci_percentage == 0.95: self.z_score = 1.96
		if self.ci_percentage == 0.99: self.z_score = 2.58

		self.bound = self.z_score * float(math.sqrt(self.success_count))/self.send_count
		self.lower_bound = self.sr - self.bound
		self.upper_bound = self.sr + self.bound

		self.writer = ''' insert into yahoo_campaign_results (campaign_name, run_date, test_start, test_end, sends, success, sr, ci_lower, ci_upper, confidence_interval, success_measure)
			select '%s', current_date, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'
			''' % (self.campaign_name, self.date_interval_1, self.date_interval_2, int(self.send_count), int(self.success_count), self.sr, self.lower_bound, self.upper_bound, self.ci_percentage, self.success)

''' 
CampaignComparison ingests a series of campaigns and identifies the following:
1) Do you have enough click data to make a conclusion on sr? Go through campaign and print Y or N
2) Calculate the sr for campaigns you've input and create the confidence bounds
3) Output if difference in sr is statistically different
'''

def CampaignComparison(campaign_id1,campaign_id2):

	print ''

	if campaign_id1.campaign_name:

		if campaign_id1.success_count > 30:

			print "Campaign %s has enough %s data: %s" % (campaign_id1.campaign_name, campaign_id1.success ,campaign_id1.success_count)
			print "Campaign %s %s-rate is %s" % (campaign_id1.campaign_name, campaign_id1.success, '{percent:.5%}'.format(percent = campaign_id1.sr))
			print "Campaign %s confidence interval is (%s, %s)" % (campaign_id1.campaign_name, '{percent:.5%}'.format(percent = campaign_id1.lower_bound), '{percent:.5%}'.format(percent = campaign_id1.upper_bound))

		else:

			print "Campaign %s does not have enough successes" % campaign_id1.campaign_name

	print ''

	if campaign_id2.campaign_name:

		if campaign_id2.success_count > 30:

			print "Campaign %s has enough %s data: %s" % (campaign_id2.campaign_name, campaign_id2.success ,campaign_id2.success_count)
			print "Campaign %s %s-rate is %s" % (campaign_id2.campaign_name, campaign_id2.success, '{percent:.5%}'.format(percent = campaign_id2.sr))
			print "Campaign %s confidence interval is (%s, %s)" % (campaign_id2.campaign_name, '{percent:.5%}'.format(percent = campaign_id2.lower_bound), '{percent:.5%}'.format(percent = campaign_id2.upper_bound))

		else:

			print "Campaign %s does not have enough successes" % campaign_id2.campaign_name

	print ''

	if ((campaign_id2.lower_bound <= campaign_id1.lower_bound <= campaign_id2.upper_bound) or (campaign_id2.lower_bound <= campaign_id1.upper_bound <= campaign_id2.upper_bound)):

		print "Campaign %s and campaign %s are not statistically different at a %s percent confidence level" % (campaign_id1.campaign_name, campaign_id2.campaign_name, campaign_id1.ci_percentage*100)

	else:

		print "Campaigns are statistically different at a %s percent confidence level" % (campaign_id1.ci_percentage*100)
		print ''

'''
Write the output of campaigns into Equate PG
'''

def CampaignWriter(campaign_id1,campaign_id2):

	executeEquateQuery(campaign_id1.writer)
	executeEquateQuery(campaign_id2.writer)	

	print "Campaigns have written to Equate DB"
	print ''

if __name__ == '__main__':

	campaign_1 = Campaign('prepop-health', '2015-04-08', '2015-04-15', 'click', 0.95)
	campaign_2 = Campaign('test-life4', '2015-04-11', '2015-04-13', 'click', 0.75)
	campaign_3 = Campaign('health-daily', '2015-04-08', '2015-04-15', 'click', 0.95)

	CampaignComparison(campaign_1, campaign_3)
	CampaignWriter(campaign_1, campaign_3)

