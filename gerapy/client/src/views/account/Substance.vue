<template>
	<el-form
		ref="form"
		:model="formData"
		:rules="rules"
		label-position="right"
		label-width="100px"
	>
		<el-form-item :label="$lang.columns.username" prop="username">
			<el-input
				v-model="formData.username"
				:placeholder="$lang.messages.enter + ' ' + $lang.columns.username"
				size="small"
			></el-input>
		</el-form-item>
		<el-form-item :label="$lang.columns.password" prop="password">
			<el-input
				v-model="formData.password"
				:placeholder="$lang.messages.enter + ' ' + $lang.columns.password"
				size="small"
			></el-input>
		</el-form-item>
		<el-form-item :label="$lang.columns.email" prop="email">
			<el-input
				v-model="formData.email"
				:placeholder="$lang.messages.enter + ' ' + $lang.columns.email"
				size="small"
			></el-input>
		</el-form-item>
		<el-form-item :label="$lang.columns.is_staff" prop="is_staff">
			<el-select
				v-model="formData.is_staff"
				:placeholder="$lang.messages.is_staff"
				size="small"
			>
				<el-option :key="1" :label="$lang.buttons.yes" :value="1"></el-option>
				<el-option :key="0" :label="$lang.buttons.no" :value="0"></el-option>
			</el-select>
		</el-form-item>
		<el-form-item :label="$lang.columns.is_active" prop="is_active">
			<el-select
				v-model="formData.is_active"
				:placeholder="$lang.messages.is_active"
				size="small"
			>
				<el-option :key="1" :label="$lang.buttons.normal" :value="1"></el-option>
				<el-option :key="0" :label="$lang.buttons.delete" :value="0"></el-option>
			</el-select>
		</el-form-item>
		<div>
			<el-form-item>
				<slot name="submit"></slot>
				<el-button size="small" @click="$router.back()">
					<i class="fa fa-reply"></i>
					{{ $lang.buttons.return }}
				</el-button>
			</el-form-item>
		</div>
	</el-form>
</template>

<script>
export default {
	name: "Substance",
	props: {
		id: {  // 接收父组件传过来的参数
			type: String,
			default: null,
		},
	},
	data() {
		return {
			formData: {  // 该参数将接收所有字段值
				username: null,
				password: [],
				email: null,
				is_staff: null,
				is_active: null,
			},
			clientOptions: [],
			rules: {  // 指定表单字段校验规则
				username: [
					{
						required: true,
						message:
							this.$store.getters.$lang.columns.username +
							" " +
							this.$store.getters.$lang.messages.isNull,
						trigger: "blur",
					},
				],
				password: [
					{
						required: true,
						message:
							this.$store.getters.$lang.columns.password +
							" " +
							this.$store.getters.$lang.messages.isNull,
						trigger: "blur",
					},
				],
				email: [
					{
						required: true,
						message:
							this.$store.getters.$lang.columns.email +
							" " +
							this.$store.getters.$lang.messages.isNull,
						trigger: "blur",
					},
				],
			},
		};
	},
	mounted() {
		this.getAccountData();
	},
	methods: {
		// 存在用户id时再获取该用户数据，编辑用户时会进行
		getAccountData() {
			if (this.id) {
				this.$http
					.get(
						this.formatString(this.$store.state.url.account.info, {
							id: this.id,
						})
					)
					.then(({data: {data: account}}) => {
						this.formData = account;
					})
					.catch(() => {
						this.$message.error(this.$store.getters.$lang.messages.loadError);
					});
			}
		},
	},
};
</script>

<style lang="scss">
.el-date-editor.el-input {
	width: 152px;
}

.el-tag.el-tag--info {
	color: #35cbaa;
}

.el-select .el-tag__close.el-icon-close {
	background-color: #eeeeee;

	&:hover {
		background-color: #cccccc;
	}
}

.el-picker-panel {
	.el-picker-panel__footer {
		.el-button.el-picker-panel__link-btn.el-button--text.el-button--mini {
			display: none;
		}
	}

	.el-picker-panel__sidebar {
		.el-picker-panel__shortcut {
			font-size: 12px;
		}
	}
}
</style>

