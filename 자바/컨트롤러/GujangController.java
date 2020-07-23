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
public class GujangController {
	
	
	@Autowired
	private SqlSessionTemplate db;
	@RequestMapping(value="gujangsearch.spring", method=RequestMethod.GET)
	public String gujangsearch() {
		
		return "client/gujangsearch";
	}
	
	@RequestMapping(value="goto_gujang.spring", method=RequestMethod.GET)
	public String goto_gujang(Model model,@RequestParam("gujang_idx") int gujang_idx) {
		
		GujangBean bean = db.selectOne("gujang.get_all_gujang",gujang_idx);
		model.addAttribute("gujang_bean",bean);
//		List<GujangNoticeBean> list =db.selectList("notice.get_gujang_notice",gujang_idx);
//		model.addAttribute("gujang_notice_list",list);
		
		return "client/goto_gujang";
	}
	
	
		
	@RequestMapping(value="info_gujang_pro.spring", method=RequestMethod.GET)
	public String info_gujang(@RequestParam(defaultValue="") String search,Model model,@RequestParam(defaultValue="1") int now_page) {
			PagingBean pagingBean = new PagingBean();
			int listCnt = db.selectOne("gujang.get_gujang_cnt",search);
			int min_p =  1 + ((now_page - 1) * 5);
			int max_p = min_p + (5 - 1); 
			String min = String.valueOf(min_p);
			String max = String.valueOf(max_p);
			int a1 = listCnt / 5;
			if(listCnt % 5 >0){
				a1++;
			}
			pagingBean.setAllpage_cnt(a1);
			int a2 = (now_page - 1) / 10;
			int a3 = (a2*10) + 1;
			pagingBean.setPagination_min(a3);
			int a4 = a3 + 10-1;
			if(a4 > pagingBean.getAllpage_cnt()) {
				a4 = pagingBean.getAllpage_cnt();
			}
			pagingBean.setPagination_max(a4);
			pagingBean.setPagination_cnt(10);
			pagingBean.setCnt_per_page(5);
			pagingBean.setNow_page(now_page);
			
			HashMap<String, String> map = new HashMap<String, String>();
			map.put("search", search);
			map.put("min", min);
			map.put("max", max);
			
			List<GujangBean> list = db.selectList("gujang.get_gujang",map);
			
			model.addAttribute("page_bean",pagingBean);
			model.addAttribute("gujang_list",list);
			model.addAttribute("search",search);
		return "client/info_gujang";
	}

	@RequestMapping(value="spead_notice.spring", method=RequestMethod.POST)
	public String spead_notice(Model model,@RequestParam("gujang_idx") int gujang_idx,@RequestParam(defaultValue="1") int now_page) {
		PagingBean pagingBean = new PagingBean();
		int listCnt = db.selectOne("notice.get_gujang_notice_cnt",gujang_idx);
		GujangBean bean = db.selectOne("gujang.get_all_gujang",gujang_idx);
		model.addAttribute("gujang_bean",bean);
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
		map.put("gujang_idx", String.valueOf(gujang_idx));
		map.put("min", min);
		map.put("max", max);
		
		List<GujangNoticeBean> list =db.selectList("notice.get_gujang_notice",map);
		model.addAttribute("gujang_notice_list",list);
		model.addAttribute("page_bean",pagingBean);
		return "ajax/gujang_notice_ajax";
	}
	
	
	
	@RequestMapping(value="read_notice.spring", method=RequestMethod.GET)
	public String read_notice_spring(@RequestParam("gujang_notice_idx") int gujang_notice_idx,Model model){
		GujangNoticeBean bean = db.selectOne("notice.get_notice_detail",gujang_notice_idx);
		model.addAttribute("gujang_notice_bean",bean);
		
		return "client/read_notice";
	}
	
	
	
}
