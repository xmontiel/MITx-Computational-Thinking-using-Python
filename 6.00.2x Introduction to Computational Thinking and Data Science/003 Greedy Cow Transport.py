# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:20:49 2026

@author: Xuan
"""
# Enter your code for the Greedy Cow Transport here 

def greedy_cow_transport(cows, limit=10):
    remaining_cows = cows.copy()
    trips = []

    while remaining_cows:
        trip = []
        available_space = limit

        fitting_cows = [
            (name, weight)
            for name, weight in remaining_cows.items()
            if weight <= available_space
        ]

        while fitting_cows:
            cow, weight = max(fitting_cows, key=lambda x: x[1])

            trip.append(cow)
            available_space -= weight
            del remaining_cows[cow]

            fitting_cows = [
                (name, weight)
                for name, weight in remaining_cows.items()
                if weight <= available_space
            ]

        trips.append(trip)

    return trips