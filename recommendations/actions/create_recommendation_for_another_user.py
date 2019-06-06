from recommendations.models import Recommendation, User, TrustedUser
from recommendations.sms_sender import SmsSender

class CreateRecommendationForAnotherUser: 

    @classmethod
    def execute(cls, payload):
        recommender = User.objects.get(phone=payload['recommender_phone'])
        recommendee = User.objects.get(username=payload['recommendee_username'])
        is_trusted = recommender.is_trusted_by(recommendee)
        recommendation = Recommendation(recommender=recommender, recommendee=recommendee, name=payload['name'], accepted=is_trusted)
        
        recommendation.full_clean()
        recommendation.save()

        if is_trusted: 
            SmsSender.send_to_user(recommendee, f"{recommender.username} recommended '{recommendation.name}' to you.")
        else: 
            SmsSender.send_to_user(recommendee, f"{recommender.username} recommended '{recommendation.name}' to you. Text back 'r{recommendation.id}' if you would like to add this recommendation and them as a trusted user?")            
        return {'message': f"'{recommendation.name}' was recommended to {recommendee.username}."}

   