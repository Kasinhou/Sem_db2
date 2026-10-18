create or replace type t_person as object (
    rod_cislo char(11),
    name varchar2(20),
    surname varchar2(30),
    constructor function t_person(p_rod_cislo char)
    return self as result,
    member function get_age
    return number,
    member function get_sex
    return varchar2,
    member function get_full_name
    return varchar2,
    map member function sort_person
    return varchar2
);
/

create or replace type body t_person as
    constructor function t_person(p_rod_cislo char)
    return self as result
    is
    begin
        self.rod_cislo := p_rod_cislo;
        self.name := null;
        self.surname := null;
        return;
    end;
    
    member function get_age
    return number
    is
        dat_narodenia date;
    begin
        dat_narodenia := to_date(
            '19' || substr(self.rod_cislo, 1, 2) || '.' || 
            mod(substr(self.rod_cislo, 3, 2), 50) || '.' || 
            substr(self.rod_cislo, 5, 2),
            'YYYY.MM.DD'
        );
        
        return floor(months_between(sysdate, dat_narodenia) / 12);
    end;

    member function get_sex
    return varchar2
    is
    begin
        if to_number(substr(self.rod_cislo, 3, 2)) > 50 then
            return 'female';
        else
            return 'male';
        end if;
    end;
    
    member function get_full_name
    return varchar2
    is
    begin
        return self.name||' '||self.surname;
    end;
    
    map member function sort_person
    return varchar2
    is
    begin
        return self.surname || ' ' || self.name;
        -- ak order tak davam -1,1,0
    end;
end;
/