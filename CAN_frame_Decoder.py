def can_decoder(frame):
    # try:
        can_frame_id , can_data = frame.split("#")
        # print(can_frame_id, can_data)
        can_id = int(can_frame_id, 16)   #canid converted into hexa code int
        data = bytes.fromhex(can_data)   #can data in array

        rpm_raw = int.from_bytes(data[0:2], byteorder="big")
        # print(rpm_raw)

        speed_raw = int.from_bytes(data[2:3] , byteorder="big")
        speed = speed_raw / 100.0

        #  gear value
        # gear_raw = data[4]

        print(len(data))
        print(f"CAN ID: 0x{can_id}")
        print(f"{rpm_raw} is the vehical rpm")
        print(f"{speed} is the speed of the vehica")
        # print(f"{gear_raw} is the gear")

    # except Exception as e:
    #     print("code is error",e)



can_decoder("0CFE6CEE#10FA00AA")