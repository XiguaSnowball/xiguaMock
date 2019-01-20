Welcome to the xiguaMock wiki!
> 规则模仿了Mockjs

## 数据模板定义规范
#### 数据模板中的每个属性由 3 部分构成：属性名、生成规则、属性值：
```
// 属性名   name
// 生成规则 rule
// 属性值   value
'name|rule': value
```
#### 注意：

* 属性名 和 生成规则 之间用竖线 | 分隔。
* 生成规则 是可选的。
* 生成规则 有 4 种格式：
<ol> 
<li> <p><code>  'name|min-max': value </code></p></li>
<li> <p><code>  'name|count': value</code></p></li>
<li> <p><code>  'name|+loop': value</code></p></li>
<li> <p><code>  'name|+minLoop-maxLoop': value</code></p></li>
</ol>

*  生成规则 的 含义 需要依赖 属性值的类型 才能确定。
*  属性值 还指定了最终值的初始值和类型。
#### 生成规则和示例：

### 1. 属性值是字符串 String
<ol>
<li> 
<p><code>'name|min-max': string</code></p>
<p>通过重复 string 生成一个字符串，重复次数大于等于 min，小于等于 max。</p>
</li>
<li> <p><code>'name|count': string</code></p>

<p>通过重复 string 生成一个字符串，重复次数等于 count。</p></li>
</ol>


### 2. 属性值是数字 Number
<ol>

<li> <p><code>'name|+loop': number</code></p>
<p>属性值加自身loop次，也就是number*loop,number 只是用来确定类型。 </p></li>

<li> <p><code>'name|+minLoop-maxLoop': number</code></p>
<p>生成一个大于等于 minLoop、小于等于 maxLoop 的整数loop，属性值加自身loop次属性值,也就是number x loop, number 只是用来确定类型。</p></li>

<li> <p><code>'name|min-max': number</code></p>
<p>生成一个大于等于 min、小于等于 max 的整数，属性值 number 只是用来确定类型。如果number的类型为float，则返回区间内随机的小数，小数点后保留2位</p></li>
</ol>

>属性值 number 只是用来确定类型。如果number的类型为float，则返回区间内随机的小数，小数点后保留2位


### 3. 属性值是布尔型 Boolean
<ol>
<li> <p><code>'name|1': boolean</code></p>

<p>随机生成一个布尔值，值为 true 的概率是 1/2，值为 false 的概率同样是 1/2。</p></li>
</ol>

### 4. 属性值是对象 Object
<ol>
<li> <p><code>'name|count': object</code></p>

<p>从属性值 object 中随机选取 count 个属性。</p></li>

<li> <p><code>'name|min-max': object</code></p>

<p>从属性值 object 中随机选取 min 到 max 个属性。</p></li>
</ol>

### 5. 属性值是数组 Array
<ol>
<li> <p><code>'name|count': array</code></p>
<p>从属性值 array 中随机选取 count 个元素，作为最终值。</p></li>

<li> <p><code>'name|min-max': array</code></p>
<p>从属性值 array 中随机选取 min-max 个元素，作为最终值。</p></li>

<li> <p><code>'name|+loop': array</code></p>
<p>+代表重复，通过重复属性值 array 生成一个新数组，重复次数为 loop。</p></li>

<li> <p><code>'name|+minLoop-maxLoop': array</code></p>
<p>+代表重复，通过重复属性值 array 生成一个新数组，重复次数为 minLoop-maxLoop。</p></li>

</ol>

### 6. 属性值是函数 Function
<ol>
<li> <p><code>'name': function</code></p>

<p>执行函数 function，取其返回值作为最终的属性值，函数的上下文为属性 'name' 所在的对象。</p></li>
</ol>

### 7. 属性值是正则表达式 RegExp
<ol>
<li> <p><code>'name': regexp</code></p>

<p>根据正则表达式 regexp 反向生成可以匹配它的字符串。用于生成自定义格式的字符串。</p>
<pre>
({
    'regexp1': /[a-z][A-Z][0-9]/,
    'regexp2': /\w\W\s\S\d\D/,
    'regexp3': /\d{5,10}/
})
// =>
{
    "regexp1": "pJ7",
    "regexp2": "F)\fp1G",
    "regexp3": "561659409"
}</pre>