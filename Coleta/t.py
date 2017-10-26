#!/usr/bin/env python
# -*- coding: cp1252 -*-
import threading as t
 
class MyThread(t.Thread):
    def run(self):
        print "init thread " + self.getName() 
 
mt = MyThread()
mt.start()
 
print 'fim'