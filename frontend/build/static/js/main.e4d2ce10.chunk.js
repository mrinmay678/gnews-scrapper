(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{12:function(t,e,n){},13:function(t,e,n){},15:function(t,e,n){"use strict";n.r(e);var c=n(1),i=n.n(c),a=n(3),r=n.n(a),s=(n(12),n(4)),h=n(5),o=n(7),j=n(6),d=(n(13),n(0)),l=function(t){Object(o.a)(n,t);var e=Object(j.a)(n);function n(){var t;Object(s.a)(this,n);for(var c=arguments.length,i=new Array(c),a=0;a<c;a++)i[a]=arguments[a];return(t=e.call.apply(e,[this].concat(i))).baseURL="http://15.206.75.100:8000/",t.state={data:[]},t}return Object(h.a)(n,[{key:"componentDidMount",value:function(){var t=this;fetch("".concat(this.baseURL,"news/scrap"),{method:"GET",headers:{"Content-Type":"application/json"}}).then((function(t){return t.json()})).then((function(e){t.setState({data:e.data}),console.log(t.state.data)}))}},{key:"render",value:function(){return Object(d.jsx)("div",{children:Object(d.jsxs)("table",{children:[Object(d.jsxs)("tr",{children:[Object(d.jsx)("th",{children:"Image"}),Object(d.jsx)("th",{children:"Title"}),Object(d.jsx)("th",{children:"Published at"})]}),this.state.data.map((function(t){return Object(d.jsxs)("tr",{children:[Object(d.jsx)("td",{children:Object(d.jsx)("a",{href:t.link,children:Object(d.jsx)("img",{src:t.image,width:"50",height:"50"})})}),Object(d.jsx)("td",{children:Object(d.jsx)("a",{href:t.link,children:t.title})}),Object(d.jsx)("td",{children:t.time})]})}))]})})}}]),n}(c.Component),b=function(t){t&&t instanceof Function&&n.e(3).then(n.bind(null,16)).then((function(e){var n=e.getCLS,c=e.getFID,i=e.getFCP,a=e.getLCP,r=e.getTTFB;n(t),c(t),i(t),a(t),r(t)}))};r.a.render(Object(d.jsx)(i.a.StrictMode,{children:Object(d.jsx)(l,{})}),document.getElementById("root")),b()}},[[15,1,2]]]);
//# sourceMappingURL=main.e4d2ce10.chunk.js.map