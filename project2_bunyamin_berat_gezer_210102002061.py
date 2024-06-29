my_name = "Bunyamin Berat Gezer"
my_id = "210102002061"
my_email = "b.gezer2021@gtu.edu.tr"



import random


class Transceiver:

    value_of_id= 0

    def __init__(self,x,y,tpower,rpower=0.001):
        self.x=x
        self.y=y
        self.id=Transceiver.value_of_id
        Transceiver.value_of_id+=1
        self.tpower=tpower
        self.rpower=rpower
        self.localtime=0

    def get_coordinate_x(self):
        return self.x

    def get_coordinate_y(self):
        return self.y

    def get_coordinates(self):
        x=self.x
        y=self.y
        return (x,y)

    def get_tpower(self):
        return self.tpower

    def get_rpower(self):
        return self.rpower

    def get_id(self): 
        return self.id

    def get_localtime(self):
        return self.localtime

    def set_coordinates(self,x,y):
        self.x=x
        self.y=y

    def set_transmitting_power(self,tpower):
        self.tpower=tpower

    def set_receiving_power(self,rpower):
        self.rpower=rpower

    def update_local_time(self,localtime):
        self.localtime=localtime

    def distance(self,m):
        coordinate_x=(self.x-m.x)**2
        coordinate_y=(self.y-m.y)**2
        cordinate=((coordinate_x)+(coordinate_y))**(0.5)
        return cordinate

    def transmitted_power(self,coordinate):
        x,y=coordinate
        x1=(self.x-x)**2
        y1=(self.y-y)**2
        x_y_d=(x1+y1)**(0.5)
        if x_y_d<1:            
            return int(self.tpower)
        else:    
            return self.tpower/x_y_d

            
    def __eq__(self,other):
                
        a1=self<other
        a2=self>other
        if a1==True and a2==True:
            return True
        else:
            return False

        

    def __lt__(self,other):
        if self.transmitted_power(other.get_coordinates())>=other.rpower :
            return True
        else:
            return False
        

    def __gt__(self,other):
        if other.transmitted_power(self.get_coordinates())>=self.rpower:

           return True
        else:

            return False



            

        

    def __str__(self):
        name_of_class = "Class: Tower"
        number_of_tower = "   Tower Number: {}".format(self.get_id())
        cordinatee = "   Coordinates: <{},{}>".format(self.x, self.y)
        power_of_t = self.tpower
        power_of_r = self.rpower
        unit_of_t = "W"
        unit_of_r = "W"
        if power_of_t >= 1000:
            power_of_t = power_of_t / 1000
            unit_of_t = "kW"
        elif power_of_t < 1:
            power_of_t = power_of_t * 1000
            unit_of_t = "mW"
        if power_of_r >= 1000:
            power_of_r = power_of_r / 1000
            unit_of_r = "kW"
        elif power_of_r < 1:
            power_of_r = power_of_r * 1000
            unit_of_r = "mW"
        power_of_transmitting = "   Transmitting Power: {} {}".format(power_of_t, unit_of_t)
        min_reciving = "   Min. Receiving Power: {} {}".format(power_of_r, unit_of_r)
        return "{}\n{}\n{}\n{}\n{}".format(name_of_class, number_of_tower, cordinatee, power_of_transmitting, min_reciving)


class Robot(Transceiver):
    id_of_robot=0

    def __init__(self,x,y,vx,vy):
        Transceiver.__init__(self,x,y,1,0.01)
        self.id=Robot.id_of_robot
        Robot.id_of_robot+=1
        self.vx=vx
        self.vy=vy
        self.status=True
        self.disconnet_time=0

    def get_velocity(self):
        return (self.vx,self.vy)

    def get_status(self):
        return self.status

    def get_disconnet_time(self):
        return self.disconnet_time

    def set_velocity(self,vx,vy):
        self.vx=vx
        self.vy=vy

    def set_status(self,newstatus):
        self.status=newstatus

    def update_disconnet(self):
        self.disconnet_time+=1

    def set_disconnet_time(self):
        self.disconnet_time=0
    
    def update_location(self):
        self.y+=self.vy
        self.localtime+=1
        self.x+=self.vx
    def __str__(self):
        indicator = """
        Class: Robot
        Robot Number: {}
        Current Coordinates: <{},{}>
        Current Velocity: <{},{}>
        Transmitting Power: {} {}
        Min. Receiving Power: {} {}
        Status: {}
        """        
        t_of_unit = "W"
        r_of_unit = "W"
        t_of_power = self.tpower
        r_of_power = self.rpower
        if self.tpower >= 1000:
            t_of_power = t_of_power / 1000
            t_of_unit = "kW"
        elif self.tpower < 1:
            t_of_power = t_of_power * 1000
            t_of_unit = "mW"
        if self.rpower >= 1000:
            r_of_power = r_of_power / 1000
            r_of_unit = "kW"
        elif self.rpower < 1:
            r_of_power = r_of_power * 1000
            r_of_unit = "mW"
        
        if self.status == False:
            status = "Dead"
        else:
            status="Alive"
        return indicator.format(self.get_id(), self.x, self.y, self.vx, self.vy, t_of_power, t_of_unit, r_of_power, r_of_unit, status)      

