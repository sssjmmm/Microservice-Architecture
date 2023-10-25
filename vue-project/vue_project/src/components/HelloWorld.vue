<template>
	<div class="background">
		<el-row :gutter="20">
			<el-col :span="8">
				<div class="header-left-text">Microservice architecture Personal project</div>
			</el-col>
			<el-col :span="8">
				<el-input
				v-model="keyword"
				placeholder="please input city name"
				class="input-city"
				@keyup.enter="searchCity"
				>
				<template #append>
					<el-button @click="searchCity" type="large" class="cool-button">Search</el-button>
				</template>
				</el-input>
				<!-- <el-icon><Search /></el-icon> -->
			</el-col>
			<el-col :span="8">
				<div class="header-left-text">
					<div style="font-size: 30px;">Tongji University SSE</div>
					<div style="font-size: 30px;">2151299 SUJIAMING</div>
				</div>
			</el-col>
		</el-row>
		<!-- 第一行 -->
		<!-- 列之间将有20个单位的间距 -->
		<el-row :gutter="20">
			<!-- 每一行24个sapn -->
			<el-col :span="8">
				<el-card shadow="hover" class="color03" style="height: 524px" >
					<template #header>
						<div class="api-title">
						<span>Baidu Map</span>
						</div>
					</template>
					<!-- 
						scroll-wheel-zoom是是否可以缩放
						@ready是图加载完后触发事件
						center是位置定位
						zoom是缩放大小限制
						inertial-dragging是允许惯性拖拽
					-->
					
					<baidu-map
						class="bm-view"
						:zoom="15"
						:center=city
						inertial-dragging
						@ready="mapReady"
						:scroll-wheel-zoom="true"
					>
						<!-- 定位控件   anchor="BMAP_ANCHOR_BOTTOM_RIGHT"代表放在右下角 -->
						<!-- <bm-geolocation
						anchor="BMAP_ANCHOR_BOTTOM_RIGHT"
						:showAddressBar="true"
						:autoLocation="true"
						></bm-geolocation> -->

						<!-- 地区检索  keyword：关键字搜索   @searchcomplete：检索完成后的回调函数   auto-viewport：检索结束后是否自动调整地图事业  -->
						<!-- <bm-local-search
						:keyword="keyword"
						@searchcomplete="search"
						:auto-viewport="true"
						class="search"
						></bm-local-search> -->

						<!-- 缩放控件   anchor代表控件停靠位置   anchor="BMAP_ANCHOR_TOP_RIGHT"代表放在右上角-->
						<bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
					</baidu-map>
				</el-card>

			</el-col>
			<el-col :span="16">
				<el-row :gutter="20" class="mgb20">
					<el-col :span="8">
						<el-card shadow="hover" class="color01" :body-style="{ padding: '0px' }">
							<div class="grid-content">
								<el-icon class="grid-con-icon">
									<Bicycle />
								</el-icon>
								<div class="grid-cont-right">
									<div>Cultural & Tourism</div>
								</div>
							</div>
						</el-card>
					</el-col>
					<el-col :span="8">
						<el-card shadow="hover" class="color03" :body-style="{ padding: '0px' }">
							<div class="grid-content">
								<el-icon class="grid-con-icon">
									<LocationInformation />
								</el-icon>
								<div class="grid-cont-right">
									<!-- <div class="grid-num">{{AllPostCount}}</div> -->
									<div>Geographic Information</div>
								</div>
							</div>
						</el-card>
					</el-col>
					<el-col :span="8">
						<el-card shadow="hover" class="color02" :body-style="{ padding: '0px' }">
							<div class="grid-content">
								<el-icon class="grid-con-icon">
									<User />
								</el-icon>
								<div class="grid-cont-right">
									<!-- <div class="grid-num">{{AllUserCount}}</div> -->
									<div>Life Guide</div>
								</div>
							</div>
						</el-card>
					</el-col>
				</el-row>

				<!-- 天气预报 -->
				<el-card shadow="hover" class="color02" style="height: 403px;position: relative;">
					<template #header>
						<div class="api-title">
							<span>WeatherForecast</span>
						</div>
					</template>
					<el-scrollbar style="height: 285px;">
						<el-table :data="weather_forecast" height=260 style="width: 100%">
							<el-table-column prop="date" label="Date" width="110" />
							<el-table-column prop="week" label="Week" width="100" />
							<el-table-column prop="weather" label="Weather" width="100" />
							<el-table-column prop="real" label="Real" width="100" />
							<el-table-column prop="lowest" label="Lowest" width="100" />
							<el-table-column prop="highest" label="Highest" width="100" />
							<el-table-column prop="wind" label="Wind" width="100" />
							<el-table-column prop="windspeed" label="Windspeed" width="100" />
							<el-table-column prop="windsc" label="Windsc" width="100" />
							<el-table-column prop="sunrise" label="Sunrise" width="100" />
							<el-table-column prop="sunset" label="Sunset" width="100" />
							<el-table-column prop="moonrise" label="Moonrise" width="100" />
							<el-table-column prop="moondown" label="Moondown" width="100" />
							<el-table-column prop="vis" label="Vis" width="50" />
							<el-table-column prop="humidity" label="Humidity" width="100" />
							<el-table-column prop="tips" label="Tips" width="550" />
						</el-table>
					</el-scrollbar>
				</el-card>
			</el-col>
		</el-row>

		<!-- 第二行 -->
		<el-row :gutter="20">
			<el-col :span="12">
				<el-card shadow="hover" style="height: 440px" class="color03">
					<template #header>
						<div class="api-title">
							<span>Province&Area</span>
						</div>
					</template>
					<div class="align-left mb-10 cool-word">
						<div>Province: {{ province }}</div>
						<div>Codes for the administrative divisions: {{ code }}</div>
					</div>
					<el-scrollbar style="height: 270px;">
						<el-table :data="area" height=255 style="width: 100%">
							<el-table-column prop="name" label="Name" width="254" />
							<el-table-column prop="code" label="Code" width="550" />
						</el-table>
					</el-scrollbar>
				</el-card>
			</el-col>
			<el-col :span="12">
				<el-card shadow="hover" class="color01" style="height: 440px">
					<template #header>
						<div class="api-title">
							<span>TouristAttraction</span>
						</div>
					</template>
					<el-scrollbar style="height: 320px;">
							<el-table :data="tourist_attraction"  height=300 style="width: 100%">
							<el-table-column prop="name" label="Name" width="150" />
							<el-table-column prop="content" label="Content" width="500" />
							<el-table-column prop="province" label="Province" />
						</el-table>
					</el-scrollbar>
				</el-card>
			</el-col>
		</el-row>
		<!-- 第三行 -->

		<el-row :gutter="20">
			<el-col :span="20">
				<el-card shadow="hover" class="color01" style="height: 464px">
					<!-- <schart ref="line" class="schart" canvasId="line" :options="options2"></schart> -->
				<template #header>
					<div class="api-title">
						<span>CulturalTourismNews</span>
					</div>
				</template>
				<el-scrollbar style="height: 334px;">
					<el-table :data="cultural_tourism_news" height=320 style="width: 100%">
						<el-table-column prop="ctime" label="Time" width="150" />
						<el-table-column label="Picture">
							<template #default="scope">
								<el-image style="width: 50px;" :src="scope.row.picUrl"></el-image>
							</template>
						</el-table-column>							<el-table-column prop="title" label="Title" width="550" />
						<el-table-column prop="source" label="Source" />
						<el-table-column prop="url" label="Url" width="500" />
					</el-table>
				</el-scrollbar>
				</el-card>
			</el-col>

			<el-col :span="4">
				<el-card shadow="hover" class="color02" >
					<template #header>
						<div class="api-title">
							<span>OilPrice</span>
						</div>
					</template>
					<!-- <el-button @click="getOilPrice">获取油价</el-button> -->
					<el-dropdown @command="showOilPrice">
					<el-button type="primary" plain class="wiki-button">
						Choose Oil Type<el-icon class="el-icon--right"><arrow-down /></el-icon>
					</el-button>
					<template #dropdown>
						<el-dropdown-menu>
							<el-dropdown-item command="t0">0 # diesel oil price</el-dropdown-item>
							<el-dropdown-item command="t89">89 # gasoline price</el-dropdown-item>
							<el-dropdown-item command="t92">92 # gasoline price</el-dropdown-item>
							<el-dropdown-item command="t95">95 # gasoline price</el-dropdown-item>
							<el-dropdown-item command="t98">98 # gasoline price</el-dropdown-item>
						</el-dropdown-menu>
					</template>
					</el-dropdown>
					<div style="margin-top: 10px;" >
						<el-text class="oil-prize" tag="b">Price：{{ oil_price_key }}￥/liter</el-text>
					</div>
				</el-card>
				<el-card shadow="hover" class="color04" style="margin-top: 20px;">
					<template #header>
						<div class="api-title">
							<div>Wikipedia</div>
							<img v-show="showLogo" style="width: 100px; height: 110px" src="../assets/wiki_log.png" alt="WikiLogo" />
						</div>
					</template>
					<!-- <input class="inputbox" v-model="searchTerm" @keyup.enter="wikiSearch" /> -->
					<!-- <button class="searchbtn" @click="wikiSearch">Search</button> -->
					<el-button @click="visible = true" class="wiki-button">
						Open Wikipedia
					</el-button>
				</el-card>
			</el-col>
		</el-row>
		<!-- 第四行 -->
		<el-row :gutter="20">
			<el-col :span="12">
				<el-card shadow="hover" class="color02">
					<template #header>
						<div class="api-title">
							<span>AirConditon</span>
						</div>
					</template>

					<el-scrollbar style="height: 140px;">
						<el-table :data="air_conditon" style="width: 100%;" height=200 class="">
							<el-table-column prop="so2" label="SO2" width="80" />
							<el-table-column prop="o3" label="O3" width="80" />
							<el-table-column prop="pm2_5" label="PM2.5" width="90" />
							<el-table-column prop="co" label="CO" width="80" />
							<el-table-column prop="num" label="Num" width="80" />
							<el-table-column prop="no2" label="No2" width="80" />
							<el-table-column prop="quality" label="Quality" width="90" />
							<el-table-column prop="aqi" label="Aqi" width="80" />
							<el-table-column prop="pm10" label="PM10" width="80" />
							<el-table-column prop="o3_8h" label="O3" width="80" />
						</el-table>
					</el-scrollbar>
				</el-card>
			</el-col>
			<el-col :span="6">
				<el-card shadow="hover" class="color02" style="height: 250px;">
					<template #header>
						<div class="api-title">
							<span>CityId</span>
						</div>
					</template>
					<div class="cool-text">
						<div>areacode: {{ areacode }} </div>
						<div>path: {{ path }}</div>
					</div>
				</el-card>
			</el-col>
			<el-col :span="6">
				<el-card shadow="hover" class="color05" style="height: 250px;">
					<template #header>
						<div class="api-title">
							<span>OTHER</span>
						</div>
					</template>
					<el-button @click="show_history = true" class="wiki-button">
						Historic Record
					</el-button>
					<div class="cool-text">
						<div>Vue框架</div>
						<div>Axios请求接口</div>
						<div>完成时间：2023/10/20</div>
					</div>
				</el-card>
			</el-col>
		</el-row>


		<el-drawer v-model="visible" :show-close="false">
			<template #header="{ close, titleId, titleClass }">
			<h1 :id="titleId" :class="titleClass">Wikipedia</h1>
			<el-button type="danger" @click="close">
				<el-icon class="el-icon--left"><CircleCloseFilled /></el-icon>
				Close
			</el-button>
			</template>
			<div class="searchbox" :style="searchBoxStyle">
				<div class="searchresult" v-show="showResults">
					<ol>
					<li v-for="result in results" :key="result.pageid" class="result-box">
						<a :href="result.url" class="result-title">{{ result.title }}</a>
						<p v-html="result.content" class="result-content"></p>
					</li>
					</ol>
				</div>
			</div>
		</el-drawer>
		<el-drawer v-model="show_history" :show-close="false">
			<template #header="{ close, titleId, titleClass }">
			<h1 :id="titleId" :class="titleClass">History</h1>
			<el-button type="danger" @click="close">
				<el-icon class="el-icon--left"><CircleCloseFilled /></el-icon>
				Close
			</el-button>
			<el-button type="primary" @click="getHistory">
				<el-icon class="el-icon--left"><el-icon><Refresh /></el-icon></el-icon>
				Refresh
			</el-button>
			</template>
				<el-table :data="record_data" height=720 style="width: 100%; background-color: rgb(14, 60, 34);">
						<el-table-column prop="time" label="Time"/>
						<el-table-column prop="key" label="Key" />
				</el-table>
		</el-drawer>
	</div>
