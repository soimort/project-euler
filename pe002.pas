program pe002;
var
    a, b, i, sum, temp: longint;
begin
    a := 1;
    b := 2;
    i := 2;
    sum := 0;
    while b <= 4000000 do
        begin
            if b mod 2 = 0 then
                sum := sum + b;
            temp := b;
            b := a + b;
            a := temp;
            i := i + 1;
        end;
    writeln(sum)
end.
