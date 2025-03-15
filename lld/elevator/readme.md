+-----------------------------------+
|            <<enum>>               |
|           Direction               |
+-----------------------------------+
| UP                                |
| DOWN                              |
| IDLE                              |
+-----------------------------------+

+-----------------------------------+
|            <<enum>>               |
|         ElevatorState             |
+-----------------------------------+
| MOVING                            |
| IDLE                              |
| STOPPED                           |
+-----------------------------------+

+-----------------------------------+
|             Request               |
+-----------------------------------+
| - source_floor: int               |
| - destination_floor: int          |
| - direction: Direction            |
+-----------------------------------+
| + __init__(source_floor,          |
|            destination_floor=None)|
| + __lt__(other): bool             |
+-----------------------------------+

+-----------------------------------+
|             Elevator              |
+-----------------------------------+
| - id: int                         |
| - current_floor: int              |
| - direction: Direction            |
| - state: ElevatorState            |
| - destination_floors: list        |
| - lock: threading.Lock            |
| - display: Display                |
+-----------------------------------+
| + add_destination(floor: int)     |
| + move()                          |
+-----------------------------------+

+-----------------------------------+
|             Display               |
+-----------------------------------+
| - elevator: Elevator              |
+-----------------------------------+
| + update(current_floor: int,      |
|          direction: Direction)    |
+-----------------------------------+

+-----------------------------------+
|           <<interface>>           |
|            Scheduler              |
+-----------------------------------+
| + schedule(request: Request,      |
|            elevators: list)       |
+-----------------------------------+

+-----------------------------------+
|      NearestElevatorScheduler     |
+-----------------------------------+
| + schedule(request: Request,      |
|            elevators: list)       |
+-----------------------------------+

+-----------------------------------+
|     ElevatorControlSystem         |
+-----------------------------------+
| - elevators: list                 |
| - scheduler: Scheduler            |
| - request_queue: list             |
| - lock: threading.Lock            |
+-----------------------------------+
| + start_elevators()               |
| + add_request(request: Request)   |
| + process_requests()              |
+-----------------------------------+

+-----------------------------------+
|             Button                |
+-----------------------------------+
| - control_system: ElevatorControl |
| - floor: int                      |
+-----------------------------------+
| + press(destination_floor: int)   |
+-----------------------------------+





### Relationships

##### Inheritance (Is-a):

- NearestElevatorScheduler is-a Scheduler.

##### Composition (Has-a):

- ElevatorControlSystem has-a Scheduler.
- ElevatorControlSystem has-a list of Elevator.
- Elevator has-a Display.
- Button has-a ElevatorControlSystem.

##### Association:

- Elevator uses Request to manage destination floors.
- Scheduler uses Request and Elevator to assign elevators to requests.

#### Dependency:
- ElevatorControlSystem depends on Scheduler for scheduling logic.
- Button depends on ElevatorControlSystem to add requests.

`bash 
    User -> Button: press(destination_floor)
    Button -> ElevatorControlSystem: add_request(request)
    ElevatorControlSystem -> Scheduler: schedule(request, elevators)
    Scheduler -> Elevator: add_destination(floor)
    Elevator -> Display: update(current_floor, direction)
    Elevator -> Elevator: move()
`