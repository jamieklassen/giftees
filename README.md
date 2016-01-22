## Problem

I have a large family. At Christmas time, there are a lot of gifts to
buy, and therefore a lot of gifts to receive. There are so many people
relative to the size of the average wish list that the risk of a
gift-choice collision is unacceptable -- people can't be getting the
same gift from multiple people! Therefore, everyone *but* the person
receiving gifts should collaborate on choices from the person's
wishlist. How can we make this easy? email is hard because it requires
long chains of responses and the careful attention to who is on the
receiving list to ensure the giftee doesn't see who's getting them
what. Really it's a fascinating exercise in game theory or something
I imagine.

## Objectives

* we want to manage the people we're buying gifts for; a to-gift list
* more importantly, we want to manage their wishlists
* we want an easy place to store our gift choices - like a gift
  registry - so we can share them with other people planning to buy
  them gifts
* The gift registry entries should be INVISIBLE to the giftee
* People are allowed multiple choices for each person

## Object Model

* User
    * buying_for User
* Gift:
    * wisher
    * buyer
    * bought?
    * name

## Logic

* user can view and edit giftee list
* user can add new people to giftee list
* user can see all unbought gifts for giftees
* user can select a gift to add to shopping list
* user can see "shopping list" of gifts to buy
* user can update the "bought" status of to-buy gifts
* user can add/remove items on their wishlist; if they remove, notify
  anyone who signed up to buy the item!!! Maybe handle this with an
  exception...

## API

* api/wishlist/[create|read|destroy|id]
* api/giftees/[add|remove|read]
* api/shopping/[add|read|update|remove]
* api/users/[all]

## HTML outline

* wishlist pane - #wishlist
    * tabular list of desired gifts -- api/wishlist/read
    * "add gift" button at the bottom with modal popup -- api/wishlist/create
    * "remove gift" x on each gift with confirmation popup -- api/wishlist/destroy
* giftees pane - #giftees
    * tabular list of giftees -- api/giftees/read
    * "add giftee" button at the bottom with modal popup -- api/users/all
        * list where you select multiple (checkboxes) and hit OK -- api/giftees/add
    * "remove giftee" x on each gift -- api/giftees/remove
    * "view wishlist" button with modal popup -- api/wishlist/id
        * list where you select multiple (checkboxes) and hit OK -- api/shopping/add
* shopping list pane - #shopping
    * tabular list of gifts to buy -- api/shopping/read
    * "bought" switch on each gift -- api/shopping/update
    * "remove gift" x on each gift -- api/shopping/remove

templates: index.html

## CSS outline

* use bootstrap
* use the nice "alert boxes" in bootstrap for gift entries

## Javascript outline

Follow the API and object model with Knockout
we'll have to try to use Knockout models:

* User
* Gift

## Python outline

* Follow the API and object model with Django
* TemplateView for the main page

## Authentication

* login/register modal
* permissions checks in html templates
