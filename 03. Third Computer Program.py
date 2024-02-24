def main():
    print("Cost Estimate for Masonry Works")
    print("By: German Francis Intano\n") #Program author hard encoded for transparency

    #Getting user-input
    canopy_volume = float(input("Enter canopy volume (cu. m): "))
    wall_area = float(input("Enter wall area (sq. m): "))
    window_door_sill_length = float(input("Enter Total Length of Window & Door Sill (m): "))
    floor_area = float(input("Enter floor area (sq. m): "))

    #Declaring unit cost
    COST_PER_CUBIC_METER_CANOPY = 5500 #in PHP per cu. m
    COST_PER_SQUARE_METER_WALL = 187.50 #in PHP per sq. m
    COST_PER_METER_WINDOW_DOOR_SILL = 278.25 #in PHP per meter
    COST_PER_CUBIC_METER_FLOOR_TOPPING = 5500 #in PHP per cu. m

    #Calculating cost
    canopy_cost = round(float(canopy_volume*COST_PER_CUBIC_METER_CANOPY),2)
    masonry_retouch_area = float(wall_area*0.25)
    masonry_retouch_cost = round(float(masonry_retouch_area*COST_PER_SQUARE_METER_WALL),2)
    window_door_sill_cost = round(float(window_door_sill_length*COST_PER_METER_WINDOW_DOOR_SILL),2)
    floor_topping_volume = round(float(2*2.54*0.01*floor_area),2)
    floor_topping_cost = round(float(floor_topping_volume*COST_PER_CUBIC_METER_FLOOR_TOPPING),2)
    total_cost = round(float(canopy_cost+masonry_retouch_cost+window_door_sill_cost+floor_topping_cost),2)

    #Output
    print("-"*75)
    print("The following are the cost estimates:")
    print("Canopy: {} CU.M, PHP {:.2f}".format(canopy_volume,canopy_cost))
    print("Masonry Retouch: {} SQ.M, PHP {:.2f}".format(masonry_retouch_area,masonry_retouch_cost))
    print("Window and Door Sill: {} M, PHP {:.2f}".format(window_door_sill_length,window_door_sill_cost))
    print("Floor Topping: {} CU.M, PHP {:.2f}".format(floor_topping_volume,floor_topping_cost))

    print("\nThe total cost estimate for Masonry Works is: PHP {:.2f}".format(total_cost))

if __name__ == "__main__":
    main()