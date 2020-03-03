# -*- coding: utf-8 -*-
"""
@author: 唐帆
@time: 2020/02/16 20:52
柜台排队示例，多柜台情况

"""
from random import random
from 数据结构和算法.浙大课程.linkQueue import LinkQueuePublic


class Simulator(object):
    def __init__(self, no_of_sever, arrival_low, arrival_high, service_time_low, service_time_high, custom_num):
        self.no_of_sever = no_of_sever
        self.arrival_low = arrival_low
        self.arrival_high = arrival_high
        self.service_time_low = service_time_low
        self.service_time_high = service_time_high
        self.custom_num = custom_num
        self.event = {
            "time": 0,
            "type": 0,
        }

    def average_wait_time(self):
        server_busy = 0
        total_wait_time = 0
        wait_queue = LinkQueuePublic()
        event_queue = LinkQueuePublic()
        for i in range(0, self.custom_num):
            a = random()
            event = {
                "time": 0,
                "type": 0,
            }
            event["time"] += self.arrival_low + (self.arrival_high - self.arrival_low + 1) * a
            event_queue.enqueue(event)
        while event_queue.is_empty() is False:
            current_event = event_queue.dequeue()
            current_time = current_event["time"]
            current_type = current_event["type"]
            if current_type == 0:
                if server_busy != self.no_of_sever:
                    server_busy += 1
                    current_event["time"] += self.service_time_low + (self.service_time_high - self.service_time_low + 1) * random()
                    current_event["type"] = 1
                    event_queue.enqueue(current_event)
                else:
                    wait_queue.enqueue(current_event)
            elif current_type == 1:
                if wait_queue.is_empty() is False:
                    current_event = wait_queue.dequeue()
                    total_wait_time += current_time - current_event["time"]
                    current_event["time"] = current_time + self.service_time_low + (self.service_time_high - self.service_time_low + 1) * random()
                    current_event["type"] = 1
                    event_queue.enqueue(current_event)
                else:
                    server_busy -= 1
        return total_wait_time/self.custom_num


if __name__ == "__main__":
    print(Simulator(3, 5, 10, 5, 20, 20).average_wait_time())
