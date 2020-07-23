package com.stuHallReservation.beans;

public class PagingBean {
	private int now_page;
	//전체 글 의 개수
	private int allcontent_cnt;
	//전체 페이지의 개수
	private int allpage_cnt;
	//페이지네이션 최소값
	private int pagination_min;
	//페이지네이션 최대값
	private int pagination_max;
	//페이지네이션 개수
	private int pagination_cnt;
	//페이지당 글의 개수
	private int cnt_per_page;
	public int getNow_page() {
		return now_page;
	}
	public void setNow_page(int now_page) {
		this.now_page = now_page;
	}
	public int getAllcontent_cnt() {
		return allcontent_cnt;
	}
	public void setAllcontent_cnt(int allcontent_cnt) {
		this.allcontent_cnt = allcontent_cnt;
	}
	public int getAllpage_cnt() {
		return allpage_cnt;
	}
	public void setAllpage_cnt(int allpage_cnt) {
		this.allpage_cnt = allpage_cnt;
	}
	public int getPagination_min() {
		return pagination_min;
	}
	public void setPagination_min(int pagination_min) {
		this.pagination_min = pagination_min;
	}
	public int getPagination_max() {
		return pagination_max;
	}
	public void setPagination_max(int pagination_max) {
		this.pagination_max = pagination_max;
	}
	public int getPagination_cnt() {
		return pagination_cnt;
	}
	public void setPagination_cnt(int pagination_cnt) {
		this.pagination_cnt = pagination_cnt;
	}
	public int getCnt_per_page() {
		return cnt_per_page;
	}
	public void setCnt_per_page(int cnt_per_page) {
		this.cnt_per_page = cnt_per_page;
	}
	
	
	
	
	
}
