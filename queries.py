# To test things out you can use `python manage.py shell`

# importing relevant module
from django.shortcuts import get_object_or_404
from projects.models import Project, Review, Tag
# or
# from .models import Project, Review, Tag


# Don't forget the structure
# querySet = <ModelName>.objects.all()
#   .filter()  .get()   .exclude()
#   .last()     .first()
#   item.delete() or .save()

# this shows all rows
Project.objects.all()

# this one shows those with title exactly as
Project.objects.get(title='Portfolio Project')

# storing the returned object into a variable has its own advantages
projectObj = Project.objects.get(title='Portfolio Project')
print(projectObj.created) # accessing attributes of that object

# One line create and save
Tag.objects.create(name="angular")

# Create and Save
user = User.objects.first()
Project = Project(user=user, title='Item 1', price=19.95)
# Save
Project.save()

# Update a particular object
item = Project.objects.get(title='Bumble Bee')
item.title = 'Bumble Lee'
item.save()

# Delete the most recently created object
item = Project.objects.last()
item.delete()

# Select Related (to avoid n+1 query)
posts = Review.objects.select_related('user', 'category').all()

# Read or render a 404 not found page
project = get_object_or_404(Project, id=512)

# Filter
Project.objects.filter(vote_ratio__gt=2016)  # __gt = greater than
Project.objects.filter(vote_ratio__lt=2001)  # __lt = less than
Project.objects.filter(vote_ratio__gt=80, title__endswith='e')
Project.objects.filter(vote_ratio__gt=80, title__endswith='e')  # the inverse of the above
Project.objects.filter(title__icontains='mB')  # __icontains


# Filter on relationship sub model field
Project.objects.get(user__usertitle='mike')

# Ordering
Project.objects.order_by('title')     # ascending
Project.objects.order_by('-title')   # descending

# Slicing return first
Project.objects.all().order_by('title')[0]

# Slicing return last
Project.objects.all().order_by('-title')[0]

# Slicing limit/offset
Project.objects.all().order_by('title')[1..10]

# Updating
project = Project.objects.first()
project.title = 'new title'
project.save()

# One line update
Project.objects.filter(id=4).update(title='new title')

# Deleting
project = Project.objects.first()
project.delete()

# One line delete
Project.objects.get(id=1).delete()

# Delete all
Project.objects.all().delete()

# Query Models Children
item = Project.objects.first()
# item.<childmodel>_set.all() the childmodel has to be lowercase
item.review_set.all()

# Set ForeignKey field value
model1 = Model(title='dyson')
Project.model = model1

# Get ForeignKey value
Project1.model.title
model1.Project_set.all()

# Add Many-to-Many
Project1.tags.add(tag1)
Project1.tags.all()
tag1.Projects_set.all()


# Query ManyToMany Fields
item = Project.objects.first()
item.relationship.all()