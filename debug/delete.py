from tellonym import Tellonym as Te

username = 'vapewwa'
password = 'cipkadupka12$'

client = Te.Tellonym(username, password)

for x in client.get_tells():
    client.delete_tell(x.id)
