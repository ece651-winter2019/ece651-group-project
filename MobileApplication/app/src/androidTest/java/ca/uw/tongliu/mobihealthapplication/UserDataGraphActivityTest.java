package ca.uw.tongliu.mobihealthapplication;

import android.content.Context;

import com.jjoe64.graphview.GraphView;

import org.junit.Rule;
import org.junit.Test;

import androidx.test.InstrumentationRegistry;
import androidx.test.rule.ActivityTestRule;

import static org.junit.Assert.*;

public class UserDataGraphActivityTest {

    @Rule
    public ActivityTestRule<UserDataGraphActivity> mActivityRule = new ActivityTestRule<>(UserDataGraphActivity.class);

    @Test
    public void useAppContext() {
        // Context of the app under test.
        Context appContext = InstrumentationRegistry.getTargetContext();

        assertEquals("ca.uw.tongliu.mobihealthapplication", appContext.getPackageName());
    }

    @Test
    public void drawGraphTest(){
        GraphView graph = mActivityRule.getActivity().findViewById(R.id.graph);
        mActivityRule.getActivity().createPoltInGraph(graph, 0);
        mActivityRule.getActivity().createPoltInGraph(graph, 1);
        mActivityRule.getActivity().createPoltInGraph(graph, 2);

    }
}