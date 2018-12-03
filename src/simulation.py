import random
import sys
from models import Controller, State, FuzzyLogicController
from road import Vehicle, Lane

if __name__ == '__main__':
    # create a controller
    control = Controller()
    #control = FuzzyLogicController()
    # create North-to-South and West-to-East lanes
    north2south = Lane(control,S=15, D=7, name='North to South', init_state=State.green)
    west2east = Lane(control, S=15, D=7, name='West to East', init_state=State.red)

    lanes = {
        north2south.id: north2south,
        west2east.id: west2east
    }

    print("Intersection created")

    step = 0
    while (north2south.car_out < 50) and (west2east.car_out < 50):
        if step > 400:
            sys.exit(0)
        print('[STEP {}]'.format(step))
        # coin toss to generate a new car or not
        if random.uniform(0, 1) >= 0.5: # 
            print('new vehicle in lane {}'.format(north2south.name))
            north2south.append(Vehicle())
        if random.uniform(0,1) >= 0.8: #fewer cars on lane west2east
            print('new vehicle in lane {}'.format(west2east.name))
            west2east.append(Vehicle())

        control.step()
        north2south.step()
        west2east.step()

        print("N2S")
        #print(north2south) #comment to avoid printing the lane
        print("W2E")
        #print(west2east) #comment to avoid printing the lane
        
        step+=1
        print('\n')
    
    print("N2S total wait: {}".format(north2south.total_wait))
    print("W2S total wait: {}".format(west2east.total_wait))

    



