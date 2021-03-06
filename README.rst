=======================================
django-guestbook 
=======================================

*This is RedsolutionCMS fork. See original version at: https://github.com/dokterbob/django-guestbook*

A simple guestbook application for Django
-----------------------------------------

What is it?
===========
Guestbook is a simple guestbook application for
the Django web-framework. It is closely based
on the contributed comments application.

Guestbook is build to work against a late 
pre-1.0 checkout and should be 1.0-compatible.

More info about this app can be found in the blog
post introducing it at:
http://cooking.visualspace.nl/post/9992059/Django-Guestbook-application

Status
======
This app is currently being used in several small-scale production environments.
However, it is probably that it still has a few kinks so feel free to submit bugfixes.

Installation
============
#)  Get it from the Cheese Shop::
    
     easy_install django-guestbook
    
    **Or** get the latest & greatest from Github and link it to your
    application tree::
    
     git clone git://github.com/dokterbob/django-guestbook.git
     ln -s django-guestbook/guestbook $PROJECT_DIR/guestbook
    
    (Here `$PROJECT_DIR` is your project root directory.)
    
#)  Add popularity to `INSTALLED_APPS` in settings.py::

     INSTALLED_APPS = (
         ...
         'guestbook',
         ...
     )

#)  Create required data structure::

     cd $PROJECT_DIR
     ./manage.py syncdb

#)  Add guestbook views to `urls.py`::

     urlpatterns += patterns('',
         ...
         (r'^guestbook/', include('guestbook.urls')),
         ...
     )

#)  Enjoy!

Avaliable settings
==================

GUESTBOOK_USE_CAPTCHA:
    If ``django-simple-captcha`` is used in your project, guestbook post
    form wiil be protected with CAPTCHA field automatically. If you want
    to turn this feature off, set::

        GUESTBOOK_USE_CAPTCHA=false

    in your project's ``settings.py`` file.


Differences in this branch
==========================

#) All templates extended from project's ``base.html``
#) Removed debug in "400" template
#) Changed models
#) Integrated with `django-simple-captcha <http://code.google.com/p/django-simple-captcha/>`_
