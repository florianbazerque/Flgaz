# Flgaz

http://florianb.eu.pythonanywhere.com/

## App showcase

This app allows unregister people to write a message under 280 characters under the username of their choice.
If someone puts more than 280 characters or put an empty message we will not register this message.
You can see all of the messages of a specific username by clicking on his username.

## App content

### Python 3.x with Flask

### CSV to register the message

### Message restriction

To restrict the number of characters that we get by the user we used a simple if condition

```
if len(row[0]) < 20 and len(row[1]) < 280 and len(row[0]) > 0 and len(row[1]) > 0:
```

### Cache control

### Google font

In the CSS we used the google url to import the font "Google Sans"

```
@import url('https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap');
```