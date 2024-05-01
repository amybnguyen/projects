package com.amybnguyen;

import javax.swing.*;
import javax.swing.BorderFactory;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.text.NumberFormat;


public class GUI implements ActionListener {
    JFrame frame;
    JPanel panel;
    JLabel moneyLabel;
    JButton manualClick;
    JButton[] buttons = new JButton[6];
    String[] upgradeList = new String[] {
            "finger",
            "espressoMachine",
            "nintendo",
            "mountainDew",
            "desperation",
            "singer"};
    String[] buttonText = new String[] {
            "finger",
            "espresso machine",
            "nintendo",
            "mountain dew",
            "desperation",
            "singer"
    };

    public GUI(SaveData saveData) throws IOException {
        DataJsonReader dataJsonReader = new DataJsonReader();
        ImageIcon[] imageIcons = getImageIcons();
        Double[] costs = dataJsonReader.getCosts(saveData);
        Integer[] owned = dataJsonReader.getOwned(saveData);
        Image espresso = Toolkit.getDefaultToolkit().getImage("src/main/resources/Triple_Shot_Espresso.png");
        ImageIcon espressoIcon = new ImageIcon("src/main/resources/Triple_Shot_Espresso.png");

        frame = new JFrame();
        frame.setIconImage(espresso);
        panel = new JPanel();
        GridLayout layout = new GridLayout(0, 1, 0, 0);
        panel.setLayout(layout);
        panel.setBorder(BorderFactory.createEmptyBorder(10, 30, 10, 30));

        JLabel espressoCup = new JLabel(espressoIcon);
        manualClick = new JButton("Click me");
        manualClick.addActionListener(this);
        moneyLabel = new JLabel("<html>Money: " + NumberFormat.getCurrencyInstance().format(saveData.money) +
                "<<br />Profit per second: " + NumberFormat.getCurrencyInstance().format(saveData.moneyPerSecond) + "</html>");
        moneyLabel.setHorizontalAlignment(SwingConstants.CENTER);
        panel.add(espressoCup);
        panel.add(moneyLabel);
        panel.add(manualClick);

        for (int i = 0; i < buttons.length; i++) {
            buttons[i] = new JButton("<html>Buy a " + buttonText[i] +
                    "<br />Cost: " + NumberFormat.getCurrencyInstance().format(costs[i]) +
                    "<br />Owned: " + owned[i] + "</html>", imageIcons[i]);
            buttons[i].addActionListener(this);
            panel.add(buttons[i]);
        }

        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("That's that me, espresso");
        frame.pack();
        frame.setVisible(true);
    }

    private static ImageIcon[] getImageIcons() {
        ImageIcon fingerIcon = new ImageIcon("src/main/resources/Skeletal_Hand.png");
        ImageIcon espressoMachineIcon = new ImageIcon("src/main/resources/Coffee_Maker.png");
        ImageIcon nintendoIcon = new ImageIcon("src/main/resources/Retro_Radio.png");
        ImageIcon mountainDewIcon = new ImageIcon("src/main/resources/Joja_Cola.png");
        ImageIcon desperationIcon = new ImageIcon("src/main/resources/Emote_Angry.png");
        ImageIcon singerIcon = new ImageIcon("src/main/resources/Emote_Note.png");

        ImageIcon[] imageIcons = new ImageIcon[] {fingerIcon, espressoMachineIcon, nintendoIcon, mountainDewIcon, desperationIcon, singerIcon};
        return imageIcons;
    }

    public static void main(String[] args) throws InterruptedException {
//        GUI gui = new GUI(SaveData saveData);
        }

    @Override
    public void actionPerformed(ActionEvent e) {
        DataJsonReader dataJsonReader = new DataJsonReader();
        SaveData saveData;
        try {
            saveData = dataJsonReader.getData();
        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }

        Object source = e.getSource();
        Double[] costs;
        Integer[] owned;
        Double[] increaseBy;
        try {
            costs = dataJsonReader.getCosts(saveData);
            owned = dataJsonReader.getOwned(saveData);
            increaseBy = dataJsonReader.getIncreaseBy(saveData);
        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }

        if (source.equals(manualClick)) {
            saveData.money++;
        }
        else {
            for (int i = 0; i < buttons.length; i++) {
                if (source.equals(buttons[i]) && saveData.money >= costs[i]) {
                    saveData.money -= costs[i];
                    saveData.moneyPerSecond += increaseBy[i];
                    costs[i] *= 1.1;
                    owned[i]++;
                    buttons[i].setText("<html>Buy a " + buttonText[i] +
                            "<br />Cost: " + NumberFormat.getCurrencyInstance().format(costs[i]) +
                            "<br />Owned: " + owned[i] + "</html>");
                    dataJsonReader.updateValues(saveData, costs, owned, i);
                }
            }
        }
        moneyLabel.setText("<html>Money: " + NumberFormat.getCurrencyInstance().format(saveData.money) +
                "<br />Profit per second: " + NumberFormat.getCurrencyInstance().format(saveData.moneyPerSecond) + "</html>");

        try {
            dataJsonReader.writeData(dataJsonReader.printData(saveData));
        } catch (IOException ex) {
            System.out.println("Error");
            throw new RuntimeException(ex);
        }
    }
}
