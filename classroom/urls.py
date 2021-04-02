from django.urls import path
from classroom import views


urlpatterns = [
	path('', views.index, name='home'),
	path('course_list/',views.courseListView,name='course_list'),
	path('course/<slug>',views.courseDetailView ,name='course_detail'),


	#ToDO Course Creation
	path('course/add_videos/<course_slug>',views.addVideosToCourse ,name='add_videos_to_course'),
	path('course/add_notes/<course_slug>',views.addNotesToCourse ,name='add_notes_to_course'),
	path('create_course/',views.createCourse,name='create_course'),

	path('vid/',views.videoTesting),

	#Static Pages
	path('contact_us/',views.contactUs,name="contact_us"),
	path('about_us/',views.aboutUs,name="about_us"),

	path('internships/',views.internships,name='internships'),
	path('internships/<id>',views.internshipDetail,name='internships-detail'),

	#checkout page
	path('checkout/<course_slug>',views.checkoutPage,name="checkout")


]

# TODO
"""
1. search
~3. phone number field in contact form add javascript checker frontend 
4. Active Button On Navbar
5. User Registration with custom form main/index.html
11. courses list page
6. Checkout (sam)
7. Content
8. Payment
9. Course videos (sam)
10. internship form (sam)
11. Blog Frontend --- requires frontend developer 
12. Profile Page  --- requires frontend developer

"""

# python manage.py loaddata db.json

# python manage.py dumpdata > db.json

