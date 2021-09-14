function x_final = analogToDigital(x_old, threshold)
    x_final = x_old;
    aboveThreshold = x_final>=threshold;
    belowThreshold = x_final<threshold;
    x_final(aboveThreshold) = 1;
    x_final(belowThreshold) = 0;
end