</template>

<!-- 全国各省城市信息 -->
<!-- https://www.mxnzp.com/api/address/list?app_id=nrptqjkmouonxmmn&app_secret=8bh5CMKLpi1pxZLfzKk0DlDTPK2zk1kq -->

<script>

// import {imgurl} from '../assets/img/img.jpg';
import axios from 'axios';
import { ArrowDown } from '@element-plus/icons-vue'
import { Search } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

export default {
    data() {
        return {
			city: '',

			//https://www.tianapi.com 天行数据
			API_KEY: '2cb86b94b38e57177daacee3c2857685',
			//https://www.mxnzp.com ROLL
			app_id: 'nrptqjkmouonxmmn',
			app_secret: '8bh5CMKLpi1pxZLfzKk0DlDTPK2zk1kq',
			//
			key:'7d244947aac4cd0ce96f0737d6bcb55e',

			// 接口1参数
			tourist_attraction: [],
			tourist_attraction_num: 8,
			//接口2参数
			cultural_tourism_news: [],
			cultural_tourism_news_num: 8,
			// cultural_tourism_news_word: '',
			//接口3参数
			weather_forecast: [],
			weather_forecast_type: 7,//7是七天 1是当天
			//接口4参数：百度地图
			//定位位置信息
			center: {},
			//检索关键字
			keyword: "",
			//接口5参数：省份及区信息
			code: '',
			province: '',
			area: [],
			//接口6参数：省份油价
			oil_price: [],
			oil_price_key: '',

			//接口7参数：空气质量
			air_conditon:[],

			//接口8参数：城市id
			areacode: '',
			path: '',

			//接口9参数：Wiki百科
			searchTerm: '',
			results: [],
			showLogo: true,
			showResults: true,

			visible: false,

			//数据库参数
			show_history:false,
			record_data:[],

        };
    },
    components:{
		Search,
		ArrowDown,
    },
    methods: {
		
		async wikiSearch() {
			if (this.searchTerm && this.searchTerm !== 'please input city name') {
				const apiUrl =
				'https://en.wikipedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=0&gsrlimit=10&prop=pageimages|extracts&pilimit=max&exintro&explaintext&exsentences=1&exlimit=max&origin=*&gsrsearch=' +
				this.searchTerm;

				await axios
				.get(apiUrl)
				.then((response) => {
					const pages = response.data.query.pages;
					this.results = Object.keys(pages).map((pageid) => {
					const page = pages[pageid];
					const title = page.title;
					const extract = page.extract;
					const imgsrc = page.thumbnail ? page.thumbnail.source : '';
					const listcontent = imgsrc ? `<img src="${imgsrc}">` + extract : extract;
					const href = 'http://en.wikipedia.org/wiki/' + encodeURIComponent(title);
					return { title, content: listcontent, url: href, pageid };
					});
					this.showResults = true;
					ElMessage({
						showClose: true,
						message: 'WikiSearch: Congrats, request successful.',
						type: 'success',
					})
				})
				.catch((error) => {
					ElMessage({
						showClose: true,
						message: 'WikiSearch: Oops, request failed.',
						type: 'error',
					})
					console.error(error);
				});
			} else {
				this.searchTerm = 'please input city name';
				this.$refs.inputbox.focus();
			}
		},
		async postHistory() {
			// 创建一个新的 Date 对象以获取当前时间
			const date = new Date();

			// 获取小时、分钟和秒

			const year = date.getFullYear();
			const month = date.getMonth() + 1;
			const day = date.getDate();
			const hour = date.getHours();
			const minute = date.getMinutes();
			const second = date.getSeconds();

			// 格式化时间为字符串
			const format_time = `${year}年${month}月${day}日${hour}时${minute}分${second}秒`;
			// Import Axios
			const axios = require('axios');

			// Define the base URL
			const apiUrl = 'http://100.80.67.59/api/mgr/citylog';

			// Construct the payload for adding a customer
			const addCustomerPayload = {
			action: 'add_city',
			data: {
				key: this.city,
				time: format_time,
			},
			};

			// Send a POST request to add a customer
			await axios
			.post(apiUrl, addCustomerPayload)
			.then((response) => {
				console.log(response.data);
			})
			.catch((error) => {
				console.error('Error:', error);
			});
		},		
		async testData2() {
			try {
				await axios.get(`http://localhost:8888/api/mgr/citylog?action=list_city`)
				.then((response) => {
					// 请求成功时的处理
					console.log(response.data.retlist)
				})
				.catch((error) => {
					// 请求失败时的处理
					console.error('Error:', error);
				});
			} catch (error) {
				this.error = error;
			}
		
		},
		async testData3() {
			// 创建一个新的 Date 对象以获取当前时间
			const 当前时间 = new Date();

			// 获取小时、分钟和秒

			const nian = 当前时间.getFullYear()
			const 小时 = 当前时间.getHours();
			const 分钟 = 当前时间.getMinutes();
			const 秒 = 当前时间.getSeconds();

			// 格式化时间为字符串
			const 格式化时间 = `${nian}年${小时}时${分钟}分${秒}秒`;

			// 输出格式化后的时间
			console.log('当前时间：' + 格式化时间);
		
		
		},			
		async getCityAreacode() {
			const axios = require('axios');
			// 设置API请求参数
			const apiUrl = 'https://eolink.o.apispace.com/456456/function/v001/city'; 
			const params = {
			// 请求参数
				location: this.city,
				items: 10,
				area: 'global',
			};
				
			// 配置请求头
			const headers = {
			"X-APISpace-Token":"baf5hkeppcbwg3bmalc97i442zknhs6q",
			"Authorization-Type":"apikey"
			};

			// 创建Axios配置对象
			const axiosConfig = {
			headers: headers, // 设置请求头
			};

			// 发送API请求
			axios.get(apiUrl, { params, ...axiosConfig })
			.then(response => {
				// 处理响应
				this.areacode = response.data.areaList[0].areacode;
				this.path = response.data.areaList[0].path;
				ElMessage({
					showClose: true,
					message: 'CityAreacode: Congrats, request successfully.',
					type: 'success',
				})
			})
			.catch(error => {
				console.error('API请求失败:', error);
				ElMessage({
					showClose: true,
					message: 'CityAreacode: Oops, request failed. Please enter the correct city name.eg.\"上海\",instead of \"上海市\" ',
					type: 'error',
					duration: 5000
				})
			});
		},		
		async getAirConditon() {
			try {
				await axios.get(`https://apis.tianapi.com/aqi/index?key=${this.API_KEY}&area=${this.city}`)
				.then((response) => {
					// 请求成功时的处理
					console.log(response.data.result)
					this.air_conditon.push(response.data.result)
					ElMessage({
						showClose: true,
						message: 'AirConditon: Congrats, request successfully.',
						type: 'success',
					})
				})
				.catch((error) => {
					// 请求失败时的处理
					console.error('Error:', error);
					ElMessage({
						showClose: true,
						message: 'AirConditon: Oops, request failed.',
						type: 'error',
					})
				});
			} catch (error) {
				this.error = error;
				ElMessage({
					showClose: true,
					message: 'AirConditon: Oops, request failed.',
					type: 'error',
				})
			}
		},
		async getOilPrice() {
			try {
				await axios.get(`https://www.mxnzp.com/api/oil/search?province=${this.province}&app_id=${this.app_id}&app_secret=${this.app_secret}`)
				.then((response) => {
					// 请求成功时的处理
					this.oil_price = response.data.data;
					console.log(response.data.data)
					console.log("油价",this.oil_price)
					ElMessage({
						showClose: true,
						message: 'OilPrice: Congrats, request successfully.',
						type: 'success',
					})
				})
				.catch((error) => {
					// 请求失败时的处理
					console.error('Error:', error);
					ElMessage({
						showClose: true,
						message: 'OilPrice: Oops, request failed.',
						type: 'error',
					})
				});
			} catch (error) {
				this.error = error;
				ElMessage({
					showClose: true,
					message: 'OilPrice: Oops, request failed.',
					type: 'error',
				})
			}
		},
		async getProvinceArea() {
			try {
				await axios.get(`https://www.mxnzp.com/api/address/search?type=1&value=${this.city}&app_id=${this.app_id}&app_secret=${this.app_secret}`)
				.then((response) => {
					this.code = response.data.data[0].code;
					this.changeProviceKey(response.data.data[0].name)
					// this.province = response.data.data[0].name;
					this.area = response.data.data[0].pchilds[0].cchilds;
					// 请求成功时的处理
					console.log(response.data.data[0])
					ElMessage({
						showClose: true,
						message: 'ProvinceArea: Congrats, request successfully.',
						type: 'success',
					})
					// 设置一个延迟，例如3秒
					setTimeout(() => {
					this.getOilPrice();
					}, 3000); // 延迟3秒（3000毫秒）
				})
				.catch((error) => {
					// 请求失败时的处理
					console.error('Error:', error);
					ElMessage({
						showClose: true,
						message: 'ProvinceArea: Oops, request failed.',
						type: 'erroe',
					})
				});
			} catch (error) {
				this.error = error;
				ElMessage({
					showClose: true,
					message: 'ProvinceArea: Oops, request failed.',
					type: 'error',
				})
			}
		},
		async getWeatherForecast() {
			try {
				await axios.get(`https://apis.tianapi.com/tianqi/index?key=${this.API_KEY}&city=${this.city}&type=7`)
				.then((response) => {
					this.weather_forecast = response.data.result.list;
					// 请求成功时的处理
					console.log(response.data.result.list)
					ElMessage({
						showClose: true,
						message: 'WeatherForecast: Congrats, request successfully.',
						type: 'success',
					})
				})
				.catch((error) => {
				// 请求失败时的处理
				console.error('Error:', error);
				ElMessage({
					showClose: true,
					message: 'WeatherForecast: Oops, request failed.',
					type: 'error',
				})
				});
			} catch (error) {
				this.error = error;
				ElMessage({
					showClose: true,
					message: 'WeatherForecast: Oops, request failed.',
					type: 'error',
				})
			}
		},
		async getCulturalTourismNews() {
			try {
				await axios.get(`https://apis.tianapi.com/travel/index?key=${this.API_KEY}&num=${this.cultural_tourism_news_num}&word=${this.city}`)
				.then((response) => {
					this.cultural_tourism_news = response.data.result.newslist;
					// 请求成功时的处理
					console.log(response.data.result.newslist)
					ElMessage({
						showClose: true,
						message: 'CulturalTourismNews: Congrats, request successfully.',
						type: 'success',
					})
				})
				.catch((error) => {
					// 请求失败时的处理
					console.error('Error:', error);
					ElMessage({
						showClose: true,
						message: 'CulturalTourismNews: Oops, request failed.',
						type: 'error',
					})
				});
			} catch (error) {
				this.error = error;
				ElMessage({
					showClose: true,
					message: 'CulturalTourismNews: Oops, request failed.',
					type: 'error',
				})
			}
		},
		async getTouristAttraction() {
			try {
				await axios.get(`https://apis.tianapi.com/scenic/index?key=${this.API_KEY}&city=${this.city}&num=${this.tourist_attraction_num}`)
				.then((response) => {
					this.tourist_attraction = response.data.result.list;
					// 请求成功时的处理
					console.log(response.data.result)
					ElMessage({
						showClose: true,
						message: 'TouristAttraction: Congrats, request successfully.',
						type: 'success',
					})
				})
				.catch((error) => {
					// 请求失败时的处理
					console.error('Error:', error);
					ElMessage({
						showClose: true,
						message: 'TouristAttraction: Oops, request failed.',
						type: 'error',
					})
				});
			} catch (error) {
				this.error = error;
				ElMessage({
					showClose: true,
					message: 'TouristAttraction: Oops, request failed.',
					type: 'error',
				})
			}
		},
		async init(){
			await this.getProvinceArea(); //先加载接口5，获取省份
			console.log("调用接口5")
			console.log("调用接口6")
			await this.getCityAreacode(); //先加载接口8，获取areacode
			console.log("调用接口8")
			await this.getTouristAttraction();
			console.log("调用接口1")
			await this.getCulturalTourismNews();
			console.log("调用接口2")
			await this.getWeatherForecast();
			console.log("调用接口3")
			
			await this.getOilPrice();//需要province
			console.log("调用接口6")
			await this.getAirConditon();
			console.log("调用接口7")
			await this.wikiSearch();
			console.log("调用接口9")
			await this.getHistory();
			console.log("调用接口10")

		},
		showOilPrice(command) {
			switch (command){
				case "t0":
					this.oil_price_key = this.oil_price.t0;
					break;
				case "t89":
					this.oil_price_key = this.oil_price.t89;
					break;
				case "t92":
					this.oil_price_key = this.oil_price.t92;
					break;			
				case "t95":
					this.oil_price_key = this.oil_price.t95;
					break;
				case "t98":
					this.oil_price_key = this.oil_price.t98;
					break;
				default:
					break;		
			}
		},
		searchCity(){
			this.city = this.keyword;
			this.searchTerm = this.keyword;
			console.log(this.city);
			this.init();
			this.postHistory();
		},
		changeProviceKey(old_province){
			//目标格式：
			//安徽、北京、重庆、福建、甘肃、广东、广西、贵州、海南、
			//河北、黑龙江、河南、湖北、湖南、江苏、江西、吉林、辽宁、
			//内蒙古、宁夏、青海、陕西、上海、山东、山西、四川、天津、西藏、新疆、云南、浙江
			
			//需要转化的省份：
			//广西壮族自治区 内蒙古自治区 黑龙江省 宁夏回族自治区 西藏自治区 新疆维吾尔自治区
			if(old_province == '内蒙古自治区' || old_province == '黑龙江省'){
				this.province = old_province.substr(0,3);
			}
			else{
				this.province = old_province.substr(0,2);
			}

		},
		async getHistory(){
			try {
				await axios.get(`http://100.80.67.59/api/mgr/citylog?action=list_city`)
				.then((response) => {
					// 请求成功时的处理
					this.record_data = response.data.retlist;
					console.log(response.data.retlist)
				})
				.catch((error) => {
					// 请求失败时的处理
					console.error('Error:', error);
				});
			} catch (error) {
				this.error = error;
			}
		}


    },
    computed: {
		searchBoxStyle() {
			return {
				marginTop: this.showResults ? '5px' : '300px',
			};
		},
    },
    created() {
		// this.init();
    },
};
</script>
<style scoped>


