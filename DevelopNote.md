# DevelopNote

不是开发者的朋友们，可以跳过这一节。

Say we have a piece of music for two or more people to play. It has multiple parts, one per player, and multiple
measures. XML represents data in a hierarchy, but musical scores are more like a lattice. How do we reconcile this?
Should the horizontal organization of musical parts be primary, or should the vertical organization of musical measures?

The answer is different for every music application. David Huron, a music cognition specialist and the inventor of
Humdrum, advised us to make sure we could represent music both ways, and be able to switch between them easily.

This is why MusicXML has two different score formats, each with its own root element. For a partwise document, the root
element is <score-partwise>. The musical part is primary, and measures are contained within each part. For a timewise
document, the root element is <score-timewise>. The measure is primary, and musical parts are contained within each
measure.

Having two different structures does not work well if there is no automatic way to switch between them. MusicXML
provides two XSLT stylesheets to convert back and forth between the two document types. The parttime.xsl stylesheet
converts from <score-partwise> to <score-timewise>, while the timepart.xsl stylesheet converts from <score-timewise>
to <score-partwise>.

---

假设我们有一段音乐供两个人或更多人演奏。它有多个部分，每个玩家一个，以及多个小节。XML以层次结构表示数据，但乐谱更像是一个格子。我们如何协调这一
点？音乐部分的横向组织应该是首要的，还是音乐措施的纵向组织？

每个音乐应用程序的答案都不同。音乐认知专家、Hudrum的发明者大卫·休伦（David Huron）建议我们确保我们能够以两种方式表达音乐，
并能够轻松地在两者之间切换。

这就是为什么MusicXML有两种不同的乐谱格式，每种格式都有自己的根元素。对于部分文档，根元素是<score partwise>。
音乐部分是首要的，每个部分都包含小节。对于时间型文档，根元素是<score timewise>。小节是主要的，每个小节中都包含音乐部分。

如果没有自动方式在两种不同的结构之间切换，那么拥有两种不同结构的效果就不好。MusicXML提供了两个XSLT样式表，可以在两种文档类型之间来回转换。parttime.xsl样式表从<score partwise>
转换为<score timewise>，而timepart.xsl样式从<score-timewise>转化为<score-partwise>。

---

An application reading MusicXML can choose which format is primary, and check for that document type. If it is your root
element, just proceed. If not, check to see if it is the other MusicXML root element. If so, apply the appropriate XSLT
stylesheet to create a new MusicXML document in your preferred format, and then proceed. If it is neither of the two
top-level document types, you do not have a MusicXML score, and can return an appropriate error message.

When your application writes to MusicXML, simply write to whichever format best meets your needs. Let the program
reading the MusicXML convert it if necessary.

In practice, most of today's MusicXML applications use the <score-partwise> format. If all else is equal, that would be
the format of choice for your application.