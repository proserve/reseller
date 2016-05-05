from api.google_analytics_api import Profile, GANewVisitors, GABounceRate, Accounts, GANewVisitorsBySource, \
    ConversionRates, Property
from api.intercom_api import TotalUsers, GrowthRate
from api.mixpanel_api import DailyNewUsers, ClicksByUsers, PeriodicallyActiveUsers, PeriodicallyActiveUsersGrowth, \
    PeriodicallyEngagedUsers, ChurnedUsers, LifeTimeChurnedUsers
from flask import Flask
from flask.ext.restful import Api

from handlers.auth.google import google_oauth2_callback

app = Flask(__name__)
api = Api(app)
api_root = '/report/api/v1.0'

api.add_resource(Profile, api_root + '/profile')
api.add_resource(Property, '/properties')
api.add_resource(GANewVisitors, '/new_visitors')
api.add_resource(GABounceRate, '/bounce_rate')
api.add_resource(Accounts, '/accounts')
api.add_resource(GANewVisitorsBySource, '/new_users_by_source')
api.add_resource(ConversionRates, '/conversion_rates')

api.add_resource(TotalUsers, '/total_users')
api.add_resource(GrowthRate, '/growth_rate')

api.add_resource(DailyNewUsers, '/daily_new_users')
api.add_resource(ClicksByUsers, '/click_by_users')
api.add_resource(ChurnedUsers, '/churned_users')
api.add_resource(LifeTimeChurnedUsers, '/life_time_churned_users')

api.add_resource(PeriodicallyActiveUsers, '/periodically_active_users')
api.add_resource(PeriodicallyActiveUsersGrowth, '/periodically_active_users_growth')
api.add_resource(PeriodicallyEngagedUsers, '/periodically_engaged_users')

app.add_url_rule('/auth/google', 'google_auth', google_oauth2_callback, methods=['GET', 'POST'])
