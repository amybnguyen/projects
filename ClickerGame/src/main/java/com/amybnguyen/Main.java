package com.amybnguyen;

import java.io.IOException;
import java.text.NumberFormat;
import java.util.concurrent.TimeUnit;


public class Main {
    public static void main(String[] args) throws InterruptedException, IOException {
        // Load game save data
        DataJsonReader dataJsonReader = new DataJsonReader();
        SaveData saveData = dataJsonReader.getData();

        GUI gui = new GUI(saveData);

        // Update user's money balance every second
        long startTime = System.currentTimeMillis();
        while (true) {
            TimeUnit.SECONDS.sleep(1);
            saveData = dataJsonReader.getData();
            saveData.money += saveData.moneyPerSecond;

            gui.moneyLabel.setText("<html>Money: " + NumberFormat.getCurrencyInstance().format(saveData.money) +
                    "<br />Profit per second: " + NumberFormat.getCurrencyInstance().format(saveData.moneyPerSecond) + "</html>");

            String jsonString = dataJsonReader.printData(saveData);
            dataJsonReader.writeData(jsonString);
        }
    }


}


