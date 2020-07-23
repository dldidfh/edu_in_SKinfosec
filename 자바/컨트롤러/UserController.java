package com.stuHallReservation.main;


import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;


import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Repository;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.stuHallReservation.beans.*;


@Repository
@Controller
public class UserController {
	
	@Autowired
	private SqlSessionTemplate db;
	@RequestMapping(value="join.spring", method=RequestMethod.GET)
	public String join_spring(){
		
		return "user/join";
	}
	@RequestMapping(value="login.spring", method=RequestMethod.GET)
	public String login_spring(){
		
		return "user/login";
	}
	@RequestMapping(value="logout.spring", method=RequestMethod.GET)
	public String logout_spring(){
		
		return "user/logout";
	}
	@RequestMapping(value="my_info.spring", method=RequestMethod.GET)
	public String my_info_spring( Model model,HttpSession session){
		UserBean user_bean = db.selectOne("get_user_info",(UserBean)session.getAttribute("login_bean"));
		model.addAttribute("user_bean",user_bean);
		
		return "user/my_info";
	}
	@RequestMapping(value = "login_pro.spring", method = RequestMethod.POST )
	public String login_pro(UserBean user_bean, Model model, HttpSession session) {
		int chk = db.selectOne("user.get_login", user_bean);
		if(chk == 1 ) {
			model.addAttribute("msg",chk);
			UserBean login_bean =  db.selectOne("user.get_session_user", user_bean.getUser_id());
			login_bean.setLogin(true);
			session.setAttribute("login_bean", login_bean);
			session.setAttribute("user_status", login_bean.getUser_status());
			
		}
		
		return "common/msg";
	}
	@RequestMapping(value = "join_pro.spring", method = RequestMethod.POST)
	public String join_pro(UserBean user_bean, Model model,HttpServletRequest request) {
		String user_join_ip = request.getRemoteAddr();
		user_bean.setUser_join_ip(user_join_ip);
		db.insert("user.user_join", user_bean);
		
		model.addAttribute("msg","OK");
	
		return "common/msg";
	}
	@RequestMapping(value = "check_user_id.spring",  method = RequestMethod.POST)
	public String check_user_id(UserBean user_bean, Model model) {
		int chk = db.selectOne("user.chk_user_id", user_bean.getUser_id());
		if(chk == 1) {
			model.addAttribute("msg",chk);
		}
		
		return "common/msg";
	}
	@RequestMapping(value="update_user_info.spring", method=RequestMethod.POST)
	public String update_user_info(UserBean user_bean,Model model){
		db.update("user.modify_user_info",user_bean);
		model.addAttribute("msg","OK");
		return "common/msg";
	}
	
}
