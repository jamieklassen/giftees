import json
from django.core import serializers
from django.views.generic import base as djviews
from django.contrib.auth import models as djmodels
from app import models


class Wishlist(djviews.View):
    """
    URL: /api/wishlist/<id>?
    """
    def get(self, request, **kwargs):
        """
        GET (no id): returns authenticated user's personal wishlist
        GET (with id): returns list of available gifts for user with given id
        """
        profile_id = kwargs.get('id')
        if profile_id is None:
            user = models.UserProfile.objects.get(user=request.user)
            qs = models.Gift.objects.filter(wisher=user)
        else:
            user = models.UserProfile.objects.get(id=profile_id)
            qs = models.Gift.objects.filter(wisher=user)
            if user.user != request.user:
                qs = qs.filter(buyer=None)
        return json.loads(serializers.serialize('json', qs))

    def post(self, request):
        """
        POST (no id): creates new wishlist item for authenticated user
        """
        gift = models.Gift.objects.create(request.POST)
        gift.wisher = models.UserProfile.objects.get(user=request.user)
        gift.save()

    def delete(self, request, **kwargs):
        """
        DELETE (with id): destroy wishlist item with given id
        """
        gift_id = kwargs.get('id')
        gift = models.Gift.objects.get(id=gift_id)
        if gift.wisher == request.user:
            gift.delete()


class Giftees(djviews.View):
    """
    URL: /api/giftees/<id>?
    """
    def get(self, request, **kwargs):
        """
        GET (no id): returns authenticated user's list of giftees
        GET (with id): returns giftee with given id
        """
        profile_id = kwargs.get('id')
        if profile_id is None:
            user = models.UserProfile.objects.get(user=request.user)
            qs = user.buying_for.all()
        else:
            qs = models.UserProfile.objects.filter(id=profile_id)
        return json.loads(serializers.serialize('json', qs))

    def post(self, request, **kwargs):
        """
        POST (with id): adds user with given id to authenticated user's list of
                        giftees
        """
        profile_id = kwargs.get('id')
        this = models.UserProfile.objects.get(user=request.user)
        this.buying_for.add(models.UserProfile.get(id=profile_id))
        this.save()

    def delete(self, request, **kwargs):
        """
        DELETE (with id): removes user with given id from authenticated user's
                          list of giftees
        """
        profile_id = kwargs.get('id')
        this = models.UserProfile.objects.get(user=request.user)
        this.buying_for.remove(models.UserProfile.get(id=profile_id))
        this.save()


class Shopping(djviews.View):
    """
    URL: /api/shopping/<id>?
    """
    def get(self, request, **kwargs):
        """
        GET (no id): returns authenticated user's shopping list
        GET (with id): returns shopping list item with given id
        """
        gift_id = kwargs.get('id')
        if gift_id is None:
            qs = models.Gift.objects.filter(
                buyer=models.UserProfile.objects.get(user=request.user)
            )
        else:
            qs = models.Gift.objects.get(id=gift_id)
        return json.loads(serializers.serialize('json', qs))

    def put(self, request, **kwargs):
        """
        PUT (with id): update "bought" state for shopping list item
                       with given id
        """
        # TODO: authenticate the user; only buyer can change bought status
        bought = request.PUT.get('bought')
        gift_id = kwargs.get('id')
        gift = models.Gift.objects.get(id=gift_id)
        gift.bought = bool(int(bought))
        gift.save()

    def post(self, request, **kwargs):
        """
        POST (with id): add item with given id to authenticated
        user's shopping list
        """
        gift_id = kwargs.get('id')
        gift = models.Gift.objects.get(id=gift_id)
        gift.buyer = models.UserProfile.objects.get(user=request.user)
        gift.save()

    def delete(self, request, **kwargs):
        """
        DELETE (with id): removes shopping list item with given id
        """
        # TODO: authenticate user; only buyer can renege
        gift_id = kwargs.get('id')
        gift = models.Gift.objects.get(id=gift_id)
        gift.buyer = None
        gift.save()


class Users(djviews.View):
    """
    URL: /api/users
    """
    def get(self, request):
        """
        GET: return all registered users
        """
        qs = djmodels.User.objects.all()
        return json.loads(serializers.serialize('json', qs))
