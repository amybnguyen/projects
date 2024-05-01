package com.amybnguyen;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper; // ObjectMapper
import java.io.File; // Ability to read json file
import java.io.FileWriter;
import java.io.IOException;
import java.text.NumberFormat; // NumberFormat

public class DataJsonReader {
    public static void main(String[] args) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();
        String path = "src/main/resources/savedata.json";
        File saveDataJasonFile = new File(path);
        SaveData saveData = objectMapper.readValue(saveDataJasonFile, SaveData.class);

        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String formattedMoney = currency.format(saveData.money);
        System.out.println("Money: " + formattedMoney);
    }

    public SaveData getData() throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();
        String path = "src/main/resources/savedata.json";
        File saveDataJasonFile = new File(path);
        SaveData saveData = objectMapper.readValue(saveDataJasonFile, SaveData.class);

        return saveData;
    }

    public String printData(SaveData saveData) throws JsonProcessingException {
        ObjectMapper objectMapper = new ObjectMapper();

        return objectMapper.writeValueAsString(saveData); //JSONString
    }

    public void writeData(String jsonString) throws IOException {
        String path = "src/main/resources/savedata.json";
        FileWriter file = new FileWriter(path);
        file.write(jsonString);
        file.close();
    }

    public Double[] getCosts(SaveData saveData) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();
        return new Double[] {
                saveData.upgrades.finger.cost,
                saveData.upgrades.espressoMachine.cost,
                saveData.upgrades.nintendo.cost,
                saveData.upgrades.mountainDew.cost,
                saveData.upgrades.desperation.cost,
                saveData.upgrades.singer.cost
        };
    }

    public Integer[] getOwned(SaveData saveData) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();
        return new Integer[] {
                saveData.upgrades.finger.own,
                saveData.upgrades.espressoMachine.own,
                saveData.upgrades.nintendo.own,
                saveData.upgrades.mountainDew.own,
                saveData.upgrades.desperation.own,
                saveData.upgrades.singer.own
        };
    }

    public Double[] getIncreaseBy(SaveData saveData) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();
        return new Double[] {
                saveData.upgrades.finger.increaseMPSBy,
                saveData.upgrades.espressoMachine.increaseMPSBy,
                saveData.upgrades.nintendo.increaseMPSBy,
                saveData.upgrades.mountainDew.increaseMPSBy,
                saveData.upgrades.desperation.increaseMPSBy,
                saveData.upgrades.singer.increaseMPSBy
        };
    }

    public void updateValues(SaveData saveData, Double[] costs, Integer[] owned, Integer i) {
        switch(i) {
            case 0:
                saveData.upgrades.finger.cost = costs[0];
                saveData.upgrades.finger.own += 1;
                break;
            case 1:
                saveData.upgrades.espressoMachine.cost = costs[1];
                saveData.upgrades.espressoMachine.own += 1;
                break;
            case 2:
                saveData.upgrades.nintendo.cost = costs[2];
                saveData.upgrades.nintendo.own += 1;
                break;
            case 3:
                saveData.upgrades.mountainDew.cost = costs[3];
                saveData.upgrades.mountainDew.own += 1;
                break;
            case 4:
                saveData.upgrades.desperation.cost = costs[4];
                saveData.upgrades.desperation.own += 1;
                break;
            case 5:
                saveData.upgrades.singer.cost = costs[5];
                saveData.upgrades.singer.own += 1;
                break;
        }
    }
}
