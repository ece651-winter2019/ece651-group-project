package ca.uw.ece.mobileapplication;

import org.json.JSONException;
import org.json.JSONObject;
import java.io.IOException;

import java.util.HashMap;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;


public class HttpComm {

    private String baseUrl = "http://192.168.92.210:6543/";
    private String data1;
    private String data2;
    private String data3;
    private String urlResource;
    private String httpMethod; // GET, POST, PUT, DELETE
    private String urlPath;
    private String lastResponse;
    private JSONObject jsonObject;

    /**
     *
     * @param baseUrl String
     * @param data1 String
     * @param data2 String
     * @param httpmethod String
     */
    public HttpComm(String httpmethod, JSONObject jsonObjectData) {
        this.baseUrl = baseUrl;
        this.urlResource = "";
        this.urlPath = "";
        this.httpMethod = httpmethod;
        lastResponse = "";
        jsonObject = jsonObjectData;
        // This is important. The application may break without this line.
        System.setProperty("jsse.enableSNIExtension", "false");
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

    private void settingGetContent(HttpURLConnection conn) {
        // Timeout for reading InputStream arbitrarily set to 3000ms.
        conn.setReadTimeout(3000);
        // Timeout for connection.connect() arbitrarily set to 3000ms.
        conn.setConnectTimeout(3000);
        conn.setDoInput(true);
    }

    public String httpAPI() throws IOException, JSONException {
        String result = "";
        StringBuilder outputStringBuilder = new StringBuilder();

        URL url = new URL(baseUrl+urlResource);

        // 1. create HttpURLConnection
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod(httpMethod);
        conn.setRequestProperty("Content-Type", "application/json; charset=utf-8");

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

}
