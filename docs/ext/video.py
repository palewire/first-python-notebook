# -*- coding: utf-8 -*-
"""
    ReST directive for embedding Youtube and Vimeo videos.

    There are two directives added: ``youtube`` and ``vimeo``. The only
    argument is the video id of the video to include.

    Both directives have three optional arguments: ``height`` and ``width``.

    Default height is 315 and default width is 560.

    Example::

        .. youtube:: anwy2MPT5RE
            :height: 315
            :width: 560

    :copyright: (c) 2012 by Danilo Bargen.
    :license: BSD 3-clause
"""
from __future__ import absolute_import
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class IframeVideo(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'height': directives.nonnegative_int,
        'width': directives.nonnegative_int,
    }
    default_width = 560
    default_height = 315

    def run(self):
        self.options['video_id'] = directives.uri(self.arguments[0])
        if not self.options.get('width'):
            self.options['width'] = self.default_width
        if not self.options.get('height'):
            self.options['height'] = self.default_height
        return [nodes.raw('', self.html % self.options, format='html')]


class Youtube(IframeVideo):
    html = '<div class="embed-container"><iframe src="https://www.youtube.com/embed/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowfullscreen class="youtube"></iframe></div>'


class Vimeo(IframeVideo):
    html = '<div class="embed-container"><iframe src="https://player.vimeo.com/video/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>'


def setup(builder):
    directives.register_directive('youtube', Youtube)
    directives.register_directive('vimeo', Vimeo)
