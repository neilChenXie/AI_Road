**2.4G以太网接口说明文档**

**（v3.0）**

1简介[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940669 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >3</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2API接口函数说明[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940670 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >3</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.1以太网库函数初始化RdrLibinit[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940671 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >3</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.2服务器启动监听RdrStartListen[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940672 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >4</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.3启动接收RdrStartAccept[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940673 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >4</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.4获得卡号数据RdrGetCardId[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940674 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >5</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.5设置授权RdrSetAuthorize[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940675 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >5</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.6取消授权RdrCancelAuthorize[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940676 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >6</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.7设置读卡器ID RdrSetReaderId[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940677 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >6</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.8查询读卡器ID RdrGetReaderId[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940678 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >7</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.9设置蜂鸣器开关RdrSetBuzzerSwitch[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940679 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >7</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.10获取蜂鸣器开关状态RdrGetBuzzerSwitch[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940680 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >8</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.11设置读卡器工作模式RdrSetReadMode[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940681 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >8</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.12获取读卡器工作模式RdrGetReadMode[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940682 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >9</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.13设置继电器开关RdrSetRelay[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940683 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >10</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.14设置衰减器调节方式RdrSetAttenuatorMode[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940684 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >11</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.15获取衰减器调节方式RdrGetAttenuatorMode[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940685 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >11</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.16获取机器号对应的IP地址RdrGetMachineIP[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940686 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >12</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.17关闭套接字库RdrCloseSock[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940687 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >12</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

2.18查询设备心跳RdrGetHeartBeat[if supportFields]><span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-begin" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >&nbsp;PAGEREF _Toc427940688 \h </span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-separator" ></span></span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" >13</span><span style="mso-spacerun:'yes';font-family:Calibri;mso-fareast-font-family:宋体;
mso-bidi-font-family:'Times New Roman';font-size:11.0000pt;mso-font-kerning:0.0000pt;" ><span style="mso-element:field-end" ></span></span></span><!

# 1简介

适用的产品为：RDR-2I01C、RDR-2I02C、RDR-2I03C、RDR-2I04C

一般性使用的流程为：

第1步RdrLibinit();初始化库

第2步RdrStartListen();开启服务器监听

第3步RdrStartAccept();启动接收

第4步Char out_data[4096] = {0};自定义变量用来放接受数据

第5步RdrGetCardid(out_data);接受数据

第6步RdrCloseSock();断开连接，关闭套接字库，并释放资源

# 2 API接口函数说明

## 2.1以太网库函数初始化RdrLibinit

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| 函数原型 | int  RdrLibinit(void) |  |  |  |  |
| 函数功能 | 以太网库函数初始化 |  |  |  |  |
| 参数 |  |  |  |  |  |
| 参数名 | 传输方向 | 参数类型 | 参数意义 |  | 取值说明 |
| 无 |  |  |  |  |  |
| 返回值 |  |  |  |  |  |
| 返回类型 | 返回值 |  |  | 返回值说明 |  |
| int | 0 |  |  | 加载套接字库成功，库版本2.2 |  |
| int | -1 |  |  | 加载套接字库失败 |  |

## 2.2服务器启动监听 RdrStartListen

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int  RdrStartListen(int port) |  |  |  |  |
| 函数功能 |  | 服务器启动监听 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| port | IN |  | int | 端口号 |  | 服务器监听端口号 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 0 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 监听失败 |  |

## 2.3启动接收 RdrStartAccept

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int  RdrStartAccept(void) |  |  |  |  |
| 函数功能 |  | 服务器启动接收 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| 无 |  |  |  |  |  |  |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 0 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 接收线程创建失败 |  |

## 2.4获得卡号数据 RdrGetCardId

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int  RdrGetCardId(char *outcardid) |  |  |  |  |
| 函数功能 |  | 获得设备接收到的卡号数据 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| outcardid | OUT |  | Char* | 输出的数据 |  | 参加通信协议 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 命令失败 |  |

## 2.5设置授权 RdrSetAuthorize

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int RdrSetAuthorize(char *inoldmachineid, char *cmdtext) |  |  |  |  |
| 函数功能 |  | 设置授权 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inoldmachineid | IN |  | Char* | 读卡器ID |  |  |
| cmdtext | IN |  | Char* | 有效数据 |  | 参见通信协议 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 授权命令失败 |  |

## 2.6取消授权RdrCancelAuthorize

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int RdrCancelAuthorize(char *inoldmachineid, char *cmdtext) |  |  |  |  |
| 函数功能 |  | 取消授权 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inoldmachineid | IN |  | Char* | 读卡器ID |  |  |
| cmdtext | IN |  | Char* | 有效数据 |  | 参见通信协议 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 命令失败 |  |

## 2.7设置读卡器ID RdrSetReaderId

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int RdrSetReaderId(char *inoldmachineid, char *cmdtext); |  |  |  |  |
| 函数功能 |  | 设置读卡器ID |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inoldmachineid | IN |  | Char* | 12个十六进制F |  | FFFFFFFFFFFF |
| cmdtext | IN |  | Char* | 要设置的ID |  |  |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
|  |  | -1 |  |  | 命令失败 |  |

## 2.8查询读卡器ID RdrGetReaderId

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int RdrGetReaderId(char *inoldmachineid, char *outnewmachineid) |  |  |  |  |
| 函数功能 |  | 查询读卡器ID |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inoldmachineid | IN |  | Char* | 读卡器ID |  |  |
| outnewmachineid | OUT |  | Char* | 输出的数据 |  |  |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
|  |  | -1 |  |  | 命令失败 |  |

## 2.9设置蜂鸣器开关RdrSetBuzzerSwitch

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int RdrSetBuzzerSwitch(char *inoldmachineid, char *cmdtext) |  |  |  |  |
| 函数功能 |  | 设置读卡器的蜂鸣器开关状态 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inoldmachineid | IN |  | char * | 读卡器机器ID |  | 12个十六进制数字 |
| cmdtext | IN |  | char * | 开关状态 |  | “0”:蜂鸣器开启“1”:蜂鸣器关闭 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 命令失败 |  |

## 2.10获取蜂鸣器开关状态RdrGetBuzzerSwitch

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int  RdrGetBuzzerSwitch(char *inoldmachineid, char *cmdtext) |  |  |  |  |
| 函数功能 |  | 获取读卡器的蜂鸣器开关状态 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inoldmachineid | IN |  | char * | 读卡器机器ID |  | 12个十六进制数字 |
| cmdtext | OUT |  | char * | 开关状态 |  | “0”:蜂鸣器开启“1”:蜂鸣器关闭 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 命令失败 |  |

## 2.11设置读卡器工作模式RdrSetReadMode

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int RdrSetReadMode(char *inoldmachineid, char *cmdtext) |  |  |  |  |
| 函数功能 |  | 设置读卡器的工作模式 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inoldmachineid | IN |  | char * | 读卡器机器ID |  | 12个十六进制数字 |
| cmdtext | IN |  | char * | 读卡器工作模式 |  | “0”:触发读卡 “1”:连续读卡 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 命令失败 |  |

## 2.12获取读卡器工作模式RdrGetReadMode

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int RdrGetReadMode(char *inoldmachineid, char *cmdtext) |  |  |  |  |
| 函数功能 |  | 获取读卡器的工作模式 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inoldmachineid | IN |  | char * | 读卡器机器ID |  | 12个十六进制数字 |
| cmdtext | OUT |  | char * | 读卡器工作模式 |  | “0”:触发读卡 “1”:连续读卡 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 命令失败 |  |

## 2.13设置继电器开关RdrSetRelay

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int RdrSetRelay(char *inmachineid, char *cmdtext) |  |  |  |  |
| 函数功能 |  | 设置继电器开关 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inmachineid | IN |  | char * | 读卡器机器ID |  | 12个十六进制数字 |
| cmdtext | IN |  | char * | 继电器开关 |  | “0”:开启继电器 “1”:关闭继电器 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 命令失败 |  |

## 2.14设置衰减器调节方式RdrSetAttenuatorMode

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int RdrSetAttenuatorMode(char *inmachineid, char *cmdtext) |  |  |  |  |
| 函数功能 |  | 设置衰减器调节方式 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inmachineid | IN |  | char * | 读卡器机器ID |  | 12个十六进制数字 |
| cmdtext | IN |  | char * | 衰减器调节方式 |  | “00”:手动调节 “E0-->FF”:软件调节E0：最小，FF:最大 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 命令失败 |  |

## 2.15获取衰减器调节方式RdrGetAttenuatorMode

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | int  RdrGetAttenuatorMode(char *inmachineid, char *cmdtext) |  |  |  |  |
| 函数功能 |  | 获取衰减器调节方式 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inmachineid | IN |  | char * | 读卡器机器ID |  | 12个十六进制数字 |
| cmdtext | OUT |  | char * | 衰减器调节方式 |  | “00”:手动调节 “E0-->FF”:软件调节E0：最小，FF:最大 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| int |  | 1 |  |  | 命令成功 |  |
| int |  | -1 |  |  | 命令失败 |  |

## 2.16获取机器号对应的IP地址RdrGetMachineIP

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 函数原型 |  | unsigned long  RdrGetMachineIP(char *inmachineid) |  |  |  |  |
| 函数功能 |  | 获取机器号对应的IP地址 |  |  |  |  |
| 参数 |  |  |  |  |  |  |
| 参数名 | 传输方向 |  | 参数类型 | 参数意义 |  | 取值说明 |
| inmachineid | IN |  | char * | 读卡器机器ID |  | 12个十六进制数字 |
| 返回值 |  |  |  |  |  |  |
| 返回类型 |  | 返回值 |  |  | 返回值说明 |  |
| unsigned long |  | 当前机器号对应的IP地址 |  |  |  |  |

## 2.17关闭套接字库RdrCloseSock

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| 函数原型 | int RdrCloseSock(void) |  |  |  |  |
| 函数功能 | 关闭套接字库 |  |  |  |  |
| 参数 |  |  |  |  |  |
| 参数名 | 传输方向 | 参数类型 | 参数意义 |  | 取值说明 |
| 无 |  |  |  |  |  |
| 返回值 |  |  |  |  |  |
| 返回类型 | 返回值 |  |  | 返回值说明 |  |
| int | 0 |  |  | 成功 |  |
| int | -1 |  |  | 失败 |  |

## 2.18查询设备心跳RdrGetHeartBeat

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| 函数原型 | int RdrGetHeartBeat(char *cmdtext) |  |  |  |  |
| 函数功能 | 获得设备心跳 |  |  |  |  |
| 参数 |  |  |  |  |  |
| 参数名 | 传输方向 | 参数类型 | 参数意义 |  | 取值说明 |
| cmdtext | OUT | char * | 心跳内容 |  |  |
| 返回值 |  |  |  |  |  |
| 返回类型 | 返回值 |  |  | 返回值说明 |  |
| int | 1 |  |  | 成功 |  |
| int | -1 |  |  | 失败 |  |

