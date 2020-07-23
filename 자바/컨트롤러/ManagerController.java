package com.stuHallReservation.main;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;

import com.stuHallReservation.beans.*;


@Controller
public class ManagerController {
	@Autowired
	private SqlSessionTemplate db;
	
		
		
	@RequestMapping(value="add_gujang.spring", method=RequestMethod.GET)
	public String add_gujang_spring(){
		
		
		
		return "manager/add_gujang";
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	}
	@RequestMapping(value = "chktime_pro.spring", method = RequestMethod.POST)
	public String chktime_pro(YeahyackDayBean bean,Model model) {

		YeahyackDayBean yeahyack = db.selectOne("yeahyack.get_yeahyack_day",bean);
		model.addAttribute("yeahyack",yeahyack);
		
		return "ajax/chktime";
	}
	@RequestMapping(value = "yeahyacktime.spring", method = RequestMethod.POST)
	public String yeahyacktime(YeahyackDayBean bean,Model model) {

		YeahyackDayBean yeahyack = db.selectOne("yeahyack.get_yeahyack_day",bean);
		model.addAttribute("yeahyack",yeahyack);
		
		return "ajax/yeahyacktime";
	}
	@RequestMapping(value="yeahyacktime_pro.spring", method=RequestMethod.POST)
	public String yeahyacktime_pro(Model model,String[] picktime,YeahyackDayBean bean) {
		////아작스로 시간값을 전송해 예약 시간을 변경시킨다
		int aaaa = bean.getYeahyack_day_gujang_idx();
		String gujang_idx = String.valueOf(aaaa);
		for(String pick : picktime) {
			HashMap<String,String> map = new HashMap<String,String>();
			map.put("pick",pick);
			map.put("yeahyack_day_gujang_idx", gujang_idx);
			map.put("yeahyack_day", bean.getYeahyack_day());
			db.update("yeahyack.set_return_yeahyack",map);
		}
		
		model.addAttribute("msg","OK");
		return "common/msg";
	}
	@RequestMapping(value="check_time_ajax_pro.spring", method=RequestMethod.POST)
	public String check_time_ajax_pro(Model model,String[] picktime,YeahyackDayBean bean) {
		////아작스로 시간값을 전송해 예약 시간을 변경시킨다
		int aaaa = bean.getYeahyack_day_gujang_idx();
		String gujang_idx = String.valueOf(aaaa);
		for(String pick : picktime) {
			HashMap<String,String> map = new HashMap<String,String>();
			map.put("pick",pick);
			map.put("yeahyack_day_gujang_idx", gujang_idx);
			map.put("yeahyack_day", bean.getYeahyack_day());
			db.update("yeahyack.set_disabled_yeahyack",map);
		}
		
		model.addAttribute("msg","OK");
		return "common/msg";
	}
	@RequestMapping(value="check_time_ajax_pro1.spring", method=RequestMethod.POST)
	public String check_time_ajax_pro1(Model model,String[] picktime,String[] pick_time,YeahyackDayBean bean) {
		//아작스로 시간값을 전송해 이용가능시간으로 변경한다
		// 
		int aaaa = bean.getYeahyack_day_gujang_idx();
		String gujang_idx = String.valueOf(aaaa);
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
			map.put("pick",pick);
			map.put("yeahyack_day_gujang_idx", gujang_idx);
			map.put("yeahyack_day", bean.getYeahyack_day());
			db.update("yeahyack.set_abled_yeahyack",map);
		}
		
