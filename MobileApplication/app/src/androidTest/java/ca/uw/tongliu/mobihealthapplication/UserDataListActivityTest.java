package ca.uw.tongliu.mobihealthapplication;

import android.content.Context;
import android.widget.ListView;
import ca.uw.tongliu.mobihealthapplication.ListViewAdapter;

import org.junit.Rule;
import org.junit.Test;

import java.util.ArrayList;
import java.util.HashMap;

import androidx.test.InstrumentationRegistry;
import androidx.test.rule.ActivityTestRule;

import static org.junit.Assert.*;

public class UserDataListActivityTest {
    @Rule
    public ActivityTestRule<UserDataListActivity> mActivityRule = new ActivityTestRule<>(UserDataListActivity.class);

    @Test
    public void papulateListTest(){
        ListView user_data_listView;
        ArrayList<HashMap<String, String>> list;

        user_data_listView = (ListView)mActivityRule.getActivity().findViewById(R.id.dataListView);
        String user_data = "[{\"id\":2,\"user\":22,\"bp_systolic\":165,\"bp_diastolic\":70,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T17:58:35Z\",\"height\":\"180\"},{\"id\":12,\"user\":22,\"bp_systolic\":100,\"bp_diastolic\":123,\"heart_rate\":66,\"weight\":180,\"created_on\":\"2019-03-18T17:58:35Z\",\"height\":\"180\"},{\"id\":22,\"user\":22,\"bp_systolic\":1200,\"bp_diastolic\":70,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T17:58:35Z\",\"height\":\"180\"},{\"id\":32,\"user\":22,\"bp_systolic\":1200,\"bp_diastolic\":800,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T17:58:35Z\",\"height\":\"181\"},{\"id\":42,\"user\":22,\"bp_systolic\":1200,\"bp_diastolic\":800,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T17:58:36Z\",\"height\":\"160\"},{\"id\":52,\"user\":22,\"bp_systolic\":1200,\"bp_diastolic\":800,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T17:58:36Z\",\"height\":\"160\"},{\"id\":62,\"user\":32,\"bp_systolic\":165,\"bp_diastolic\":70,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T18:49:03Z\",\"height\":\"180\"},{\"id\":72,\"user\":32,\"bp_systolic\":100,\"bp_diastolic\":123,\"heart_rate\":66,\"weight\":180,\"created_on\":\"2019-03-18T18:49:03Z\",\"height\":\"180\"},{\"id\":82,\"user\":32,\"bp_systolic\":1200,\"bp_diastolic\":70,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T18:49:03Z\",\"height\":\"180\"},{\"id\":92,\"user\":32,\"bp_systolic\":1200,\"bp_diastolic\":800,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T18:49:03Z\",\"height\":\"181\"},{\"id\":102,\"user\":32,\"bp_systolic\":1200,\"bp_diastolic\":800,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T18:49:03Z\",\"height\":\"160\"},{\"id\":112,\"user\":32,\"bp_systolic\":1200,\"bp_diastolic\":800,\"heart_rate\":60,\"weight\":180,\"created_on\":\"2019-03-18T18:49:04Z\",\"height\":\"160\"},{\"id\":122,\"user\":32,\"bp_systolic\":1,\"bp_diastolic\":1,\"heart_rate\":1,\"weight\":1,\"created_on\":\"2019-03-18T18:56:57Z\",\"height\":\"1\"},{\"id\":132,\"user\":32,\"bp_systolic\":5,\"bp_diastolic\":5,\"heart_rate\":5,\"weight\":5,\"created_on\":\"2019-03-20T12:35:03Z\",\"height\":\"5\"},{\"id\":142,\"user\":22,\"bp_systolic\":110,\"bp_diastolic\":70,\"heart_rate\":79,\"weight\":150,\"created_on\":\"2019-03-21T22:29:59Z\",\"height\":\"173\"},{\"id\":152,\"user\":22,\"bp_systolic\":140,\"bp_diastolic\":90,\"heart_rate\":90,\"weight\":150,\"created_on\":\"2019-03-22T03:01:16Z\",\"height\":\"173\"},{\"id\":162,\"user\":22,\"bp_systolic\":140,\"bp_diastolic\":90,\"heart_rate\":90,\"weight\":150,\"created_on\":\"2019-03-22T03:01:17Z\",\"height\":\"173\"},{\"id\":172,\"user\":22,\"bp_systolic\":140,\"bp_diastolic\":90,\"heart_rate\":90,\"weight\":150,\"created_on\":\"2019-03-22T03:01:17Z\",\"height\":\"173\"},{\"id\":182,\"user\":22,\"bp_systolic\":140,\"bp_diastolic\":90,\"heart_rate\":90,\"weight\":150,\"created_on\":\"2019-03-22T03:01:38Z\",\"height\":\"173\"},{\"id\":192,\"user\":22,\"bp_systolic\":110,\"bp_diastolic\":70,\"heart_rate\":80,\"weight\":140,\"created_on\":\"2019-03-22T03:35:59Z\",\"height\":\"173\"},{\"id\":202,\"user\":22,\"bp_systolic\":120,\"bp_diastolic\":78,\"heart_rate\":66,\"weight\":140,\"created_on\":\"2019-03-24T00:42:55Z\",\"height\":\"174\"},{\"id\":212,\"user\":22,\"bp_systolic\":110,\"bp_diastolic\":80,\"heart_rate\":75,\"weight\":140,\"created_on\":\"2019-03-25T16:01:00Z\",\"height\":\"175\"},{\"id\":222,\"user\":22,\"bp_systolic\":120,\"bp_diastolic\":75,\"heart_rate\":65,\"weight\":150,\"created_on\":\"2019-03-26T03:25:22Z\",\"height\":\"175\"},{\"id\":232,\"user\":22,\"bp_systolic\":120,\"bp_diastolic\":75,\"heart_rate\":65,\"weight\":150,\"created_on\":\"2019-03-26T03:28:20Z\",\"height\":\"175\"},{\"id\":242,\"user\":22,\"bp_systolic\":120,\"bp_diastolic\":75,\"heart_rate\":65,\"weight\":150,\"created_on\":\"2019-03-26T14:16:48Z\",\"height\":\"175\"},{\"id\":252,\"user\":22,\"bp_systolic\":120,\"bp_diastolic\":75,\"heart_rate\":65,\"weight\":150,\"created_on\":\"2019-03-26T14:38:39Z\",\"height\":\"175\"},{\"id\":262,\"user\":22,\"bp_systolic\":100,\"bp_diastolic\":70,\"heart_rate\":66,\"weight\":160,\"created_on\":\"2019-03-26T20:39:32Z\",\"height\":\"175\"},{\"id\":272,\"user\":22,\"bp_systolic\":90,\"bp_diastolic\":60,\"heart_rate\":70,\"weight\":150,\"created_on\":\"2019-03-26T20:59:33Z\",\"height\":\"175\"}]";
        list = mActivityRule.getActivity().populateList(user_data);
        if ( list == null )
            return;
        ListViewAdapter adapter=new ListViewAdapter(mActivityRule.getActivity(), list);


    }


}