import os
import requests

from logging import getLogger
from datetime import datetime

from django.db.models import Q
from django.conf import settings
from django.utils import timezone

from source import constants
from source.models import Source


logger = getLogger('screenshots.generator')


def take_screenshots():
    """
    Downloads all the screenshots
    """

    now = timezone.now()
    sources = Source.objects.filter(
        Q(screenshot_date__lte=now - constants.SCREENSHOT_MAX_AGE) |
        Q(screenshot__isnull=True)
    )

    for source in sources:
        msg = 'Generating screenshot for {0}'.format(source.id)
        print(msg)

        logger.info(msg)
        screenshot_name = '{pk}_{date}.png'.format(
            pk=source.pk, date=now.strftime('%d%m%Y')
        )

        # relative path is expected in FileField.name
        relative_path = os.path.join(constants.SCREENSHOT_DIR,
                                     screenshot_name)
        absolute_path = os.path.join(settings.MEDIA_ROOT, relative_path)

        r = requests.get(settings.MANET_URL, params={
            'url': source.main_seed.url,
            'width': constants.SCREENSHOT_RESOLUTION_X,
            'height': constants.SCREENSHOT_RESOLUTION_Y,
            'clipRect': constants.SCREENSHOT_RECTANGLE,
            'format': 'png',
            'delay': 1000
        })

        if r.status_code == requests.codes.ok:
            with open(absolute_path, 'wb') as screen:
                screen.write(r.content)

            source.screenshot.name = relative_path
            source.screenshot_date = now
            source.save()
