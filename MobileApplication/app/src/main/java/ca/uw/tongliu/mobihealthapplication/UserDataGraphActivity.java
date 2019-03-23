package ca.uw.tongliu.mobihealthapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.webkit.WebView;

import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.LegendRenderer;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.BarGraphSeries;
import com.jjoe64.graphview.series.LineGraphSeries;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;


public class UserDataGraphActivity extends AppCompatActivity {
    private String user_data = null;
    int total_records = 0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate (savedInstanceState);
        setContentView (R.layout.activity_user_data_graph);
        GraphView graph = (GraphView) findViewById(R.id.graph);

        WebView webView = (WebView) findViewById (R.id.graphwebview);
        webView.loadUrl ("file:///android_asset/heart2.html");

        LineGraphSeries<DataPoint> series0 = new LineGraphSeries<>(generateData(0));
        series0.setTitle("Systolic");
        series0.setColor(Color.argb(255, 255, 0, 0));
        series0.setDrawDataPoints(true);
        series0.setAnimated (true);
        series0.setThickness (10);
        graph.addSeries(series0);
        LineGraphSeries<DataPoint> series1 = new LineGraphSeries<>(generateData(1));
        series1.setColor(Color.argb(255, 0, 255, 0));
        series1.setTitle("Diastolic");
        series0.setAnimated (true);
        series0.setThickness (10);
        graph.addSeries(series1);
        LineGraphSeries<DataPoint> series2 = new LineGraphSeries<>(generateData(2));
        series2.setColor(Color.argb(255, 0, 0, 255));
        series2.setTitle("Heart Rate");
        series2.setAnimated (true);
        series2.setThickness (10);
        graph.addSeries(series2);
        graph.getViewport ().setXAxisBoundsManual (true);
        graph.getViewport ().setMinX (0);
        graph.getViewport ().setMaxX (total_records);
        graph.getLegendRenderer ().setVisible (true);
        graph.getLegendRenderer ().setAlign (LegendRenderer.LegendAlign.TOP);

    }

    private DataPoint[] generateData(int index) {
        user_data = ReadDataFromLocalFile();

        if ( user_data == null)
            return null;
        JSONArray jsonArray = null;
        try {
            jsonArray = new JSONArray (user_data);
        } catch (JSONException e) {
            e.printStackTrace ( );
        }
        double tmp_data = 0.0;
        DataPoint v;
        int count = jsonArray.length ( );
        DataPoint[] values = new DataPoint[count];
        try {
            //jsonArray = new JSONArray (user_data);
            for (int i = 0; i < count ; i++) {
                JSONObject recordObject = jsonArray.getJSONObject (i);
                if ( index == 0 ){
                    tmp_data = recordObject.getDouble ("bp_systolic");
                }
                else if(index == 1){
                    tmp_data = recordObject.getDouble ("bp_diastolic");
                }
                else if(index == 2){
                    tmp_data = recordObject.getDouble ("heart_rate");
                }
                if ( tmp_data > 200 ) tmp_data = tmp_data / 10;
                v = new DataPoint(i, tmp_data);
                values[i] = v;
            }
        } catch (JSONException e) {
            e.printStackTrace ( );
        }
        total_records = count;
        return values;
    }

    private String ReadDataFromLocalFile() {
        String filename = "bpData";
        StringBuffer file_contents = new StringBuffer ( );
        String lineData = "";
        File file = new File (getFilesDir ( ), filename);

        FileInputStream fileInputStream = null;

        try {
            fileInputStream = new FileInputStream (file);
        } catch (FileNotFoundException e) {
            e.printStackTrace ( );
        }

        if (fileInputStream != null) {
            InputStreamReader inputStreamReader = new InputStreamReader (fileInputStream);
            BufferedReader bufferedReader = new BufferedReader (inputStreamReader);

            try {
                lineData = bufferedReader.readLine ( );
                while (lineData != null) {
                    file_contents.append (lineData);
                    lineData = bufferedReader.readLine ( );
                }

            } catch (IOException e) {
                e.printStackTrace ( );
            }
        }
        return file_contents.toString ( );
    }
}
