package ca.uw.tongliu.mobihealthapplication;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.ArgumentCaptor;
import org.mockito.Mock;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.spy;

@RunWith(PowerMockRunner.class)
@PrepareForTest(HttpComm.class)
public class HttpCommUnitTest {

    private HttpComm http_comm;

    @Mock
    private Context mockContext;
    @Before
    public void setUp() throws Exception {
        // We will Spy our tested activity so that we will be able to give it some input when
        //  for example the FindViewByID method is called.
    }

    @Test
    public void HttpCommTest() throws Exception {
        // When we call the onCreate...
        http_comm = spy(new HttpComm(mockContext, null));

        http_comm.saveDataToLocalFile("testDataFile", "1234567890");

        String data_string = http_comm.readDataFromLocalFile("testDataFile");

        http_comm.setProtocol("HTTP");
        http_comm.setAuthToken("deadbeef");
        http_comm.setHttpMethod("GET");
        //http_comm.setBaseUrl("http://pyramid-backend.herokuapp.com");
        //http_comm.setUrlResource("api/");
        //http_comm.setUrlPath("patientrecords");

        http_comm.httpAPI();
        assertNotNull(data_string);



    }

}