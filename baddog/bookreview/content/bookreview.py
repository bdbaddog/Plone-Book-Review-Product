"""Definition of the Book Review content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import newsitem
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from baddog.bookreview.interfaces import IBookReview
from baddog.bookreview.config import PROJECTNAME

BookReviewSchema = newsitem.ATNewsItem.schema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.LinesField('bookAuthors',
                     required=True,
                     searchable=True,
                     widget=atapi.LinesWidget(
                     rows=1,
                     label=u'Book Authors',
                     description=u"The author of the book being reviewed."),
                    ),



))
# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

#TODO REMOVE 
#BookReviewSchema['title'].storage = atapi.AnnotationStorage()
#BookReviewSchema['description'].storage = atapi.AnnotationStorage()
# End TODO

schemata.finalizeATCTSchema(BookReviewSchema, moveDiscussion=False)

#This must be after the finalizeATCTSchema() call
BookReviewSchema.changeSchemataForField('creators','default')

BookReviewSchema['creators'].widget.label = u'Review Author'
BookReviewSchema['creators'].widget.description = u'The user who reviewed this book'
BookReviewSchema['creators'].widget.rows = 1
BookReviewSchema['creators'].isMetadata=False
BookReviewSchema.moveField('bookAuthors',after='title')
BookReviewSchema.moveField('creators',after='bookAuthors')
#BookReviewSchema['creators'].schemata='default'

BookReviewSchema['imageCaption'].widget.visible=dict(edit='invisible')
BookReviewSchema.moveField('image',after='creators')
BookReviewSchema['image'].widget.label = u'Book Cover Image'
BookReviewSchema['image'].widget.description = u'Upload Book Cover thumbnail'

class BookReview(newsitem.ATNewsItem):
    """BUsed to hold users book reviews"""
    implements(IBookReview)

    meta_type = "BookReview"
    schema = BookReviewSchema

#TODO REMOVE 
#    title = atapi.ATFieldProperty('title')
#    description = atapi.ATFieldProperty('description')
# End TODO

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(BookReview, PROJECTNAME)