/* 表格单元格样式 */
  /* 表格部分样式
   最外层透明 */
::v-deep .el-table,
::v-deep .el-table__expanded-cell {
  background-color: transparent;
  color: #e5e8ea;
  font-size: 20px;
}
 
/* 表格内背景颜色  */
::v-deep .el-table th,
::v-deep .el-table tr,
::v-deep .el-table td {
  background-color: transparent;
  border: 0px;
  color: #93dcfe;
  /* color: #4a7589; */
  font-size: 14px;
  height: 5px;
  font-family: Source Han Sans CN Normal, Source Han Sans CN Normal-Normal;
  font-weight: Normal;
   /* 创建文本描边，设置描边宽度和颜色 */
  text-shadow: 1px 1px 2px rgba(62, 53, 53, 0.5); 
} 
/* 去掉最下面的那一条线  */
.el-table::before {
  height: 0px;
}
 
/* 设置表格行高度 */
::v-deep .el-table__body tr,
::v-deep .el-table__body td {
  padding: 0;
  height: 30px;
}
 
/* 修改高亮当前行颜色 */
::v-deep .el-table tbody tr:hover > td {
  background: #063570 !important;
}
 
/* 取消当前行高亮 */
::v-deep .el-table tbody tr {
    pointer-events: none;
}
 
