package com.amybnguyen;

public class SaveData {
    public double money;
    public double moneyPerSecond;
    public Upgrades upgrades = new Upgrades();
}

class Upgrades {
    public Finger finger = new Finger();
    public EspressoMachine espressoMachine = new EspressoMachine();
    public Nintendo nintendo = new Nintendo();
    public MountainDew mountainDew = new MountainDew();
    public Desperation desperation = new Desperation();
    public Singer singer = new Singer();
}

class Finger {
    public int own;
    public double cost;
    public double increaseMPSBy;
}

class EspressoMachine {
    public int own;
    public double cost;
    public double increaseMPSBy;
}

class Nintendo {
    public int own;
    public double cost;
    public double increaseMPSBy;
}

class MountainDew {
    public int own;
    public double cost;
    public double increaseMPSBy;
}

class Desperation {
    public int own;
    public double cost;
    public double increaseMPSBy;
}

class Singer {
    public int own;
    public double cost;
    public double increaseMPSBy;
}




