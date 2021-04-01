from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'API KEY HERE'
url = 'URL HERE'


authenticator = IAMAuthenticator(apikey)
ta = ToneAnalyzerV3(version='2017-09-21',
authenticator=authenticator)
ta.set_service_url(url)

chat = [
    {
    "text":"What a beautiful day to be the only club to have won the champions leagues in France.", 
    "user":"it's Marseille bébé"
    }, 
    {
    "text":"This sucks, we have invested more than 1 bilion euro into theses clowns and still haven't won any european championship", 
    "user":"yeah we suck"
    }
]
res = ta.tone_chat(chat).get_result()

print (res)