/* 修改表头样式-加边框 */
::v-deep .el-table__header-wrapper {
  	border: solid 1px #04c2ed;
    box-sizing: border-box;
}
 
/* 表格斑马自定义颜色 */
::v-deep .el-table__row.warning-row {
  background: #063570;
}
 
/* 滚动条样式 */
::v-deep .el-table__body-wrapper::-webkit-scrollbar-track {
  background-color: #063570;
}
 
::v-deep .el-table__body-wrapper::-webkit-scrollbar {
  width: 10px;
  opacity: 0.5;
}
 
::v-deep .el-table__body-wrapper::-webkit-scrollbar-thumb {
  border-radius: 15px;
  background-color: #0257aa;
}

.cool-button {
  display: inline-block;
  padding: 10px 20px;
  border: none;
  background: linear-gradient(45deg, #ff6b6b, #607d8b);
  color: #0f0e0e;
  font-size: 24px;
  border-radius: 5px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: 0.5s;
}
.wiki-button {
  display: inline-block;

  border: none;
  background: linear-gradient(45deg, #ff6b6b, #607d8b);
  color: #0f0e0e;
  font-size: 18px;
  border-radius: 5px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: 0.5s;
}

.cool-button::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transition: 0.5s;
}

.cool-button:hover::before {
  width: 120px;
  height: 120px;
  transition: 0.5s;
}

.cool-button:hover {
  background: linear-gradient(45deg, #ff6b6b, #56ab2f);
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
}
.input-city {
  /* 输入框的样式 */
  margin-top: 20px;
  border: 2px solid rgba(220, 211, 140, 0.7); /* 边框颜色 */
  border-radius: 5px; /* 边框圆角 */
  background-color: rgba(220, 211, 140, 0.7); /* 背景颜色 */
  color: #000000; /* 文字颜色 */
  font-size: 24px; /* 字体大小 */
  /* 内边距 */
  transition: border 0.3s, box-shadow 0.3s; /* 过渡效果 */
}

.input-city:focus {
  /* 输入框在获得焦点时的样式 */
  border-color: #56ab2f; /* 改变边框颜色 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* 添加阴影效果 */
}
.background {
 	width: 100%; /* 设置元素宽度 */
	height: 100%; /* 设置元素高度 */
	background-image: url('../assets/background.jpg');
 	background-size: cover; /* 设置背景图片的尺寸适应元素 */
 	/* 其他样式属性 */


}
.cool-text {
  font-size: 30px;
  font-weight: bold;
  color: rgba(232, 239, 240, 0.7); /* 设置文字颜色 */
  -webkit-text-stroke: 1px #ce1ce9; /* 创建文本描边，设置描边宽度和颜色 */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); /* 添加文本阴影 */
}

.oil-prize{
	font-size: 25px;
	font-weight: bold;
	color: rgba(232, 239, 240, 0.7); /* 设置文字颜色 */
	-webkit-text-stroke: 0.5px #ad1cc4; /* 创建文本描边，设置描边宽度和颜色 */
	text-shadow: 0.5px 0.5px 1px rgba(0, 0, 0, 0.5); /* 添加文本阴影 */
}
.cool-word {
  font-size: 15px;
  font-weight: bold;
  color: rgba(237, 241, 241, 0.7); /* 设置文字颜色 */
  /* -webkit-text-stroke: 1px #ce1ce9; 创建文本描边，设置描边宽度和颜色 */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5); /* 添加文本阴影 */
}
.header-left-text {
  font-size: 32px;
  font-weight: bold;
  color: rgba(255, 255, 255, 0.8); /* 设置文字颜色 */
  -webkit-text-stroke: 1px #1cace9; /* 创建文本描边，设置描边宽度和颜色 */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 添加文本阴影 */
}
.mb-10{
	margin-bottom: 10px ;
}
.align-left{
	text-align: left;
}
.api-title{
	font-family: "Helvetica Neue", Arial, sans-serif; /* 设置字体 */
	font-size: 20px; /* 设置字体大小 */
	font-weight: bold; /* 设置字体粗细 */
	color: #333; /* 设置标题颜色 */
	text-transform: uppercase; /* 将标题文本转换为大写 */
	letter-spacing: 2px; /* 设置字符间距 */
	text-align: center; /* 设置文本居中对齐 */
	text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* 添加文本阴影 */
	margin-bottom: 10px; /* 设置标题下边距 */
}
.searchbox {
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
}

/* 搜索结果的样式 */
.searchresult {
	text-align: left;
  	margin-top: 10px;
}

/* 搜索结果列表项的样式 */
.result-title {
  font-weight: bold;
  color: #007bff;
  text-decoration: underline;
}

.result-title:hover {
	color: #03468d;	
	text-decoration: underline;
}
.result-box{
	border-bottom: 1px solid #000;
	margin-bottom: 20px;
}
.result-content {
  margin-top: 5px;
}


.search-button {

  background-color: #0d6dcd; /* 自定义按钮背景颜色 */
  border: none; /* 移除按钮边框 */
  border-radius: 4px; /* 圆角按钮 */
  color: #fff; /* 文本颜色 */
  font-size: 16px; /* 自定义字体大小 */
}

.search-button:hover {
  background-color: #66b1ff; /* 鼠标悬停时的背景颜色 */
}
.color01 {
	background-color: rgba(136, 224, 199, 0.6);
}
.color02 {
	background-color: rgba(236, 161, 234, 0.6);
}
.color03 {
	background-color: rgba(139, 174, 208, 0.6);
}
.color04 {
	background-color: rgba(220, 198, 151, 0.6);
}
.color05{
	background-color: rgba(158, 220, 151, 0.6);
}

.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}
.bm-view {
  width: 100%;
  height: 420px;
}
.el-row {
	margin-bottom: 20px;
}

