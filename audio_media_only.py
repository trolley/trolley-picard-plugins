PLUGIN_NAME = u"Separate audio and video medium count"
PLUGIN_AUTHOR = u"Mark Trolley"
PLUGIN_DESCRIPTION = u'''Separates the count of audio mediums and video mediums
for a release. With this plugin you can use %_totalaudiomedia% and/or
%_totalvideomedia% instead of %totaldiscs% in your file name formatting.'''
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["1.0.0"]

from picard.metadata import register_album_metadata_processor
import re


video_mediums = [ u"DVD", u"DVD-Video", u"Blu-ray", u"HD-DVD", u"Videotape",
                  u"VHS", u"Betamax", u"VCD", u"CDV", u"SVCD", u"LaserDisc" ]


def count_release_mediums(tagger, metadata, release):
    total_media = int(release.medium_list[0].count)
    total_video_media = 0
    for medium in release.medium_list[0].medium:
        if (medium.format[0].text in video_mediums):
            total_video_media += 1
    metadata["~totalvideomedia"] = total_video_media
    metadata["~totalaudiomedia"] = total_media - total_video_media


register_album_metadata_processor(count_release_mediums)