		HashMap<String,String> map2 = new HashMap<String, String>();
		map2.put("yeahyack_day_idx", String.valueOf(bean.getYeahyack_day_idx()));
		map2.put("pick", p2);
		db.update("change_yeahyack_status",map2);
		model.addAttribute("msg","OK");
		return "common/msg";
	}
	@RequestMapping(value="check_time_gujang.spring", method=RequestMethod.GET)
	public String check_time_gujang_spring(){
		
	
		return "manager/check_time_gujang";
	}
	@RequestMapping(value="yeahyak_gujang.spring", method=RequestMethod.GET)
	public String yeahyak_gujang_spring(){

		return "manager/yeahyak_gujang";
	}
	
	@RequestMapping(value="write_notice_pro.spring", method=RequestMethod.POST)
	public String write_notice_pro(Model model, HttpSession session, GujangNoticeBean gujang_notice_bean,HttpServletRequest request){

		UserBean user_bean = db.selectOne("get_user_info",(UserBean)session.getAttribute("login_bean"));
		String gujang_notice_IP = request.getRemoteAddr();
		gujang_notice_bean.setGujang_notice_user_idx(user_bean.getUser_idx());
		gujang_notice_bean.setGujang_notice_IP(gujang_notice_IP);
		
			db.insert("notice.add_notice",gujang_notice_bean);
		
		
		model.addAttribute("msg","OK");
		
		return "common/msg";
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	}
	
	@RequestMapping(value="write_notice.spring", method=RequestMethod.GET)
	public String write_notice_spring(Model model, int gujang_idx){
		
		GujangBean gujang_bean = db.selectOne("gujang.get_all_gujang",gujang_idx);
		model.addAttribute("gujang_bean",gujang_bean);
		
		return "manager/write_notice";
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	}
	@RequestMapping(value="modify_notice.spring", method=RequestMethod.GET)
	public String modify_notice_spring(Model model,@RequestParam("gujang_notice_idx")int gujang_notice_idx){
		GujangNoticeBean notice_bean = db.selectOne("notice.get_notice_detail",gujang_notice_idx);
		model.addAttribute("gujang_notice_bean",notice_bean);
		
		return "manager/modify_notice";
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////		
	}
	@RequestMapping(value="modify_notice_pro.spring", method=RequestMethod.POST)
	public String modify_notice_pro_spring(Model model,GujangNoticeBean bean){
		db.update("modify_notice",bean);
		model.addAttribute("msg","OK");
		
		return "common/msg";
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////		
	}
	@RequestMapping(value="delete_notice_pro.spring", method=RequestMethod.POST)
	public String delete_notice_pro_spring(Model model,GujangNoticeBean bean){
		db.delete("notice.remove_notice",bean);
		model.addAttribute("msg","OK");
		
		return "common/msg";
	}
	@RequestMapping(value="manager_main.spring", method=RequestMethod.GET)
	public String manager_gujang_spring( Model model,HttpSession session,@RequestParam(defaultValue="1") int now_page){
		PagingBean pagingBean = new PagingBean();

		UserBean user_idx_p = (UserBean)session.getAttribute("login_bean");
		
		int user_idx = user_idx_p.getUser_idx();
	
		int listCnt = db.selectOne("gujang.get_manager_gujang_cnt",user_idx);
	
		
		
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
		map.put("user_idx", String.valueOf(user_idx));
		map.put("min", min);
		map.put("max", max);
		
		List<GujangBean> list = db.selectList("gujang.get_manager_gujang",map);
	
		model.addAttribute("gujang_list",list);
		model.addAttribute("page_bean",pagingBean);
		return "manager/manager_gujang";
/////////////////////////////////////////////////////////////////////////
	}
	@RequestMapping(value="modify_gujang.spring", method=RequestMethod.GET)
	public String modify_gujang_spring(@RequestParam("gujang_idx") int gujang_idx, Model model){
		
		GujangBean gujang_bean = db.selectOne("gujang.get_all_gujang",gujang_idx);
		
			model.addAttribute("gujang_bean",gujang_bean);
		
		
		return "manager/modify_gujang";
/////////////////////////////////////////////////////////////////////////////////
	}
	@RequestMapping(value="alert_page.spring", method=RequestMethod.GET)
	public String alert_page_spring(){
		
		return "manager/alert_page";
	}
/////////////////////////////////////////////////////////////////////
	
	@RequestMapping(value="closed_routine.spring", method=RequestMethod.GET)
	public String closed_routine_spring(){
		
		return "manager/closed_routine";
	}	
	
	@RequestMapping(value = "requestupload2.spring", method=RequestMethod.POST)
    //public String requestupload2(MultipartHttpServletRequest mtfRequest,GujangBean gujang_bean,Model model, HttpSession session) {
	 public String requestupload2(MultipartHttpServletRequest mtfRequest,GujangBean gujang_bean,Model model) {
		
        List<MultipartFile> fileList = mtfRequest.getFiles("gujang_img_data");
        
        //String path = "C:\\Users\\jica\\Desktop\\spring\\SpringYang_sports_reservation\\src\\main\\webapp\\resources\\upload\\";
        String path2 = mtfRequest.getSession().getServletContext().getRealPath("/resources/upload/");
        if(fileList.size() != 0) {
        	for (MultipartFile mf : fileList) {
                String originFileName = mf.getOriginalFilename(); // 원본 파일 명
                String safeFile = path2 + originFileName;
                
                try {
                		
                	gujang_bean.setGujang_img(originFileName);
                    mf.transferTo(new File(safeFile));
                } catch (IllegalStateException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
               
            }
        }else {
        	gujang_bean.setGujang_img("default.jpg");
        }
       
        	db.insert("gujang.add_gujang",gujang_bean);
        
        
        model.addAttribute("msg","OK");
        
		return "common/msg";
///////////////////////////////////////////////////////////////////////////////////
    }
	@RequestMapping(value = "modify_requestupload2.spring", method=RequestMethod.POST)
    //public String requestupload2(MultipartHttpServletRequest mtfRequest,GujangBean gujang_bean,Model model, HttpSession session) {
	 public String modify_requestupload2(MultipartHttpServletRequest mtfRequest,GujangBean gujang_bean,Model model) {
		
        List<MultipartFile> fileList = mtfRequest.getFiles("gujang_img_data");
        
        //String path = "C:\\Users\\jica\\Desktop\\spring\\SpringYang_sports_reservation\\src\\main\\webapp\\resources\\upload\\";
        String path2 = mtfRequest.getSession().getServletContext().getRealPath("/resources/upload/");
        for (MultipartFile mf : fileList) {
            String originFileName = mf.getOriginalFilename(); // 원본 파일 명
            String safeFile = path2 + originFileName;

            try {
            	gujang_bean.setGujang_img(originFileName);
                mf.transferTo(new File(safeFile));
            } catch (IllegalStateException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
       
        db.update("gujang.modify_gujang",gujang_bean);
        model.addAttribute("msg","OK");
        
		return "common/msg";
///////////////////////////////////////////////////////////////////////////////////
    }
	@RequestMapping(value="delete_gujang.spring", method=RequestMethod.POST)
	public String delete_gujang_spring(Model model,GujangBean bean){
		 
		 db.delete("gujang.delete_gujang",bean);
	     model.addAttribute("msg","OK");
		return "common/msg";
///////////////////////////////////////////////////////////////////////////////////
	}	
	
}