.grid-content {
	display: flex;
	align-items: center;
	height: 100px;
}

.grid-cont-right {
	flex: 1;
	text-align: center;
	font-size: 40px;
	font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
	font-weight: bold;
	color: rgba(232, 239, 240, 0.9); /* 设置文字颜色 */
	-webkit-text-stroke: 1px #490b52; /* 创建文本描边，设置描边宽度和颜色 */
	text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7); /* 添加文本阴影 */
}

.grid-num {
	font-size: 30px;
	font-weight: bold;
}

.grid-con-icon {
	font-size: 50px;
	width: 100px;
	height: 100px;
	text-align: center;
	line-height: 100px;
	color: #fff;
}





.user-info {
	display: flex;
	align-items: center;
	padding-bottom: 20px;
	border-bottom: 2px solid #ccc;
	margin-bottom: 20px;
}

.user-info-cont {
	padding-left: 50px;
	flex: 1;
	font-size: 14px;
	color: #999;
}

.user-info-cont div:first-child {
	font-size: 30px;
	color: #222;
}

.user-info-list {
	font-size: 14px;
	color: #999;
	line-height: 25px;
}

.user-info-list span {
	margin-left: 70px;
}

.mgb20 {
	margin-bottom: 20px;
}

.todo-item {
	font-size: 14px;
}

.todo-item-del {
	text-decoration: line-through;
	color: #999;
}

.schart {
	width: 100%;
	height: 300px;
}

.pagination-container {
	position: absolute;
	bottom: 0;
	left: 0;
	width: 100%;

}

.category-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}

.category-name {
  font-size: 18px;
  color: #333;
}

.category-num {
  font-size: 20px;
  color: #42b983; /* 你可以自定义颜色 */
}
</style>
