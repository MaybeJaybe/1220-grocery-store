from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem, User
from grocery_app.extensions import bcrypt
# , app, db

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # Add the following fields to the form class:
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

    # Add the following fields to the form class:
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
      validators=[DataRequired()])
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo')
    store = QuerySelectField('Store',
      query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Submit')

    # pass

class SignUpForm(FlaskForm):
  username = StringField('User Name',
    validators=[DataRequired(), Length(min=3, max=80)])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('Username is taken.')


class LoginForm(FlaskForm):
  username = StringField('User Name',
    validators=[DataRequired(), Length(min=3, max=80)])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Log In')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if not user:
      raise ValidationError('Username entered does not match our records.')

  def validate_password(self, password):
    user = User.query.filter_by(username=self.username.data).first()
    if user and not bcrypt.check_password_hash(
      user.password, password.data
    ):
      raise ValidationError('Password entered does not match our records.')
