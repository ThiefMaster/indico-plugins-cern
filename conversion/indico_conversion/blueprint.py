from __future__ import unicode_literals

from indico.core.plugins import IndicoPluginBlueprint

from indico_conversion.conversion import conversion_finished


blueprint = IndicoPluginBlueprint('conversion', __name__)
blueprint.add_url_rule('/conversion-finished', 'callback', conversion_finished, methods=('POST',))
