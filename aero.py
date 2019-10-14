
main ()
    exec = exec();
    while(exec)
        light = getLight();
        temp = getTemp();
        if(output(light,temp))
           print("Worked");
       else
           print("weird bug")
           waterInSeconds = getWaterInSeconds(light,temp);
       water(waterInSeconds);
        sleep(getSecondsInHour - waterInSeconds);
        exec = exec();


water(waterInSeconds2) {
    ##DO sum bullshit with that variable
    ## remember waterInSeconds != waterInSeconds2
