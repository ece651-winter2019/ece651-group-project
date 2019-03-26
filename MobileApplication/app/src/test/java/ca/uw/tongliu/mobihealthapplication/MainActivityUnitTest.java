package ca.uw.tongliu.mobihealthapplication;

import org.junit.Test;

import static org.junit.Assert.*;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
        import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;

import org.junit.Before;
import org.junit.runner.RunWith;
import org.mockito.ArgumentCaptor;
import org.mockito.Mock;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;

import static org.mockito.Matchers.anyInt;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.doReturn;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.spy;
import static org.powermock.api.support.membermodification.MemberMatcher.method;
import static org.powermock.api.support.membermodification.MemberModifier.suppress;

/**
 * Tests MainActivity in isolation from the system.
 */
@RunWith(PowerMockRunner.class)
@PrepareForTest(MainActivity.class)
public class MainActivityUnitTest {

    private MainActivity tested;

    @Mock
    private Button mockButton;
    private Menu mockMenu;
    private MenuItem menu_item;
    private Context mockContext;
    @Before
    public void setUp() throws Exception {
        // We will Spy our tested activity so that we will be able to give it some input when
        //  for example the FindViewByID method is called.
        tested = spy(MainActivity.class);
        doReturn(mockMenu).when(tested).findViewById(anyInt());
        // We need to suppress methods from the Base Activity. This is why we need PowerMock, there
        //  are other ways but are more intrusive in our code.
        suppress(method(Activity.class, "onCreate", Bundle.class));
        suppress(method(Activity.class, "setContentView", int.class));
    }

    @Test
    public void shouldStartActivity() throws Exception {
        // Let's setup our mockButton so that it will capture the listener
        ArgumentCaptor<MenuItem.OnMenuItemClickListener> captor =
                ArgumentCaptor.forClass(MenuItem.OnMenuItemClickListener.class);

        // When we call the onCreate...
        //tested.onCreate(mock(Bundle.class));

        // Listener should be in place (Was tested before) so now we need to check that it starts
        //  an activity.
        Intent login_intent = new Intent(mockContext, LoginActivity.class);
        doNothing().when(tested).startActivity(login_intent);
        doNothing().when(tested).finish();  // We should also test this to be called in a new test.

        Intent data_input = new Intent(mockContext, UserdataInputActivity.class);
        doNothing().when(tested).startActivity(data_input);
        doNothing().when(tested).finish();  // We should also test this to be called in a new test.

        Intent data_query = new Intent(mockContext, UserDataQueryActivity.class);
        doNothing().when(tested).startActivity(data_query);
        doNothing().when(tested).finish();  // We should also test this to be called in a new test.

        Intent graph = new Intent(mockContext, UserDataGraphActivity.class);
        doNothing().when(tested).startActivity(graph);
        doNothing().when(tested).finish();  // We should also test this to be called in a new test.

        Intent data_list = new Intent(mockContext, UserDataListActivity.class);
        doNothing().when(tested).startActivity(data_list);
        doNothing().when(tested).finish();  // We should also test this to be called in a new test.
    }
}