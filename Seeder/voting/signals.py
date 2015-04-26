from django.dispatch import receiver
from django.db.models.signals import post_save

from voting import constants
from source.models import Source
from voting.models import VotingRound


@receiver(signal=post_save, sender=Source)
def create_voting_round(instance, created, **kwargs):
    """
        Creates a voting round after new Source is created.
    """
    if created:
        voting_round = VotingRound(source=instance)
        voting_round.save()


@receiver(signal=post_save, sender=VotingRound)
def process_voting_round(instance, created, **kwargs):
    """
        Edits Source according to decision made in voting round.
    """
    if not created:
        instance.source.state = constants.VOTE_TO_SOURCE[instance.state]
        instance.source.save()