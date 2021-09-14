function diff_x = digitalToFrameNumber(old_x)
    x = [0; old_x];
    diff_x = diff(x);
    diff_x(diff_x<=0) = 0;

    old_num = 0;
    for iReading = 1:length(diff_x)
        if diff_x(iReading) == 1
            num = old_num + 1;
            diff_x(iReading) = num;
            old_num = num;
        else
            diff_x(iReading) = old_num;
        end
    end
end
