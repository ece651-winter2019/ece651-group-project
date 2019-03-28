package ca.uw.tongliu.mobihealthapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.animation.Animator;
import android.animation.AnimatorListenerAdapter;
import android.annotation.TargetApi;
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.text.format.DateUtils;
import android.view.View;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.BufferedWriter;
import java.io.File;
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;
import java.text.SimpleDateFormat;

public class UserDataQueryActivity extends AppCompatActivity {
    private View mProgressView;
    private TextView mTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_data_query);

        mTextView = findViewById(R.id.textView2);
        mProgressView = findViewById(R.id.progressBar);

        boolean fetch_succeed = FetchUserData();
        if (fetch_succeed == false){
            Intent login_intent = new Intent(this, LoginActivity.class );
            startActivity(login_intent);
            finish();
        }
    }

    private FetchUserDataTask mFetchDataTask;
    String ret_data_string = "";
    JSONObject ret_data_obj = null;

    public boolean FetchUserData(){            // Show a progress spinner, and kick off a background task to
        // perform the user login attempt.
        long oneWeek =  0;
        long oneMonth =  0;
        oneWeek = 1000 * 3600 * 24 * 7;
        String start_date_time = null;
        SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");
        df.setTimeZone (TimeZone.getTimeZone("UTC"));
        Date currentTime = Calendar.getInstance().getTime ();
        String end_date_time = df.format (currentTime);
        String url_path = null;
        start_date_time = df.format (new Date (currentTime.getTime()- (oneWeek * 4) ));
        showProgress(false);
        HttpComm http_comm = new HttpComm(
                getApplicationContext(),
                null
        );
        http_comm.setHttpMethod("GET");
        String token = http_comm.readDataFromLocalFile("auth_token");
        if ( token.equals("")){
            return false;
        }
        http_comm.setUrlResource("api/patientrecords");
        url_path = "?created_on__gte="+start_date_time+"&created_on__lte="+end_date_time;
        http_comm.setUrlPath (url_path);
        http_comm.setAuthToken (token);
        mFetchDataTask = new FetchUserDataTask(http_comm);
        mFetchDataTask.execute();
        return true;
    }


    /**
     * Represents an asynchronous login/registration task used to authenticate
     * the user.
     */
    public class FetchUserDataTask extends AsyncTask<String, Void, String> {
        HttpComm fetch_data_http_comm;


        public FetchUserDataTask(HttpComm http_comm) {
            fetch_data_http_comm = http_comm;
        }

        @Override
        protected String doInBackground(String... params) {
            // params comes from the execute() call: params[0] is the url.
            int retry = 0;
            final int max_retry = 3;
            String return_v = null;
            while ((retry < max_retry) && (return_v == null)){
                try {
                    try {
                        ret_data_string = fetch_data_http_comm.httpAPI ( );
                        return_v = ret_data_string;
                    } catch (JSONException e) {
                        return_v = null;
                    }
                }
                catch( IOException io_e){
                    return_v = null;
                }
                retry++;
            }

            // TODO: register the new account here.
            return return_v;
        }

        @Override
        protected void onPostExecute(String ret_msg) {
            mFetchDataTask = null;
            if (ret_msg != null) {
                //mTextView.setText (ret_msg);
                fetch_data_http_comm.saveDataToLocalFile ("bpData",ret_msg);
            }
            finish();
            showProgress(false);
        }

        @Override
        protected void onCancelled() {
            mFetchDataTask = null;
        }

    }
    @TargetApi(Build.VERSION_CODES.HONEYCOMB_MR2)
    private void showProgress(final boolean show) {
        // On Honeycomb MR2 we have the ViewPropertyAnimator APIs, which allow
        // for very easy animations. If available, use these APIs to fade-in
        // the progress spinner.
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB_MR2) {
            int shortAnimTime = getResources().getInteger(android.R.integer.config_shortAnimTime);

            mTextView.setVisibility(show ? View.GONE : View.VISIBLE);
            mTextView.animate().setDuration(shortAnimTime).alpha(
                    show ? 0 : 1).setListener(new AnimatorListenerAdapter() {
                @Override
                public void onAnimationEnd(Animator animation) {
                    mTextView.setVisibility(show ? View.GONE : View.VISIBLE);
                }
            });

            mProgressView.setVisibility(show ? View.VISIBLE : View.GONE);
            mProgressView.animate().setDuration(shortAnimTime).alpha(
                    show ? 1 : 0).setListener(new AnimatorListenerAdapter() {
                @Override
                public void onAnimationEnd(Animator animation) {
                    mProgressView.setVisibility(show ? View.VISIBLE : View.GONE);
                }
            });
        } else {
            // The ViewPropertyAnimator APIs are not available, so simply show
            // and hide the relevant UI components.
            mProgressView.setVisibility(show ? View.VISIBLE : View.GONE);
            mTextView.setVisibility(show ? View.GONE : View.VISIBLE);
        }
    }


}
