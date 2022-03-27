from operator import attrgetter


class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self) :
        return 'User({})'.format(self.user_id)

users = [User(19),User(17),User(18)]
print(users)

print(sorted(users,key=lambda u: u.user_id))

from operator import attrgetter
print(sorted(users,key=attrgetter('user_id')))
