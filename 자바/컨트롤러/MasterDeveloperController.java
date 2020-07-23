package com.stuHallReservation.main;

import java.util.HashMap;
import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.stuHallReservation.beans.*;

@Controller
public class MasterDeveloperController {
	@Autowired
	private SqlSessionTemplate db;
	@RequestMapping(value="developer_main.spring", method=RequestMethod.GET)
	public String developer_main_spring(Model model) {
		List<UserBean> list = db.selectList("user.developer_get_user_info");
		model.addAttribute("user_list",list);
		return "developer/main";
	}
	@RequestMapping(value="change_status.spring", method=RequestMethod.POST)
	public String change_status(UserBean user_bean, Model model){
		
		db.update("user.set_user_status",user_bean.getUser_idx());
		model.addAttribute("msg","OK");
		return "common/msg";
	}
	@RequestMapping(value="change_status2.spring", method=RequestMethod.POST)
	public String change_status2(UserBean user_bean, Model model){
		
		db.update("user.set_user_status2",user_bean.getUser_idx());
		model.addAttribute("msg","OK");
		return "common/msg";
	}
	@RequestMapping(value="spead_black_list.spring", method=RequestMethod.POST)
	public String spead_black_list(Model model,@RequestParam(defaultValue="")String search_id, @RequestParam(defaultValue="1") int now_page){
		PagingBean pagingBean = new PagingBean();
		int listCnt = db.selectOne("user.developer_get_user_info_2_cnt", search_id);
		int min_p =  1 + ((now_page - 1) * 5);
		int max_p = min_p + (5 - 1); 
		String min = String.valueOf(min_p);
		String max = String.valueOf(max_p);
		int a1 = listCnt / 5;
		if(listCnt % 5 >0){
			a1++;
		}
		pagingBean.setAllpage_cnt(a1);
		int a2 = (now_page - 1) / 5;
		int a3 = (a2*5) + 1;
		pagingBean.setPagination_min(a3);
		int a4 = a3 + 5-1;
		if(a4 > pagingBean.getAllpage_cnt()) {
			a4 = pagingBean.getAllpage_cnt();
		}
		pagingBean.setPagination_max(a4);
		pagingBean.setPagination_cnt(5);
		pagingBean.setCnt_per_page(5);
		pagingBean.setNow_page(now_page);
		
		HashMap<String, String> map = new HashMap<String, String>();
		map.put("search_id", search_id);
		map.put("min", min);
		map.put("max", max);
		
		List<UserBean> list2 = db.selectList("user.developer_get_user_info_2",map);
		
		model.addAttribute("user_list2",list2);
		model.addAttribute("page_bean",pagingBean);
		return "developer/black_list";
	}
	
}
