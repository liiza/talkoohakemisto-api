from marshmallow import fields, Serializer


class MunicipalitySerializer(Serializer):
    id = fields.Integer(attribute='code')

    class Meta:
        fields = ('id', 'name')


class VoluntaryWorkTypeSerializer(Serializer):
    class Meta:
        fields = ('id', 'name')


class VoluntaryWorkLinksSerializer(Serializer):
    municipality = fields.Integer()
    type = fields.Integer()

    class Meta:
        fields = ('municipality', 'type')


class VoluntaryWorkSerializer(Serializer):
    links = fields.Nested(VoluntaryWorkLinksSerializer)

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            #'organizer',
            #'contact_email',
            'street_address',
            'links',
            'url',
            'hashtag',
            'location',
            'time',
            'goal',
            #'contact_phone',
            'organization',
            'picture_url',
            'lat',
            'lng'
        )

class VoluntaryWorkEditSerializer(Serializer):
    links = fields.Nested(VoluntaryWorkLinksSerializer)

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'organizer',
            'contact_email',
            'street_address',
            'links',
            'url',
            'hashtag',
            'location',
            'time',
            'goal',
            'contact_phone',
            'organization',
            'picture_url',
            'lat',
            'lng'
        )

