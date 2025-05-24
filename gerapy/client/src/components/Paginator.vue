<template>
    <el-pagination
        class="paginator_container"
    	:current-page="current_page" 
    	:page-size="page_size" 
    	:page-sizes="[10, 20, 30, 50, 100]" 
    	:size="size"
    	:disabled="disabled"
    	:background="background"
    	layout="->,total, sizes, prev, pager, next, jumper"
    	:total="total_count"
    />
</template>
<script>
export default {
    name: "Paginator",
    props: {
        total_count: {
            type: Number,
            default:10,
        },
        current_page: {
            type: Number,
            default: 1,
        },
        page_size: {
            type: Number,
            default: 10,
        },
    },
    data() {
        return{}
    },
    methods:{},
};
</script>
