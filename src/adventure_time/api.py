from tastypie import fields
from tastypie.resources import Resource
# from tastypie.bundle import Bundle
from adventure_time.models import World, Character


class CharacterResource(Resource):

    # Just like a Django ``Form`` or ``Model``, we're defining all the
    # fields we're going to handle with the API here.
    name = fields.CharField(attribute='name')
    age = fields.IntegerField(attribute='age')
    friends = fields.ToManyField('self', 'friends')
    enemies = fields.ToManyField('self', 'enemies')
    # world = fields.ToManyField('WorldResource', 'world')

    class Meta:
        queryset = Character.nodes.all()
        resource_name = 'character'

    # The following methods will need overriding regardless of your
    # data source.
    def detail_uri_kwargs(self, bundle_or_obj):
        import pdb; pdb.set_trace()
        kwargs = {}

        # if isinstance(bundle_or_obj, Bundle):
        #     kwargs['pk'] = bundle_or_obj.obj.name
        # else:
        #     kwargs['pk'] = bundle_or_obj.name

        return kwargs

    def get_object_list(self, request):
        import pdb; pdb.set_trace()
        return Character.nodes.all()

    def obj_get_list(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        return self.get_object_list(bundle.request)

    def obj_get(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        nodes = Character.nodes.filter(pk=kwargs['pk']).all()
        if nodes:
            return nodes[0]

    def obj_create(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        # bundle.obj = RiakObject(initial=kwargs)
        # bundle = self.full_hydrate(bundle)
        # bucket = self._bucket()
        # new_message = bucket.new(bundle.obj.uuid, data=bundle.obj.to_dict())
        # new_message.store()
        # return bundle
        pass

    def obj_update(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        # return self.obj_create(bundle, **kwargs)
        pass

    def obj_delete_list(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        # bucket = self._bucket()

        # for key in bucket.get_keys():
        #     obj = bucket.get(key)
        #     obj.delete()
        pass

    def obj_delete(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        # bucket = self._bucket()
        # obj = bucket.get(kwargs['pk'])
        # obj.delete()
        pass

    def rollback(self, bundles):
        import pdb; pdb.set_trace()
        pass


class WorldResource(Resource):

    # Just like a Django ``Form`` or ``Model``, we're defining all the
    # fields we're going to handle with the API here.
    pk = fields.CharField(attribute='pk')
    name = fields.CharField(attribute='name')
    inhabitant = fields.ToManyField(CharacterResource, 'inhabitant')

    class Meta:
        queryset = World.nodes.all()
        resource_name = 'world'

    # The following methods will need overriding regardless of your
    # data source.
    def detail_uri_kwargs(self, bundle_or_obj):
        import pdb; pdb.set_trace()
        kwargs = {}

        # if isinstance(bundle_or_obj, Bundle):
        #     kwargs['pk'] = bundle_or_obj.obj.name
        # else:
        #     kwargs['pk'] = bundle_or_obj.name

        return kwargs

    def get_object_list(self, request):
        import pdb; pdb.set_trace()
        return World.nodes.all()

    def obj_get_list(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        return self.get_object_list(bundle.request)

    def obj_get(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        # return World.nodes.filter(name=kwargs['pk'])
        pass

    def obj_create(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        # bundle.obj = RiakObject(initial=kwargs)
        # bundle = self.full_hydrate(bundle)
        # bucket = self._bucket()
        # new_message = bucket.new(bundle.obj.uuid, data=bundle.obj.to_dict())
        # new_message.store()
        # return bundle
        pass

    def obj_update(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        # return self.obj_create(bundle, **kwargs)
        pass

    def obj_delete_list(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        # bucket = self._bucket()

        # for key in bucket.get_keys():
        #     obj = bucket.get(key)
        #     obj.delete()
        pass

    def obj_delete(self, bundle, **kwargs):
        import pdb; pdb.set_trace()
        # bucket = self._bucket()
        # obj = bucket.get(kwargs['pk'])
        # obj.delete()
        pass

    def rollback(self, bundles):
        import pdb; pdb.set_trace()
        pass
