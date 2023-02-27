from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button

    title = StringField('Title',
      validators=[
        DataRequired(),
        Length(min=3, max=80, message="Title must be between 3 and 80 characters.")
      ])
    address = StringField('Address',
      validators=[
        DataRequired(),
        Length(min=3, max=80, message="Address must be between 3 and 80 characters.")
      ])
    submit = SubmitField('Submit')

    # pass

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button

    name = StringField('Name',
      validators=[
        DataRequired(),
        Length(min=3, max=80, message="Name must be between 3 and 80 characters.")
      ])
    price = FloatField('Price',
      validators=[
        DataRequired()
      ])
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo')
    store = QuerySelectField('Store',
      query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Submit')

    # pass
