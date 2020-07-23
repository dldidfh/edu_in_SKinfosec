package com.stuHallReservation.main;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import javax.servlet.http.HttpServletRequest;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.stuHallReservation.beans.*;
@Controller
public class MainController {
	@Autowired
	private SqlSessionTemplate db;
	
	@RequestMapping(value = "main.spring", method=RequestMethod.GET)
	public String main() {
		
		return "main/main";
	}
	@RequestMapping(value = "every_notice.spring", method=RequestMethod.GET)
	public String every_notice() {
		
		return "main/every_notice";
	}
	@RequestMapping(value="main_search_pro.spring", method=RequestMethod.POST)
	public String info_gujang(@RequestParam("search") String search,Model model) {
		
			List<GujangBean> list = db.selectList("gujang.get_main_gujang",search);
			model.addAttribute("gujang_list",list);
		return "ajax/display2";
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
	}
	@RequestMapping(value = "display3_pro.spring", method = RequestMethod.POST)
	public String display3_pro(Model model,YeahyackDayBean bean) {
		
		int gujang_idx = bean.getYeahyack_day_gujang_idx();
		GujangBean bean1 = db.selectOne("gujang.get_all_gujang",gujang_idx);
		int use1 = bean1.getGujang_use_time1();
		int use2 = bean1.getGujang_use_time2();
		String str1 = "yeahyack_time";
		
		ArrayList<String> str2 = new ArrayList<String>();
		for(int i=1;i<use1;i++) {
			str2.add(str1 + String.valueOf(i));
		}
		for(int i=use2+1;i<=24;i++) {
			str2.add(str1 + String.valueOf(i));
		}
		
		
		int chk = db.selectOne("day_insert_chk",bean);
		if(chk == 0) {
			db.insert("yeahyack.day_insert",bean);//day값이 들어감
	
			for(int i=0;i<str2.size();i++) {
				HashMap<String,String> map = new HashMap<String,String>();
				map.put("pick", str2.get(i));
				map.put("yeahyack_day_gujang_idx", String.valueOf(gujang_idx));
				map.put("yeahyack_day", bean.getYeahyack_day());
				db.update("yeahyack.default_yeahyack",map);
			}
			model.addAttribute("msg","OK");
		}else {
			model.addAttribute("msg","OK");
		}
		
		return "common/msg";
	}
	@RequestMapping(value = "display4_pro.spring", method = RequestMethod.POST)
	public String display4_pro(YeahyackDayBean bean,Model model) {

		YeahyackDayBean yeahyack = db.selectOne("yeahyack.get_yeahyack_day",bean);
		model.addAttribute("yeahyack",yeahyack);
		return "ajax/display4";
	}
	@RequestMapping(value = "display5_pro.spring", method = RequestMethod.POST)
	public String display5_pro(int gujang_idx,Model model, YeahyackDayBean bean) {
		
		
		int gujang_pay = db.selectOne("gujang.get_gujang_pay",gujang_idx);
		int yeahyack_day_idx = db.selectOne("yeahyack.get_day_idx",bean);
		model.addAttribute("gujang_pay",gujang_pay);
		model.addAttribute("yeahyack_day_idx",yeahyack_day_idx);
		return "ajax/display5";
	}
	@RequestMapping(value = "result_set_pro.spring", method = RequestMethod.POST)
	public synchronized String result_set_pro(YeahyackBean bean,YeahyackDayBean bean1, String[] picktime,String[] pick_time, Model model,HttpServletRequest request) {
		int yeahyack_check = 0;
		int aaaa = bean1.getYeahyack_day_gujang_idx();
		String gujang_idx = String.valueOf(aaaa);
		for(String pick : picktime) {
	
			HashMap<String,String> map = new HashMap<String,String>();
			map.put("pick", pick);
			map.put("yeahyack_day_gujang_idx", gujang_idx);
			map.put("yeahyack_day", bean1.getYeahyack_day());
			yeahyack_check = db.selectOne("yeahyack.yeahyack_check",map);
		
			if(yeahyack_check == 1)break;
		}
		
		if(yeahyack_check == 1) {
			
		}else {
//			int aaaa = bean1.getYeahyack_day_gujang_idx();
//			String gujang_idx = String.valueOf(aaaa);
			 String p2 = "";
			for(String p1 : pick_time) {
				if(p2 == "") {
					p2 = p2 + p1;
				}else {
					p2 = p2 + "," + p1;
				}
			}
			for(String pick : picktime) {
				
				HashMap<String,String> map = new HashMap<String,String>();
				map.put("pick", pick);
				map.put("yeahyack_day_gujang_idx", gujang_idx);
				map.put("yeahyack_day", bean1.getYeahyack_day());
				db.update("yeahyack.set_return_yeahyack",map);
			}
			
			String yeahyack_IP = request.getRemoteAddr();
			bean.setYeahyack_IP(yeahyack_IP);
			bean.setYeahyack_pick_time(p2);
			db.insert("yeahyack.insert_yeahyack_result",bean);
			
			model.addAttribute("msg","OK");
			
		}
		
		return "common/msg";
	}
}
