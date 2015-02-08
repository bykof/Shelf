from django.db.models.fields.related import RelatedField

from rest_framework import metadata


class OrderMetadata(metadata.BaseMetadata):
    def determine_metadata(self, request, view):
        choices = {}
        for field in view.get_serializer_class().Meta.model._meta.fields:
            if isinstance(field, RelatedField) or field.name == 'status':
                if '_ptr' not in field.name:
                    for model_id, display_name in field.get_choices(include_blank=False):
                        if field.name not in choices:
                            choices[field.name] = [{'id': model_id, 'display_name': display_name}]
                        else:
                            choices[field.name].append({'id': model_id, 'display_name': display_name})
        return {
            'choices': choices,
        }