#  Copyright (c) 2020. Jan Ochwat.NesTeam

from run import TellonymPost as Tp

tellonym = Tp(('username', 'password'), d=True)

tellonym.run()

print('Test completed succesfully.')