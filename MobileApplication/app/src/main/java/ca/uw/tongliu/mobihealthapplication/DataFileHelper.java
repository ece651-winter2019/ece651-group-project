package ca.uw.tongliu.mobihealthapplication;

import android.content.Context;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class DataFileHelper {
    private Context activityContext = null;
    DataFileHelper(Context context){
        activityContext = context;
    }

    public boolean isFileExist(String filename){
        File file = new File(activityContext.getFilesDir(), filename);
        boolean exists = false;
        exists = file.exists();
        return exists;

    }

    public void saveDataToLocalFile(String filename ,String Data) {
        File file = new File(activityContext.getFilesDir(), filename);

        FileOutputStream fileOutputStream = null;
        try {
            fileOutputStream = new FileOutputStream(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        OutputStreamWriter outputStreamWriter = new OutputStreamWriter(fileOutputStream);

        BufferedWriter bufferedWriter = new BufferedWriter(outputStreamWriter);

        try {
            bufferedWriter.write(Data);
            bufferedWriter.flush();
            bufferedWriter.close();
            outputStreamWriter.close();
            fileOutputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String readDataFromLocalFile(String filename)
    {
        StringBuffer file_contents = new StringBuffer ();
        String lineData="";
        File file = new File(activityContext.getFilesDir(), filename);

        FileInputStream fileInputStream = null;

        try {
            fileInputStream = new FileInputStream(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace ( );
        }

        if ( fileInputStream != null){
            InputStreamReader inputStreamReader = new InputStreamReader(fileInputStream);
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

            try {
                lineData = bufferedReader.readLine();
                while(lineData!=null){
                    file_contents.append (lineData);
                    lineData = bufferedReader.readLine();
                }

            } catch (IOException e) {
                e.printStackTrace ( );
            }
        }
        return file_contents.toString ();
    }

}
