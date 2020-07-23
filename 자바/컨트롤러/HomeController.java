package com.stuHallReservation.main;


import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * Handles requests for the application home page.
 */
@Controller
public class HomeController {
	
	//private static final Logger logger = LoggerFactory.getLogger(HomeController.class);
	
	/**
	 * Simply selects the home view to render by returning its name.
	 */
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String home() {
		return "redirect:homepage.spring";
	}
	@RequestMapping(value = "homepage.spring", method = RequestMethod.GET)
	public String homepage() {
		return "main/homepage";
	}
	
	@RequestMapping(value = "login_please.spring")
	public String login_please(Model model) {
		System.out.println("Login_please");
		model.addAttribute("msg", "로그인 후 이용해 주시기 바랍니다.");
		return "common/login";
	}
	
	@RequestMapping(value = "wait_please.spring")
	public String wait_please() {
		
		return "client/wait_please";
	}
}
