package ca.uw.tongliu.mobihealthapplication;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import javax.net.ssl.HttpsURLConnection;
import java.net.HttpURLConnection;
import java.net.URL;
import android.content.Context;


public class HttpComm {

    private String baseUrl = "https://pyramid-backend.herokuapp.com/";
    private String urlResource;
    private String httpMethod; // GET, POST, PUT, DELETE
    private String urlPath;
    private String lastResponse;
    private JSONObject jsonObject;
    private String token = null;
    private Context activityContext = null;
    private String httpProtocol = "HTTPS";

    /**
     *
     * @param httpMethod String
     * @param jsonObjectData JSONObject
     */
    public HttpComm(Context context, JSONObject jsonObjectData) {
        this.activityContext = context;
        this.baseUrl = baseUrl;
        this.urlResource = "";
        this.urlPath = "";
        lastResponse = "";
        jsonObject = jsonObjectData;
        // This is important. The application may break without this line.
        System.setProperty("jsse.enableSNIExtension", "false");
    }

    private void setPostRequestContent(HttpsURLConnection conn, JSONObject jsonObject) throws IOException {
        conn.setDoInput(true);
        conn.setDoOutput(true);

        OutputStream os = conn.getOutputStream();
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(os, "UTF-8"));
        writer.write(jsonObject.toString());
        writer.flush();
        writer.close();
        os.close();
    }
    private void setPostRequestContent(HttpURLConnection conn, JSONObject jsonObject) throws IOException {
        conn.setDoInput(true);
        conn.setDoOutput(true);

        OutputStream os = conn.getOutputStream();
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(os, "UTF-8"));
        writer.write(jsonObject.toString());
        writer.flush();
        writer.close();
        os.close();
    }

    private void settingGetContent(HttpsURLConnection conn) {
        // Timeout for reading InputStream arbitrarily set to 3000ms.
        conn.setReadTimeout(3000);
        // Timeout for connection.connect() arbitrarily set to 3000ms.
        conn.setConnectTimeout(3000);
        conn.setDoInput(true);
    }

    private void settingGetContent(HttpURLConnection conn) {
        // Timeout for reading InputStream arbitrarily set to 3000ms.
        conn.setReadTimeout(3000);
        // Timeout for connection.connect() arbitrarily set to 3000ms.
        conn.setConnectTimeout(3000);
        conn.setDoInput(true);
    }

    public void setProtocol(String http_protocol){
        httpProtocol = http_protocol;
    }

    public void setAuthToken(String token){
        this.token = token;
    }

    public String httpAPI() throws IOException, JSONException {
        String result = "";
        StringBuilder outputStringBuilder = new StringBuilder();

        URL url = new URL(baseUrl+urlResource+urlPath);

        HttpURLConnection conn;
        // 1. create HttpURLConnection
        if ( httpProtocol.equals("HTTP")) conn = (HttpURLConnection) url.openConnection();
        else conn = (HttpsURLConnection) url.openConnection();
        conn.setRequestMethod(httpMethod);
        conn.setRequestProperty("Content-Type", "application/json; charset=utf-8");
        if ( token != null)
            conn.setRequestProperty ("Authorization","Token "+ token);

        if ( httpMethod.equals("POST")) {
            // 2. build JSON object
            //JSONObject jsonObject = buidJsonObject();

            // 3. add JSON content to POST request body
            setPostRequestContent(conn, jsonObject);
        }
        else{
            settingGetContent(conn);
        }
        // 4. make request to the given URL
        conn.connect();

        // 5. return response message
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        while ((result = br.readLine()) != null) {
            outputStringBuilder.append(result);
        }
        return outputStringBuilder.toString();

    }

    /**
    * --&gt;http://BASE_URL.COM&lt;--/resource/path
    * @param baseUrl the root part of the URL
    * @return this
    */
    public HttpComm setBaseUrl(String baseUrl) {
        this.baseUrl = baseUrl;
        if (!baseUrl.substring(baseUrl.length() - 1).equals("/")) {
            this.baseUrl += "/";
        }
        return this;
    }

    /**
     * Set the name of the resource that is used for calling the Rest API.
     * @param urlResource http://base_url.com/--&gt;URL_RESOURCE&lt;--/url_path
     * @return this
     */
    public HttpComm setUrlResource(String urlResource) {
        this.urlResource = urlResource;
        return this;
    }

    /**
     * Set the path  that is used for calling the Rest API.
     * This is usually an ID number for Get single record, PUT, and DELETE functions.
     * @param urlPath http://base_url.com/resource/--&gt;URL_PATH&lt;--
     * @return this
     */
    public final HttpComm setUrlPath(String urlPath) {
        this.urlPath = urlPath;
        return this;
    }

    /**
     * Sets the HTTP method used for the Rest API.
     * GET, PUT, POST, or DELETE
     * @return this
     */
    public HttpComm setHttpMethod(String httpMethod) {
        this.httpMethod = httpMethod;
        return this;
    }

    /**
     * Get the output from the last call made to the Rest API.
     * @return String
     */
    public String getLastResponse() {
        return lastResponse;
    }

    public void saveDataToLocalFile(String filename ,String Data) {
        DataFileHelper file_helper = new DataFileHelper(activityContext);
        file_helper.saveDataToLocalFile(filename, Data);
    }

    public String readDataFromLocalFile(String filename)
    {
        String readin_data;
        DataFileHelper fileHelper = new DataFileHelper(activityContext);
        readin_data = fileHelper.readDataFromLocalFile(filename);
        return readin_data;
    }


}
