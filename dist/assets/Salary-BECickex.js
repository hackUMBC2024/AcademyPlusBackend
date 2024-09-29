import{C as P,j as O,B as A,s as _,k as x,l as q,p as I,q as M,x as N,y as T,z as C,A as $,D as B,_ as F,m as K,c as R,a as D,d as U,F as V,u as z,r as E,o as G}from"./index-D_nW0DFF.js";const S={data:{type:Object,required:!0},options:{type:Object,default:()=>({})},plugins:{type:Array,default:()=>[]},datasetIdKey:{type:String,default:"label"},updateMode:{type:String,default:void 0}},W={ariaLabel:{type:String},ariaDescribedby:{type:String}},Z={type:{type:String,required:!0},destroyDelay:{type:Number,default:0},...S,...W},H=q[0]==="2"?(t,e)=>Object.assign(t,{attrs:e}):(t,e)=>Object.assign(t,e);function d(t){return B(t)?C(t):t}function J(t){let e=arguments.length>1&&arguments[1]!==void 0?arguments[1]:t;return B(e)?new Proxy(t,{}):t}function Q(t,e){const s=t.options;s&&e&&Object.assign(s,e)}function w(t,e){t.labels=e}function L(t,e,s){const o=[];t.datasets=e.map(r=>{const a=t.datasets.find(l=>l[s]===r[s]);return!a||!r.data||o.includes(a)?{...r}:(o.push(a),Object.assign(a,r),a)})}function X(t,e){const s={labels:[],datasets:[]};return w(s,t.labels),L(s,t.datasets,e),s}const Y=O({props:Z,setup(t,e){let{expose:s,slots:o}=e;const r=I(null),a=_(null);s({chart:a});const l=()=>{if(!r.value)return;const{type:n,data:f,options:y,plugins:p,datasetIdKey:g}=t,b=X(f,g),c=J(b,f);a.value=new P(r.value,{type:n,data:c,options:{...y},plugins:p})},u=()=>{const n=C(a.value);n&&(t.destroyDelay>0?setTimeout(()=>{n.destroy(),a.value=null},t.destroyDelay):(n.destroy(),a.value=null))},j=n=>{n.update(t.updateMode)};return M(l),N(u),T([()=>t.options,()=>t.data],(n,f)=>{let[y,p]=n,[g,b]=f;const c=C(a.value);if(!c)return;let m=!1;if(y){const i=d(y),h=d(g);i&&i!==h&&(Q(c,i),m=!0)}if(p){const i=d(p.labels),h=d(b.labels),v=d(p.datasets),k=d(b.datasets);i!==h&&(w(c.config.data,i),m=!0),v&&v!==k&&(L(c.config.data,v,t.datasetIdKey),m=!0)}m&&$(()=>{j(c)})},{deep:!0}),()=>x("canvas",{role:"img",ariaLabel:t.ariaLabel,ariaDescribedby:t.ariaDescribedby,ref:r},[x("p",{},[o.default?o.default():""])])}});function tt(t,e){return P.register(e),O({props:S,setup(s,o){let{expose:r}=o;const a=_(null),l=u=>{a.value=u==null?void 0:u.chart};return r({chart:a}),()=>x(Y,H({ref:l},{type:t,...s}))}})}const et=tt("bar",A),at={name:"BarChart",components:{Bar:et},data(){return{chartData:{labels:["Career #1","Career #2","Career #3"],datasets:[{label:"Projected Salary",data:[40,20,12],backgroundColor:"rgba(62, 156, 53, 0.6)",borderColor:"rgba(62, 156, 53, 1)",borderWidth:1}]},chartOptions:{responsive:!0,scales:{y:{beginAtZero:!0}}}}},computer:{...K(z)}},st={id:"salary"};function rt(t,e,s,o,r,a){const l=E("Bar");return G(),R(V,null,[e[0]||(e[0]=D("h1",null,"Career Projections",-1)),D("div",st,[U(l,{id:"my-chart-id",options:r.chartOptions,data:r.chartData,width:"999px"},null,8,["options","data"])])],64)}const ot=F(at,[["render",rt]]);export{ot as default};
