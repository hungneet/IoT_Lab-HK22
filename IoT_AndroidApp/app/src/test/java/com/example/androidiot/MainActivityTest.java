package com.example.androidiot;

import static org.junit.Assert.*;

import android.widget.TextView;
import android.widget.ToggleButton;


import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.MqttPersistenceException;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mockito;
import org.robolectric.Robolectric;
import org.robolectric.RobolectricTestRunner;


import java.nio.charset.Charset;

@RunWith(RobolectricTestRunner.class)
public class MainActivityTest {

    private MainActivity activity;
    private MQTTHelper mqttHelper;
    private TextView temp_screen, humi_screen, light_screen;
    private ToggleButton pumpbtn, lightbtn, fanbtn;

    @Before
    public void setUp() {
        activity = Robolectric.buildActivity(MainActivity.class).create().get();
        mqttHelper = Mockito.mock(MQTTHelper.class);
        temp_screen = activity.findViewById(R.id.temp_screen);
        humi_screen = activity.findViewById(R.id.humi_screen);
        light_screen = activity.findViewById(R.id.light_screen);
        pumpbtn = activity.findViewById(R.id.pumpbtn);
        lightbtn = activity.findViewById(R.id.lightbtn);
        fanbtn = activity.findViewById(R.id.fanbtn);
    }

    @Test
    public void testPumpButton() throws MqttException {
        pumpbtn.performClick();
        Mockito.verify(mqttHelper).mqttAndroidClient.publish("hungneet/feeds/button1", new MqttMessage("1".getBytes(Charset.forName("UTF-8"))));
        pumpbtn.performClick();
        Mockito.verify(mqttHelper).mqttAndroidClient.publish("hungneet/feeds/button1", new MqttMessage("0".getBytes(Charset.forName("UTF-8"))));
    }

    @Test
    public void testLightButton() throws MqttException {
        lightbtn.performClick();
        Mockito.verify(mqttHelper).mqttAndroidClient.publish("hungneet/feeds/button3", new MqttMessage("1".getBytes(Charset.forName("UTF-8"))));
        lightbtn.performClick();
        Mockito.verify(mqttHelper).mqttAndroidClient.publish("hungneet/feeds/button3", new MqttMessage("0".getBytes(Charset.forName("UTF-8"))));
    }

    @Test
    public void testFanButton() throws MqttException {
        fanbtn.performClick();
        Mockito.verify(mqttHelper).mqttAndroidClient.publish("hungneet/feeds/button2", new MqttMessage("1".getBytes(Charset.forName("UTF-8"))));
        fanbtn.performClick();
        Mockito.verify(mqttHelper).mqttAndroidClient.publish("hungneet/feeds/button2", new MqttMessage("0".getBytes(Charset.forName("UTF-8"))));
    }

    @Test
    public void testStartMQTT() {
        activity.startMQTT();
        Mockito.verify(mqttHelper).setCallback(Mockito.any(MqttCallbackExtended.class));
    }

    @Test
    public void testSendDataMQTT() throws MqttException, MqttPersistenceException {
        activity.mqttHelper = mqttHelper;
        activity.sendDataMQTT("test_topic", "test_value");
        Mockito.verify(mqttHelper.mqttAndroidClient).publish("test_topic", new MqttMessage("test_value".getBytes(Charset.forName("UTF-8"))));
    }
}
