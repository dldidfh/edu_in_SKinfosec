package com.stuHallReservation.interceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

public class UserInterceptor extends HandlerInterceptorAdapter{


	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		// TODO Auto-generated method stub
		super.preHandle(request, response, handler);
		
		try {
			if((Integer)request.getSession().getAttribute("user_status") == 3) {
				
				response.sendRedirect("wait_please.spring");
				return false;
			}else {
				return true;
			}
		}catch(Exception e) {
			e.printStackTrace();
			return false;
		}
	}

	@Override
	public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler,
			ModelAndView modelAndView) throws Exception {
		// TODO Auto-generated method stub
		super.postHandle(request, response, handler, modelAndView);
	}
	
}
