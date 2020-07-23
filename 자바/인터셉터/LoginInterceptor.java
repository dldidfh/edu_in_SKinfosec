package com.stuHallReservation.interceptor;



import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

public class LoginInterceptor extends HandlerInterceptorAdapter{
	
	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler)
			throws Exception {
		// TODO Auto-generated method stub
		super.preHandle(request, response, handler);
		
		try {
			if(request.getSession().getAttribute("login_bean") == null) {
				
				//response.sendRedirect(request.getContextPath() + "/지정한다");
				response.sendRedirect("login_please.spring");
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
	public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception{
		super.postHandle(request, response, handler, modelAndView);
	}
}
