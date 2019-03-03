package ca.uw.ece.mobileapplication;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

public class DataInquiryAvtivity extends FragmentActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

                try {

                    //baseUrl = "http://192.168.92.210:6543/";
                    String httpmethod = "GET";

                    JSONObject jsondata = buidJsonObject();
                    HttpComm http_comm = new HttpComm(
                            httpmethod
                            ,jsondata
                    );

                    http_comm.setUrlResource("records");
                    http_comm.setUrlPath("tliu");
                    AsyncTask<String, Void, String> execute = new ExecuteNetworkOperation(http_comm);
                    execute.execute();

                } catch (Exception ex) {
                }
    }

    private JSONObject buidJsonObject() throws JSONException {

        JSONObject jsonObject = new JSONObject();
        jsonObject.accumulate("userid",1);

        return jsonObject;
    }

    /**
     * This subclass handles the network operations in a new thread.
     * It starts the progress bar, makes the API call, and ends the progress bar.
     */

    private class ExecuteNetworkOperation extends AsyncTask<String, Void, String> {
        HttpComm data_inquiry_http_comm;
        /**
         * Overload the constructor to pass objects to this class.
         */
        public ExecuteNetworkOperation(HttpComm http_comm) {
            this.data_inquiry_http_comm = http_comm;
        }

        @Override
        protected String doInBackground(String... urls) {
            // params comes from the execute() call: params[0] is the url.
            try {
                try {
                    return data_inquiry_http_comm.httpAPI();
                } catch (JSONException e) {
                    return "Error!";
                }
            } catch (IOException e) {
                return "Unable to retrieve web page. URL may be invalid.";
            }
        }
        // onPostExecute displays the results of the AsyncTask.
        @Override
        protected void onPostExecute(String result) {
//            mDataText.setText(result);
        }
    }

}
