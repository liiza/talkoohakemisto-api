import colander
from sqlalchemy.orm.exc import NoResultFound

from .models import Municipality, VoluntaryWorkType


class MunicipalityType(colander.Integer):
    def deserialize(self, node, cstruct):
        code = super(MunicipalityType, self).deserialize(node, cstruct)
        if code is colander.null:
            return colander.null
        try:
            return Municipality.query.filter_by(code=code).one()
        except NoResultFound:
            raise colander.Invalid(
                node,
                '{0!r} is not a valid municipality ID'.format(code)
            )


class VoluntaryWorkTypeType(colander.Integer):
    def deserialize(self, node, cstruct):
        id = super(VoluntaryWorkTypeType, self).deserialize(node, cstruct)
        if id is colander.null:
            return colander.null
        try:
            return VoluntaryWorkType.query.filter_by(id=id).one()
        except NoResultFound:
            raise colander.Invalid(
                node,
                '{0!r} is not a valid type ID'.format(id)
            )


class VoluntaryWorkLinksSchema(colander.MappingSchema):
    municipality = colander.SchemaNode(MunicipalityType())
    type = colander.SchemaNode(VoluntaryWorkTypeType())


class VoluntaryWorkSchema(colander.MappingSchema):
    name = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(min=1, max=100)
    )
    organization = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(min=1, max=100)
    )
    url = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(min=1, max=100)
    )
    location = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(min=1, max=100)
    )
    street_address = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(max=100)
    )
    time = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(min=1, max=100)
    )
    goal = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(min=1, max=10000)
    )
    description = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(max=10000)
    )
    hashtag = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(min=1, max=100)
    )
    organizer = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(min=1, max=100)
    )
    contact_email = colander.SchemaNode(
        colander.String(),
        validator=colander.All(
            colander.Email(),
            colander.Length(min=4,max=100)
        )
    )
    contact_phone = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(min=1, max=100)
    )
    picture_url = colander.SchemaNode(
        colander.String(),
        missing=u'',
        validator=colander.Length(min=1, max=100)
    )
 
    links = VoluntaryWorkLinksSchema()


class VoluntaryWorkListSchema(colander.MappingSchema):
    voluntary_works = colander.SchemaNode(
        colander.Sequence(),
        VoluntaryWorkSchema(),
        validator=colander.Length(min=1, max=1)
    )