class Guard(Robot):
    def __init__(self,x,y,vx,vy,period=60,localtime=0):
        Robot.__init__(self,x,y,vx,vy)
        self.period=period
        self.localtime=localtime

    def get_period(self):
        return self.period

    def set_period(self,period):
        self.period = period

    def update_location(self):
        self.localtime+=1
        if self.localtime%self.period==0:
            self.vx,self.vy=self.vy,-self.vx
        else:
            self.x+=self.vx
            self.y+=self.vy
    
    def __str__(self):
        
        t_power = self.tpower
        r_power = self.rpower
        t_unit = "W"
        r_unit = "W"
        if self.tpower >= 1000:
            t_power = t_power / 1000
            t_unit = "kW"
        elif self.tpower < 1:
            t_power = t_power * 1000
            t_unit = "mW"
        if self.rpower >= 1000:
            r_power = r_power / 1000
            r_unit = "kW"
        elif self.rpower < 1:
            r_power = r_power * 1000
            r_unit = "mW"

            output = """
        Class: Guard
        Robot Number: {}
        Current Coordinates: <{},{}>
        Current Velocity: <{},{}>
        Transmitting Power: {} {}
        Min. Receiving Power: {} {}
        Status: {}
            """.format(self.get_id(), self.x, self.y, self.vx, self.vy, t_power, t_unit, r_power, r_unit, 'Alive' if self.status else 'Dead')
        return output

class Psycho(Robot):
    def __init__(self,x,y):
        vx=random.uniform(-10, 10)
        vy=random.uniform(-10, 10)
        Robot.__init__(self,x,y,vx,vy)
        self.period=random.randint(1, 100) 
        self.localtimep=0
    def update_location(self):
        self.localtime+=1
        self.localtimep+=1
        if self.localtimep%self.period==0:
            self.vx=random.uniform(-10, 10)
            self.vy=random.uniform(-10, 10)
            self.period=random.randint(1, 100)
            self.localtimep=0 
        self.x+=self.vx
        self.y+=self.vy
    def __str__(self):
        t_power = self.tpower
        r_power = self.rpower
        t_unit = "W"
        r_unit = "W"
        if self.tpower >= 1000:
            t_power = t_power / 1000
            t_unit = "kW"
        elif self.tpower < 1:
            t_power = t_power * 1000
            t_unit = "mW"
        if self.rpower >= 1000:
            r_power = r_power / 1000
            r_unit = "kW"
        elif self.rpower < 1:
            r_power = r_power * 1000
            r_unit = "mW"

        output = """
    Class: Psycho
    Robot Number: {}
    Current Coordinates: <{},{}>
    Current Velocity: <{},{}>
    Transmitting Power: {} {}
    Min. Receiving Power: {} {}
    Status: {}
        """.format(self.get_id(), self.x, self.y, self.vx, self.vy, t_power, t_unit, r_power, r_unit, 'Alive' if self.status else 'Dead')
        return output

class Battle_Field:
    def __init__(self):
        self.global_time = 0
        self.transceivers = []
        self.robots = []
        self.deadrobots = []

    def add_transceiver(self, x, y, tpower, rpower=0.001):
        transceiver = Transceiver(x, y, tpower, rpower)
        self.transceivers.append(transceiver)

    def add_robot(self, x, y, vx, vy):
        robot = Robot(x, y, vx, vy)
        self.robots.append(robot)

    def add_guard(self, x, y, vx, vy, timer=0, period=60):
        guard = Guard(x, y, vx, vy, period, localtime=timer)
        self.robots.append(guard)

    def add_psycho(self, x, y):
        class_of_psycho= Psycho(x, y)
        self.robots.append(class_of_psycho)

    def get_transceivers(self):
        return self.transceivers

    def get_robots(self):
        return self.robots

    
    def kill_robot(self, robot):
        if robot in self.robots:
            self.robots.remove(robot)
            robot.status = False
            self.deadrobots.append(robot)

        
    def get_deadrobots(self):
        for ğoğ in self.deadrobots:
            yield ğoğ
    
    def remove_robot(self, robotid):
        
        for s1 , robot in enumerate(self.robots):
            if robot.id == robotid:
                del self.robots[s1]
                break

    def remove_transceiver(self, trid):
        starting = 0
        while starting < len(self.transceivers):
            if self.transceivers[starting].id == trid:
                self.transceivers.pop(starting)
                break
            starting += 1

            
    def progress_time(self):
        pass
                
    def __str__(self):

        str1 = "Number of transceivers: {}".format(len(self.transceivers))
        str2 = "Number of robot (alive): {}".format(len(self.robots))
        str3 = "Number of dead robots: {}".format(len(self.deadrobots))
        return "{}\n{}\n{}".format(str1, str2, str3)


    def create_report(self):

        report = "Time: {} s\n{}\n".format(self.global_time, self)
        for i in self.transceivers:
            report += "{}\n".format(i)
        for i in self.robots:
            report += "{}\n".format(i)
        for i in self.deadrobots:
            report += "{}\n".format(i)
        return report

