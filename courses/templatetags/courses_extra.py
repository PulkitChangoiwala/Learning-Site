from django import template
from courses.models import Course
from django.utils.safestring import mark_safe
import markdown2

register = template.Library()


@register.simple_tag
def newest_course():
	''' Getting the latest course on layout page  '''
	return Course.objects.latest('created_at')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
	''' To add courses list on every pags  '''
	#This is inclusion tag, returns a tag inside a tag
	courses = Course.objects.all()
	return { 'courses' : courses
	} #returns dictionary

@register.filter('time_estimate')
def time_estimate(word_count):
	minutes = round(word_count/20)
	return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
	'''convert markdown text to html'''
	html_body = markdown2.markdown(markdown_text)
	return mark_safe(html_body) 
	# mark_safe() alternative using safe filter in course_detail.html

