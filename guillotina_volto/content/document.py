# -*- encoding: utf-8 -*-
from guillotina import configure
from guillotina.content import Folder
from guillotina.directives import index
from guillotina_volto.interfaces import IDocument


@configure.contenttype(
    type_name="Document",
    schema=IDocument,
    behaviors=[
        "guillotina.behaviors.dublincore.IDublinCore",
        "guillotina_volto.interfaces.base.ICMSBehavior",
    ],
    allowed_types=["Image", "File"],  # dynamically calculated
)
class Document(Folder):
    pass

