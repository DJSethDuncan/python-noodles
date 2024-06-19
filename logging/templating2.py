from string import Template

class User:
  name=""
  email=""

  def __init__(self, name, email):
    self.name = name
    self.email = email

  def __str__(self):
    return self.name

if __name__ == '__main__':

  seth = User("Seth", "email@email.com")

  userTemplate = Template("My name is $name and my email is $email")
  userTemplate2 = Template("My favorite person is $name")

  print(userTemplate.substitute(name=seth.name, email=seth.email))
  print(userTemplate2.substitute(name=seth.name))