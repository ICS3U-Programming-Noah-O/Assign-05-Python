#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 23, 2022
# This program is a basic physics calculator that can calculate E=MC^2
# the acceleration of an object, and power.

import math
import time
import constants
import colorama
from colorama import Fore, Back, Style


def energy_calculation(mass):
    # This function calculates E=MC^2 and then
    # returns energy back to main
    energy = mass * constants.SPEED_OF_LIGHT ** 2
    return energy


def calculate_acceleration(starting, finishing, time_passing):
    # This function calculates acceleration
    # and then returns the result back to main
    acceleration = (finishing - starting) / time_passing
    return acceleration


def work_calculation(force_n, displacement_m):
    # This function calculates a returns work
    # to main to be used to calculate power
    work_done = force_n * displacement_m
    return work_done


def power_calculation(total_work, time):
    # This function calculates power and
    # then returns the result to main
    power = total_work / time
    return power


def main():
    # Print intro message
    print("Welcome!")
    time.sleep(1)
    print(" ")
    print("This program is a basic physics calculator that can calculate " +
          "the amount of \nenergy contained within a certain amount of" +
          " mass, the amount of energy \nused over time (Power), and " +
          "the average acceleration of an object.")
    print(" ")

    while True:
        # Allow user to pick equation
        time.sleep(1)
        print("Which equation would you like to choose?")
        print(" ")
        time.sleep(0.5)
        print("E = MC² (Calculates the amount of energy" +
              " contain in something at rest)")
        time.sleep(0.5)
        print("a = Δv/Δt (Calculates the acceleration of" +
              " something over a certain amount of time)")
        time.sleep(0.5)
        print("P = W/Δt (Calculates power which is the " +
              "amount of energy used over time)")
        time.sleep(0.5)
        print(" ")
        equation_choice = input("Enter your choice here (E/a/P): ")

        # If energy equation is picked than ask for required inputs
        if equation_choice == "E" or equation_choice == "e":
            print(" ")
            print("----------------------------------------------" +
                  "-------------------------------------")
            print("You chose E = MC², good choice!")
            print(" ")
            time.sleep(1.5)
            print("In order to calculate the energy contained within an " +
                  "object at a resting state it \nrequires " +
                  "the mass of the object in kilograms.")
            print(" ")
            time.sleep(1.5)

            while True:
                # Ask user for mass
                object_mass = input("Enter the mass of your object in kg: ")
                # Make sure that mass input is valid
                try:
                    object_mass_float = float(object_mass)

                    if object_mass_float > 0:
                        print(" ")
                        # Call function to calculate energy
                        final_energy = energy_calculation(object_mass_float)
                        # Print final result
                        print("An object at rest with a mass of " +
                              "{} kg has ".format(object_mass_float) +
                              "{} J of energy contained within it.".format(
                                  final_energy))
                        print(" ")
                        time.sleep(1.5)
                        print("---------------------------------------" +
                              "--------------------------------------------")
                        break
                    else:
                        print("{} is an invalid input".format(object_mass) +
                              ". Your input must be a positive number.")
                # If input is invalid ask again
                except Exception:
                    print("{} is not a valid".format(object_mass) +
                          " input. Your input must be a number.")
                    print(" ")
            print(" ")
            # Ask user if they'd like to calculate again
            calculate_again_answer = input(
                "Would you like to calculate again? y/n: ")
            print(" ")

            if calculate_again_answer == "n" or calculate_again_answer == "N"\
                    or calculate_again_answer == "no":
                break
        # If acceleration equation is picked than ask for required inputs
        elif equation_choice == "a" or equation_choice == "A":
            print(" ")
            print("-----------------------------------------" +
                  "------------------------------------------")
            print("You chose a = Δv/Δt, good choice!")
            print(" ")
            time.sleep(1.5)
            print("In order to calculate acceleration over time it requires " +
                  "the starting velocity, the \nfinishing velocity, " +
                  "and the amount of elapsed time.")
            print(" ")
            time.sleep(1.5)

            while True:
                # Get velocity and time input from the user
                # Make sure that all of the inputs are valid
                starting_velocity = input(
                    "Enter the starting velocity of your object (m/s): ")
                time.sleep(1.5)
                print(" ")
                try:
                    starting_velocity_float = float(starting_velocity)

                    while True:
                        final_velocity = input(
                            "Enter the final velocity of your object (m/s): ")
                        time.sleep(1.5)
                        print(" ")
                        try:
                            final_velocity_float = float(final_velocity)

                            while True:
                                time_passed = input(
                                    "Enter the amount of time passed (s): ")
                                try:
                                    time_passed_float = float(time_passed)
                                    if time_passed_float > 0:
                                        # Call function to
                                        # calculate acceleration
                                        final_acceleration = \
                                            calculate_acceleration(
                                                starting_velocity_float,
                                                final_velocity_float,
                                                time_passed_float)
                                        print(" ")
                                        # Print final result
                                        print("An object that has changed " +
                                              "velocity from {}".format(
                                                  starting_velocity_float) +
                                              " m/s to {}".format(
                                                  final_velocity_float) +
                                              " m/s in {}".format(
                                                  time_passed_float) +
                                              " seconds \nhas an " +
                                              "acceleration rate " +
                                              "of {} m/s²".format(
                                                  final_acceleration))
                                        break
                                    else:
                                        print("{} is not".format(
                                            time_passed_float) +
                                              " a valid time. Time cannot " +
                                              "be negative or 0!")
                                # If input is invalid ask to user again
                                except Exception:
                                    print("{} is not a".format(time_passed) +
                                          " valid input. Your " +
                                          "input must be a number.")
                                    print(" ")
                                print(" ")
                            break
                        # If input is invalid ask to user again
                        except Exception:
                            print("{} is not".format(final_velocity) +
                                  " a valid input. " +
                                  "Your input must be a number.")
                            print(" ")

                    print(" ")
                    print(" ")
                    time.sleep(1.5)
                    print("----------------------------------------------" +
                          "--------------------------------------")

                    break
                # If input is invalid ask to user again
                except Exception:
                    print("{} is not ".format(starting_velocity) +
                          "a valid input. Your input must be a number.")
                    print(" ")
            print(" ")
            # Ask the user if they'd like to calculate again
            calculate_again_answer = input(
                "Would you like to calculate again? y/n: ")
            print(" ")

            if calculate_again_answer == "n" or calculate_again_answer == "N"\
                    or calculate_again_answer == "no":
                break
        # If power equation is picked than ask for required inputs
        elif equation_choice == "P" or equation_choice == "p":
            print(" ")
            print("----------------------------------------------" +
                  "-------------------------------------")
            print("You chose P = W/Δt, good choice!")
            print(" ")
            time.sleep(1.5)
            print("In order to calculate power it requires the amount" +
                  " of work in joules, \n over the elapsed time in seconds.")
            print(" ")
            time.sleep(1.5)
            # Ask the user if they want to calculate work
            work_question = input(
                "Would you like to calculate work first? y/n: ")
            time.sleep(1.5)
            print(" ")
            # If yes then call function to calculate work
            # and get work inputs from user
            if work_question == "n" or work_question == "N" \
                    or work_question == "no":
                while True:
                    user_work = input
                    ("Enter the amount of work done in joules: ")
                    print(" ")
                    # Make sure that work inputs are valid
                    try:
                        user_work_float = float(user_work)
                        while True:
                            time_passed = input(
                                "Enter the amount of " +
                                "time elapsed is seconds: ")
                            print(" ")
                            # Make sure that work inputs are valid
                            try:
                                time_passed_float = float(time_passed)
                                if time_passed_float > 0:

                                    total_power = power_calculation(
                                        user_work_float, time_passed_float)
                                    time.sleep(1.5)
                                    print("The total power, or energy spent" +
                                          ", in {} seconds is {} W.".format(
                                              time_passed_float, total_power))
                                    time.sleep(1.5)
                                    print(" ")
                                    break
                                else:
                                    print("{} is invalid".format(
                                        time_passed_float) +
                                          ". Time cannot be negative or 0!")
                            # If the input is invalid ask the question again
                            except Exception:
                                print("{} is not a valid ".format(
                                    time_passed) +
                                      "input. Your input must be a number.")
                                print(" ")
                        break
                    # If the input is invalid ask the question again
                    except Exception:
                        print("{} is not a valid".format(user_work) +
                              " input. Your input must be a number.")
                        print(" ")
            else:
                while True:
                    # Continue the power calculation
                    print("In order to calculate work you need the amount " +
                          "of force in newtons and displacement in meters.")
                    print(" ")
                    # Get the user inputs for force and displacement
                    time.sleep(1.5)
                    user_force = input(
                        "Enter the amount of force in newtons: ")
                    print(" ")
                    # Make sure that the inputs are valid
                    try:
                        user_force_float = float(user_force)

                        while True:
                            user_displacement = input(
                                "Enter the displacement in meters: ")
                            print(" ")

                            try:
                                user_displacement_float = float(
                                    user_displacement)
                                # Call the function to calculate work
                                user_work_float = work_calculation(
                                    user_force_float,
                                    user_displacement_float)
                                break
                            # If the input is invalid ask the user again
                            except Exception:
                                print("{} is not a".format(user_displacement) +
                                      " valid input. Your " +
                                      "input must be a number.")
                                print(" ")
                        break
                    # If the input is invalid ask the user again
                    except Exception:
                        print("{} is not a valid input".format(user_force) +
                              ". Your input must be a number.")
                        print(" ")

                while True:
                    # Ask the user for the time that has passed
                    time_passed = input("Enter the amount of time " +
                                        "elapsed is seconds: ")
                    # Make sure that the input is valid
                    try:
                        time_passed_float = float(time_passed)
                        if time_passed_float > 0:
                            # Call the function the calculate power
                            total_power = power_calculation(user_work_float,
                                                            time_passed_float)
                            print(" ")
                            time.sleep(1.5)
                            # Print the final result
                            print("The total power, or energy spent, in" +
                                  "{} seconds is ".format(time_passed_float) +
                                  "{} W.".format(total_power))
                            print(" ")
                            time.sleep(1.5)
                            break
                        else:
                            print("{} is invalid".format(time_passed_float) +
                                  ". Time cannot be negative or 0!")
                    # If the user input is invalid ask the question again
                    except Exception:
                        print("{} is not a valid ".format(time_passed) +
                              "input. Your input must be a number.")
                        print(" ")
            # Ask the user if they'd like to calculate again
            calculate_again_answer = input("Would you like to calculate " +
                                           "again? y/n: ")
            print(" ")

            if calculate_again_answer == "n" or calculate_again_answer == \
               "N" or calculate_again_answer == "no":
                break

        else:
            # If the user input is invalid ask the question again
            print(" ")
            time.sleep(0.5)
            print("{} is not a valid input".format(equation_choice))
            time.sleep(0.5)
            print("Your input must be either E, a, or P")
            print("------------------------------------------" +
                  "-----------------------------------------")
            print(" ")
            time.sleep(1)


if __name__ == "__main__":
    main()
