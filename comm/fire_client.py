from firebase import firebase
firebase = firebase.FirebaseApplication('https://recce.firebaseio.com', None)
result = firebase.get('/', None)
print str(result)

obj = { "lat": 42.14, "lng": 8.27, "path": '/to/file' }
new_lat = float(input())
#firebase.post('/vehicles',{"2": "AAA"})

f = Firebase('https://recce.firebaseio.com/vehicles')
print f.get()

