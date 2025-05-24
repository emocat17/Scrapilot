<template>
	<div class="panel">
		<panel-title :title="$lang.objects.accounts">
			<!--新增按钮实现-->
			<router-link :to="{ name: 'accountCreate' }" tag="span">
				<el-button size="mini" type="success">
					<i class="fa fa-plus"></i>
					{{ $lang.buttons.create }}
				</el-button>
			</router-link>
		</panel-title>
		<div class="panel-body">
			<!--遍历accounts-->
			<el-table
				v-loading="loading"
				:data="accounts"
				:element-loading-text="$lang.messages.loading"
				:empty-text="$lang.messages.noData"
				:style="{ width: '100%;' }"
			>
				<!--各字段呈现实现-->
				<el-table-column
					:label="$lang.columns.username"
					align="center"
					prop="username"
					min-width="30%"
				>
				</el-table-column>
				<el-table-column
					:label="$lang.columns.email"
					align="center"
					prop="email"
					min-width="30%"
				>
				</el-table-column>
				<el-table-column :label="$lang.columns.is_superuser" align="center" min-width="30%">
					<template slot-scope="props">
						<span v-if="props.row.is_superuser">
							<el-button icon="el-icon-check" round size="mini" type="primary"></el-button>
						</span>
						<span v-else>
							<el-button icon="el-icon-close" round size="mini" type="primary"></el-button>
						</span>
					</template>
				</el-table-column>
				<el-table-column :label="$lang.columns.is_staff" align="center" min-width="30%">
					<template slot-scope="props">
						<span v-if="props.row.is_staff">
							<el-button icon="el-icon-check" round size="mini" type="primary"></el-button>
						</span>
						<span v-else>
							<el-button icon="el-icon-close" round size="mini" type="primary"></el-button>
						</span>
					</template>
				</el-table-column>
				<el-table-column :label="$lang.columns.is_active" align="center" min-width="30%">
					<template slot-scope="props">
						<span v-if="props.row.is_active">
							<el-button icon="el-icon-check" round size="mini" type="primary"></el-button>
						</span>
						<span v-else>
							<el-button icon="el-icon-close" round size="mini" type="primary"></el-button>
						</span>
					</template>
				</el-table-column>
				<el-table-column
					:label="$lang.columns.date_joined"
					align="center"
					prop="date_joined"
					min-width="30%"
				>
				</el-table-column>
				<el-table-column
					:label="$lang.columns.last_login"
					align="center"
					prop="last_login"
					min-width="30%"
				>
				</el-table-column>
				<!--isSupperUserLogin标识超级管理员身份-->
				<el-table-column v-if="isSupperUserLogin" :label="$lang.columns.operations" align="center" min-width="50%">
					<template slot-scope="props">
						<router-link :to="{ name: 'accountEdit', params: { id: props.row.id } }" tag="span">
							<!--指定列跳转编辑页-->
							<el-button size="mini" type="info">
								<i class="fa fa-edit"></i>
								{{ $lang.buttons.edit }}
							</el-button>
						</router-link>
						<!--指定列删除-->
						<el-button size="mini" type="danger" @click="onSingleDelete(props.row.id)">
							<i class="fa fa-remove"></i>
							{{ $lang.buttons.delete }}
						</el-button>
					</template>
				</el-table-column>
			</el-table>
		</div>
		<paginator
			:current_page="currentPage"
			:page_size="pageSize"
			:total_count="totalCount"
			@size-change-sent="handleSizeChange"
			@current-change-sent="handleCurrentChange"
		></paginator>
	</div>
</template>
<script type="text/javascript">
import PanelTitle from "../../components/PanelTitle";
import Paginator from "../../components/Paginator";

export default {
	data() {
		return {
			accounts: [],  // 用户数据列表
			loading: true,  // 加载中
			isSupperUserLogin: true,  // 是否是超级管理员身份
			totalCount: 0,  // 用户数据总数
			currentPage: 1,  // 当前页码
			pageSize: 10,  // 页数
		};
	},
	components: {
		PanelTitle,
		Paginator,
	},
	created() {
		// 页面创建时请求数据
		this.getAccountData(this.currentPage, this.pageSize);
	},
	methods: {
		// 请求用户数据
		getAccountData(current_page, page_size) {
			this.loading = true;
			this.$http
				.get(this.$store.state.url.account.list, {
						'params': {
							pageSize: page_size,
							currentPage: current_page,
						}
					}
				).then(({data: data}) => {
				this.accounts = data['rows'];
				this.totalCount = data['count'];
				this.isSupperUserLogin = data['is_superuser'];
				this.loading = false;
			}).catch(() => {
				this.loading = false;
			});
		},
		// 删除指定用户
		deleteAccount(id) {
			this.$http
				.post(
					this.formatString(this.$store.state.url.account.remove, {
						id: id,
					})
				)
				.then(() => {
					this.$message.success(
						this.$store.getters.$lang.messages.successDelete
					);
					this.loading = false;
					this.getAccountData(this.currentPage, this.pageSize);
				})
				.catch(() => {
					this.$message.error(this.$store.getters.$lang.messages.errorDelete);
					this.loading = false;
				});
		},
		// 提交删除用户
		onSingleDelete(id) {
			this.$confirm(
				this.$store.getters.$lang.messages.confirm,
				this.$store.getters.$lang.buttons.confirm,
				{
					confirmButtonText: this.$store.getters.$lang.buttons.yes,
					cancelButtonText: this.$store.getters.$lang.buttons.no,
					type: "warning",
				}
			).then(() => {
				this.deleteAccount(id);
			});
		},
		handleSizeChange(val) {
			this.pageSize = val;
			this.getAccountData(this.currentPage, this.pageSize);
		},
		handleCurrentChange(val) {
			this.currentPage = val;
			this.getAccountData(this.currentPage, this.pageSize);
		},
	},
};
</script>

