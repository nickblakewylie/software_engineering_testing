# Systems Theory and Ethics Zoom Transcript

**These are hardly perfect, but something you can scan**

WEBVTT

1
00:00:00.000 --> 00:00:00.719
way.

2
00:00:02.939 --> 00:00:06.870
Sean Goggins: So this is the systems thinking and software engineering ethics.

3
00:00:08.010 --> 00:00:21.210
Sean Goggins: section of module four module four is really focused on stepping back and looking at software engineering in a broader context that incorporates aspects of what is known as systems thinking.

4
00:00:26.220 --> 00:00:27.030
focus on.

5
00:00:28.380 --> 00:00:44.280
Sean Goggins: Alright, so systems theory is a long standing area of investigation that looks at how people processes and technology, work together to create a system and understanding.

6
00:00:45.000 --> 00:00:55.680
Sean Goggins: The system is different than having knowledge of the system so building knowledge about any particular system in this case in software engineering mostly focused on the software part of the system.

7
00:00:56.250 --> 00:01:04.140
Sean Goggins: We do analysis we decompose it we break it apart, so that we understand the problem that's what requirements focuses on.

8
00:01:04.770 --> 00:01:20.610
Sean Goggins: Understanding comes from then synthesizing those D compositions analysis finding connections between them and putting it all back together, so you have to break it apart, to put it back together if you want to really understand a system.

9
00:01:22.200 --> 00:01:33.660
Sean Goggins: And there are in software engineering, we have unintended consequences and unintended consequences emerge in non deterministic system systems where.

10
00:01:33.990 --> 00:01:46.050
Sean Goggins: We don't know all of the potential states that the software might enter into obviously safety critical systems have fewer of these non deterministic features ideally zero of them.

11
00:01:47.070 --> 00:01:54.630
Sean Goggins: But most of the systems that most of you will work on are going to be, to some degree non deterministic the example I like to use is Facebook.

12
00:01:55.440 --> 00:02:03.840
Sean Goggins: Nobody at Facebook and tell you what you're going to be presented with when you log in there's a series of algorithms that interact with a bunch of data.

13
00:02:04.230 --> 00:02:18.360
Sean Goggins: That determine what you are presented with and it can't really be predicted in advance, but any individual the system assembles it for you, based on a bunch of rules that are constantly changing, based on the new data that's added.

14
00:02:20.730 --> 00:02:31.110
Sean Goggins: So systems theory hair systems thinking has some benefits and the benefits are, the more that you think strategically, the more likely, you are to.

15
00:02:31.680 --> 00:02:43.380
Sean Goggins: react less and the less you react to things, the more likely, you are to make better decisions, so, if you look at the perspective of you have an event, for example.

16
00:02:44.070 --> 00:02:53.730
Sean Goggins: let's use a pandemic it's something that we react to it's not something that we could we did predict, or that we knew when it was going to happen.

17
00:02:54.510 --> 00:03:01.980
Sean Goggins: Public health experts and epidemiologists have long said that it was inevitable that we would have pandemics, like the one that we're living through.

18
00:03:02.610 --> 00:03:11.460
Sean Goggins: And those individuals thought about it from a visionary perspective, they thought what are all of the things that we've studied in disease models.

19
00:03:11.880 --> 00:03:21.600
Sean Goggins: And they reflected on them and tried to come up with plans for responding to events like the like the current pandemic when it happens so.

20
00:03:21.990 --> 00:03:32.070
Sean Goggins: To the extent that we think at the vision level ahead of time or or at least identify patterns that we adapt to, or systemic structures.

21
00:03:32.520 --> 00:03:36.030
Sean Goggins: we're increasing the leverage that we have when we're.

22
00:03:36.630 --> 00:03:51.780
Sean Goggins: Working on a system, the more that we're reacting to things as they happen and are operating from the perspective of what we want the system to be and what we want, or what a stakeholder wants the software to be the more likely we are to be constantly.

23
00:03:52.890 --> 00:03:54.810
Sean Goggins: chasing our tails as as.

24
00:03:57.030 --> 00:04:06.480
Sean Goggins: So systems theory and software decision making faces phases are closely tied together so there's this model that.

25
00:04:07.020 --> 00:04:19.530
Sean Goggins: Are civil we increased and developed last year that identified things that are ideas things that are development things that are evaluation and things that are announcements and.

26
00:04:20.580 --> 00:04:28.050
Sean Goggins: These are decision making phases that exist across a range of software systems that they studied in open source so.

27
00:04:28.530 --> 00:04:37.890
Sean Goggins: Identifying something is sort of recognizing a decision needs to be made and then diagnosing it and developing it is coming up with a solution.

28
00:04:38.310 --> 00:04:48.210
Sean Goggins: That you then evaluate if you're following the little arrows on the slide that moves you back into development where you're designing a revised solution and then evaluating it.

29
00:04:48.720 --> 00:04:57.900
Sean Goggins: And another iteration of design that finally meets the specifications that people want and at that stage view announced the release of a new.

30
00:04:58.320 --> 00:05:19.680
Sean Goggins: version of your software, so you can think about this process of agile software development as going through identification of problems and iterations on solutions and this idea model that they laid out I think is an interesting and useful way to to frame.

31
00:05:20.970 --> 00:05:22.620
Sean Goggins: what's what's happening.

32
00:05:23.640 --> 00:05:26.910
Sean Goggins: i'll pause to see if there are any questions at this at this point.

33
00:05:30.270 --> 00:05:31.260
Sean Goggins: Hearing none.

34
00:05:37.830 --> 00:05:38.400
Student 1: so far.

35
00:05:39.330 --> 00:05:49.140
Sean Goggins: I have this little clicker that supposed to be, I think, maybe because I clicked on zoom and stop working so systems theory and software decision phases.

36
00:05:49.890 --> 00:05:58.980
Sean Goggins: kind of work like this, there are patterns that the identified in the ways that open source software teams which mirror in many ways.

37
00:05:59.340 --> 00:06:08.430
Sean Goggins: The kinds of virtual development we're doing in this class and also the kind of distributed development you're likely to encounter when you enter the workplace as a software developer.

38
00:06:08.820 --> 00:06:17.880
Sean Goggins: So the shortcut is to have the idea and then announced that you've implemented a solution that's that's one pattern they identify the pattern a the.

39
00:06:18.600 --> 00:06:35.010
Sean Goggins: Second pattern is what they called implicit development have the idea you evaluated and then you move to the announcement and then possibly back further to evaluation and then there's implicit evaluation, where you move.

40
00:06:36.060 --> 00:06:42.930
Sean Goggins: partly through the process, but you sort of skip a formal evaluation and move straight to the announcement of the feature.

41
00:06:43.980 --> 00:06:44.850
Sean Goggins: The complete.

42
00:06:46.530 --> 00:06:55.740
Sean Goggins: cycle, where I think you would say, is the aspirational ideal way that software is constructed as you move sequentially through an idea its development.

43
00:06:56.190 --> 00:07:10.140
Sean Goggins: iterative evaluation redevelopment and, finally, an announcement of some new set of features that are available in the software that's that's sort of a perfect idealized model with complete and then there's also things you abandon I think.

44
00:07:11.370 --> 00:07:24.330
Sean Goggins: i've certainly had experiences where software teams i'm on come up with an idea we develop it we evaluate it and we ultimately recognize that this is not something that either we can reasonably accomplished or.

45
00:07:24.900 --> 00:07:35.040
Sean Goggins: That we want to accomplish that by going through the evaluation phase we recognize that this isn't something we actually want in the software that we actually want to release.

46
00:07:35.460 --> 00:07:44.340
Sean Goggins: So that's the abandonment pattern, so these design patterns of going through this model give you the idea, hopefully, that.

47
00:07:45.300 --> 00:08:03.330
Sean Goggins: There isn't one right way, or one exact way that these these software development and software engineering always occur there are there are different patterns and the teams that you're out in may implement these patterns deliberately or accidentally at different points in time.

48
00:08:05.370 --> 00:08:17.130
Sean Goggins: The one thing that you want to do is recognize what a system is so the system test is kind of a requirement for our systems thinking definition, so you want to look at the purpose.

49
00:08:17.550 --> 00:08:26.790
Sean Goggins: The parts of the system and the connections between them, so the purpose of a system is the way systems thinking way of.

50
00:08:27.270 --> 00:08:37.440
Sean Goggins: identifying how this whole system that you want to build can be completely understood the elements are the characteristics of the system implemented they might be components.

51
00:08:37.920 --> 00:08:52.500
Sean Goggins: At the requirements phase, they might be requirements in the design phase, they might be designed so the elements take on different shapes as we move through the software development lifecycle and the purpose and the elements are all connected in some way.

52
00:08:53.550 --> 00:09:00.600
Sean Goggins: So that they relate to each other so some elements are connected to different aspects of the purpose and likewise some.

53
00:09:01.800 --> 00:09:10.980
Sean Goggins: purposes are connected to different elements of the software and these these connections aren't one to one linear and clean.

54
00:09:12.210 --> 00:09:21.840
Sean Goggins: So more than one requirement and more than one design may may likely contribute to multiple aspects of the purpose of the elements that make sense.

55
00:09:26.370 --> 00:09:26.730
yeah.

56
00:09:28.230 --> 00:09:44.820
Sean Goggins: So there are these articles that are part of the reading this week, and they have these different ways of thinking about systems that that are worth considering and contrasting with each other and that's one of the assignments that I have for you.

57
00:09:46.050 --> 00:10:01.620
Sean Goggins: In this module so Richmond is kind of the originator of systems thinking and defines it as art and science of making reliable interfaces and developing increasing increasingly deep understanding of an underlying structure.

58
00:10:02.790 --> 00:10:12.270
Sean Goggins: singing, who is the next one sort of is a leader in the field and sees interrelationships rather than things and.

59
00:10:14.190 --> 00:10:24.570
Sean Goggins: The definition, he has doesn't describe it describes highly critical elements of systems thinking approach, but it doesn't provide a purpose for systems thinking.

60
00:10:26.130 --> 00:10:44.910
Sean Goggins: And, and so on, as you go through each I won't renew like my summary of each of the authors, but what i've done is i've said that you know, are you is the author talking about systems thinking in the context of a whole rather than parts interconnections nonlinear relationships.

61
00:10:46.230 --> 00:11:00.330
Sean Goggins: stock and flow diagrams are kind of like a have a component it's going to contribute to the flow of a system in some way dynamic behavior recognizes that systems again have this non deterministic aspect to them.

62
00:11:01.350 --> 00:11:14.190
Sean Goggins: Considering feedback loops is one perspective, recognizing the importance of systems that the system can be system as a cause of the systems behavior in and of itself.

63
00:11:15.270 --> 00:11:23.190
Sean Goggins: And then, how the systems structure generates behavior and Sweeney and sturman look at the delays aspect.

64
00:11:24.060 --> 00:11:38.670
Sean Goggins: How delays affect systems thinking and systems performance, so if you if you look at the two yellow highlighted lines you're covering a good deal of the overall systems thinking territory with those two articles in particular.

65
00:11:42.720 --> 00:11:57.810
Sean Goggins: And here's just another representation of how you might how I can sort of classify these articles and I do this for you, so that as you're as you're reading the articles that I provide you have a sense of what point of view.

66
00:11:59.400 --> 00:12:04.590
Sean Goggins: In relation to recognizing what a system is in in software and other contexts.

67
00:12:06.180 --> 00:12:14.910
Sean Goggins: is represented by the article, so you can see that the number of articles that focus on the interconnections and relationships, the whole rather than the part.

68
00:12:15.240 --> 00:12:24.870
Sean Goggins: And the dynamic behavior and the feedback loops and then a smaller number of articles that reflect these these other perspectives that I outlined in the previous slide.

69
00:12:27.450 --> 00:12:36.150
Sean Goggins: Does anyone have an example of a system that they've worked on where they can see how thinking about a whole comparative parts or.

70
00:12:37.320 --> 00:12:40.380
Sean Goggins: Any of the bubbles, I have here might be related.

71
00:12:42.480 --> 00:12:45.810
Student 1: At my job we basically have a.

72
00:12:46.950 --> 00:12:55.650
Student 1: loan Origination software and a customer customer relationship management software it's like CRM thing.

73
00:12:55.920 --> 00:13:15.540
Student 1: yeah and basically the end goal is to get a prospective veteran homebuyer through the whole entire loan process so converting them from original lead to originating there alone and eventually finalizing it and establishing alone with them.

74
00:13:15.930 --> 00:13:19.170
Student 1: yeah so there's like a lot of systems.

75
00:13:20.670 --> 00:13:26.280
Student 1: That go into it and i'm one of the core things that tends to occur is.

76
00:13:27.780 --> 00:13:36.120
Student 1: Basically, we have what would be the best thing to explain it there's a lot of like one like out of all the system.

77
00:13:36.570 --> 00:13:53.190
Student 1: attributes are listed like I think a big one, is just like interrelationships and interconnections so there's like real estate agents one officers, etc, and then you have to build out like components and software to pass all the data around between all the systems and stuff.

78
00:13:53.910 --> 00:14:04.590
Sean Goggins: yeah that's a really that's a really good example because each of these systems, for example, a customer relationship management system has is focused on taking a lead and.

79
00:14:05.070 --> 00:14:14.310
Sean Goggins: Ultimately, originating and completing alone for that person, but the software that's actually doing the work of originating alone.

80
00:14:14.670 --> 00:14:25.800
Sean Goggins: Has government regulatory and underwriting for risk components to it that are not really directly related to the relationship you're trying to build with the customer.

81
00:14:26.100 --> 00:14:34.920
Sean Goggins: But related to the risk that you're trying to assess and provide that customer with alone would that be a good characterization of the distinct purposes of these two systems.

82
00:14:35.700 --> 00:14:45.570
Sean Goggins: yeah yeah so you have that that's a really good example that you have these the whole system involves multiple different pieces of software that have different.

83
00:14:45.930 --> 00:15:02.280
Sean Goggins: primary objectives and getting them to be interconnected and related in a way, where the business is successful, is is, you have to think of not just one system, but the entire collection of systems as the whole system.

84
00:15:03.840 --> 00:15:05.280
Sean Goggins: good example yeah.

85
00:15:07.860 --> 00:15:19.920
Sean Goggins: So that's that's the systems thinking portion and there's enough like I said a number of articles, I encourage you to read and reflect on that's that's one of the assignments, this week the second thing.

86
00:15:20.910 --> 00:15:22.200
Sean Goggins: inside out okay.

87
00:15:22.440 --> 00:15:24.840
Sean Goggins: good to know i'm still here.

88
00:15:26.730 --> 00:15:39.270
Sean Goggins: So software engineering ethics is the second component and ethics are something that we don't necessarily always think about in computer science, education, but I think are really important because.

89
00:15:39.750 --> 00:15:54.030
Sean Goggins: What we are able to do as as folks very knowledgeable about software and systems can be applied in ways that are ethical and not ethical and so thinking explicitly about the ethics of the work that we do.

90
00:15:54.630 --> 00:16:04.410
Sean Goggins: I think is an important piece of information to cover in this course, and I really think we should move that zoom thing over so we're not sharing that.

91
00:16:07.830 --> 00:16:15.630
Sean Goggins: So software engineering ethics involves thinking about our wider responsibilities and the importance of behaving honest and ethically.

92
00:16:16.020 --> 00:16:25.410
Sean Goggins: As professionals and then it's not just upholding the law but also following some set of principles that are morally correct morally correct is kind of a.

93
00:16:25.920 --> 00:16:38.100
Sean Goggins: loaded term, but there are professional standards that we hold ourselves to as software engineers, the first is confidentiality that we respect that whomever employs us.

94
00:16:39.030 --> 00:16:48.750
Sean Goggins: or our clients have have the right to expect that we're not going to go resell the system that we build for them, or the ideas that we develop and learn from them.

95
00:16:49.080 --> 00:17:01.020
Sean Goggins: To their competitors, we have, we have a certain responsibility to keep the domain knowledge that we develop through building systems for people confidential between us and the people who have us build them.

96
00:17:01.920 --> 00:17:11.430
Sean Goggins: The second is competence, and this is a more difficult ethical constraints, because we don't on the one hand, want to misrepresent our level of competence.

97
00:17:12.540 --> 00:17:13.140
Sean Goggins: and

98
00:17:14.190 --> 00:17:17.790
Sean Goggins: On the other hand, different people have different.

99
00:17:18.420 --> 00:17:30.510
Sean Goggins: ways of thinking about what their competence is and representing it so our personalities come into play when when we're thinking about the ethics of representing our competence i've i've worked with.

100
00:17:31.470 --> 00:17:36.810
Sean Goggins: Hundreds at least, maybe even a few thousand different software engineers over my career.

101
00:17:37.350 --> 00:17:49.650
Sean Goggins: And i'd say there's a range of people, some of whom routinely overestimate their competence and rise to their overestimation in the context of performing the work.

102
00:17:50.340 --> 00:17:59.610
Sean Goggins: There are other people at the opposite end of the spectrum who routinely underestimate what their actual competence is in comparison to their peers.

103
00:18:00.000 --> 00:18:14.970
Sean Goggins: And over perform, but maybe don't get as much opportunity professionally so recognizing what our competence level is and talking about it less in terms of I know.

104
00:18:15.480 --> 00:18:26.640
Sean Goggins: These languages or I know these technologies and more in terms of i've built systems that do these kinds of things and i've participated in.

105
00:18:27.180 --> 00:18:38.310
Sean Goggins: Understanding the requirements and doing the design and i've learned four or five languages or whatever the number is through the work that i've done in a number of projects so.

106
00:18:38.730 --> 00:18:47.700
Sean Goggins: The more time that you spend doing software development work in software engineering, the less you'll feel that not having worked in a particular language before.

107
00:18:48.060 --> 00:18:58.500
Sean Goggins: reflects a lack of your competence to do so, so once you've learned two or three languages on the job your capacity to figure out a new one.

108
00:18:58.890 --> 00:19:10.440
Sean Goggins: is very high, and so the absence of having done it before is something to consider, as you know, do you represent the fact that you've never coded in the gold language before.

109
00:19:10.770 --> 00:19:26.430
Sean Goggins: Or do you represent that you've developed very similar systems in Python and learned see assembler Java c++ and Python leading up to the position that you're currently talking to someone about and.

110
00:19:26.880 --> 00:19:36.810
Sean Goggins: In fact, your likelihood of learning and becoming competent in a new language like go is very high, so how you represent your competence is important both to not.

111
00:19:37.320 --> 00:19:47.250
Sean Goggins: Over represented in a way, where you're misleading people about what you can accomplish or underrepresented in a way that that sells yourself short so it's a tricky one.

112
00:19:49.350 --> 00:20:01.920
Sean Goggins: The other a couple other issues that we face professionally our intellectual property rights, in some cases, those are explicitly governed by different laws such as patent and copyright.

113
00:20:02.370 --> 00:20:08.880
Sean Goggins: In other cases, the governance is more more loosely coordinated in the case of open source software.

114
00:20:09.480 --> 00:20:18.060
Sean Goggins: Intellectual property rights are declared by the software license that's used so, for example, there's a license called jpl.

115
00:20:18.510 --> 00:20:27.060
Sean Goggins: Which means that any software that's got the new public license associated with it, if you deploy that software, with a product.

116
00:20:27.510 --> 00:20:35.730
Sean Goggins: All of the software that you deploy with the GPS software has to be open sourced itself under the terms of the license so it's difficult.

117
00:20:36.150 --> 00:20:44.760
Sean Goggins: To create a piece of commercial software that you closed source from a piece of GPS software because of that, the licensing constraints.

118
00:20:45.420 --> 00:20:53.790
Sean Goggins: there's another license called the MIT license that explicitly encourages you to take a piece of open source software and commercialize it.

119
00:20:54.240 --> 00:21:00.840
Sean Goggins: For your own purposes and profit and and in that case, the idea is.

120
00:21:01.770 --> 00:21:18.750
Sean Goggins: One way of sustaining a software project is to make it easy for people to take what you've done and commercialize it on their own, without your involvement it's it's how you think about what you're doing and an open source way and it relates directly to intellectual property rights.

121
00:21:21.120 --> 00:21:26.220
Sean Goggins: And when since most since I can't say all because you know.

122
00:21:27.810 --> 00:21:29.700
Sean Goggins: never, never say all.

123
00:21:30.930 --> 00:21:37.380
Sean Goggins: But most technology companies use open source software, at least to some extent and.

124
00:21:38.370 --> 00:21:47.190
Sean Goggins: anytime a technology company buys another technology company, one of the things that they are most interested in is understanding the licensing risk.

125
00:21:47.610 --> 00:21:58.950
Sean Goggins: That they're taking on so they look at what Open Source projects compose the technical value of the company and of those projects which of them have.

126
00:21:59.220 --> 00:22:07.440
Sean Goggins: Have risks of either not having declared a license or having a license declared that introduced to other software projects might.

127
00:22:08.010 --> 00:22:25.320
Sean Goggins: force those projects to be open source unintentionally, and so intellectual property rights is a very dynamic and expanding space where there aren't as many clear answers as you might expect there to be any questions about any of that.

128
00:22:29.520 --> 00:22:29.970
Sean Goggins: All right.

129
00:22:31.230 --> 00:22:44.940
Sean Goggins: Professional responsibility wise there's also, of course, the concern about computer misuse, so it can range from things that are relatively trivial like playing games on your employer's computer to something serious like the dissemination of viruses.

130
00:22:46.710 --> 00:22:57.450
Sean Goggins: A lot of cultures in in technology actually are okay with you watching YouTube videos on your lunch hour or playing video games on your laptop.

131
00:22:57.840 --> 00:23:08.310
Sean Goggins: that's owned by the company after hours that you know they look at that, as a benefit that that's offered to you by having a high quality piece of technology in your possession and.

132
00:23:08.940 --> 00:23:17.520
Sean Goggins: Their hope, the hope of course of the firm or the organization that you work for is that you loving that machine will also make you more likely to work on work stuff.

133
00:23:18.270 --> 00:23:28.740
Sean Goggins: In your off hours as well, so what computer misuse is will be defined by the terms and conditions and whoever has provided you with the computer.

134
00:23:29.790 --> 00:23:39.900
Sean Goggins: Obviously, if you're doing things that are highly secure you're likely not going to do anything but the work on that computer, but there are many cases where that isn't what the computers for.

135
00:23:41.490 --> 00:23:44.310
Sean Goggins: And, and when I said earlier that ethics are.

136
00:23:45.600 --> 00:23:56.220
Sean Goggins: sort of subject to interpretation and it's kind of a loose term, but that we have professional ethics in software engineering and computing.

137
00:23:56.700 --> 00:24:08.370
Sean Goggins: I referred, I guess, I refer specifically to the acm Association for computing machinery in the ieee Institute of electrical and electronic engineers shared code of ethics.

138
00:24:09.120 --> 00:24:16.350
Sean Goggins: These are professional societies that have said, you know no individual employer no individual.

139
00:24:16.800 --> 00:24:25.740
Sean Goggins: really should be shaping how we define the ethics for computing professionals, and so we, as an independent organization of computing professionals.

140
00:24:26.220 --> 00:24:34.860
Sean Goggins: are presenting this shared set of principles that we expect our Members to consider and abide by in the course of doing their work.

141
00:24:35.220 --> 00:24:43.830
Sean Goggins: And it's a sort of code of practice that you commit to as a professional software engineer it's the professionalization of the work that you do.

142
00:24:44.700 --> 00:24:56.160
Sean Goggins: And these two organizations do a lot to advocate for computing professionals and the both the ethics that we expect each other to follow, but also our rights.

143
00:24:56.490 --> 00:25:09.000
Sean Goggins: In the work in the workplace in the marketplace, so there are eight principles related to behavior and decisions we make it software engineers in the workplace, so the rationale is that.

144
00:25:10.050 --> 00:25:32.100
Sean Goggins: computers have this big role and because of our old building these systems, we have a big opportunity to both do good and do harm and we want to able, we want to enable people to do good or influence good so as to ensure that efforts are used for good we commit to this code of ethics.

145
00:25:33.480 --> 00:25:40.950
Sean Goggins: And the preamble is right there and it basically I could boil it down in a nutshell, to tell you that.

146
00:25:42.360 --> 00:25:53.160
Sean Goggins: it's an aspirational code of ethics and by aspirational I mean there will be times, where not all of us follow every precept of this code of ethics and every case.

147
00:25:53.760 --> 00:26:02.010
Sean Goggins: There are times when our own judgment or our own individual sense of ethics has to supersede the professional ethics.

148
00:26:02.370 --> 00:26:10.530
Sean Goggins: And we'll talk about a few of those in a minute here, but the eight core ethical principles are focused on the public.

149
00:26:11.160 --> 00:26:21.120
Sean Goggins: That we want to work in the public interest that we don't want to work up work in outside of the public interest that we have responsibility to the people who employ us.

150
00:26:22.080 --> 00:26:31.950
Sean Goggins: That we want to produce the highest quality product that we can using judgment that has both integrity and independence from the other pressures that we feel.

151
00:26:32.370 --> 00:26:45.120
Sean Goggins: And that we expect our leaders in software work to promote these ethical behaviors so sometimes you may be faced in real life with management team that doesn't.

152
00:26:45.840 --> 00:26:56.610
Sean Goggins: isn't even it doesn't even a background in computing and it's asking you to do things that you may recognize as not ethical and so we want to encourage the employment and.

153
00:26:57.870 --> 00:27:05.940
Sean Goggins: advancement of management personnel who recognize the ethics responsibility ethical responsibilities of computing professionals.

154
00:27:06.960 --> 00:27:15.090
Sean Goggins: And that we are a profession that works with integrity and cares about our reputation, we also want to be fair and supportive of our colleagues.

155
00:27:15.450 --> 00:27:28.590
Sean Goggins: and also to my point about how to represent your competence, you want to be fair and and sort of fair yourself and represent yourself in the best possible way when you're out in the world.

156
00:27:32.370 --> 00:27:36.030
Sean Goggins: So ordinarily I would have breakout groups, but this is pretty small.

157
00:27:37.980 --> 00:27:42.480
Sean Goggins: And, but maybe we can just have a brief discussion here about.

158
00:27:43.560 --> 00:27:46.080
Sean Goggins: What is an ethical issue.

159
00:27:47.430 --> 00:28:03.420
Sean Goggins: You know there's there's four examples that I provide one is a pharmacy I use EBS as the example sells you're buying information to a third party and other is when Edward snowden we classified documents about US government information.

160
00:28:04.620 --> 00:28:15.120
Sean Goggins: I assume everyone's familiar with that via yeah and i'm sure you're also familiar with the 2016 Cambridge analytica Facebook data.

161
00:28:16.650 --> 00:28:17.490
Sean Goggins: brouhaha.

162
00:28:18.390 --> 00:28:37.890
Sean Goggins: yeah and then researchers at the university analyzing posts from Twitter, and so what we want to consider is what makes something an ethical issue like where we're in space and time is is are the ethical questions and each of these cases.

163
00:28:39.330 --> 00:28:57.000
Sean Goggins: arrived at, so in the case of CVs selling your information to a third party, what are the ethical concerns, and so, if it's an ethical issue if it generates the question is this right or wrong and concerns your values and how they're applied in products and services.

164
00:28:58.470 --> 00:29:09.240
Sean Goggins: So if we go back here the US CVs selling my information to a third party, what would make that an ethical concern.

165
00:29:12.930 --> 00:29:15.180
Student 1: If they can use that information to like.

166
00:29:16.350 --> 00:29:24.540
Student 1: kind of like track you and, like know stuff about you that you'd rather not disclose to like the public.

167
00:29:25.560 --> 00:29:29.190
Student 1: Information could easily get leaked if it's sold, so any third party.

168
00:29:29.640 --> 00:29:32.430
Sean Goggins: So, especially for example prescription drugs.

169
00:29:34.380 --> 00:29:34.830
Student 1: yeah.

170
00:29:35.040 --> 00:29:36.300
Sean Goggins: That you might be using.

171
00:29:37.380 --> 00:29:44.850
Sean Goggins: If so, if CVs, what are the other contexts that CVs could sell your information to a third party that would be okay.

172
00:29:48.720 --> 00:29:49.590
Sean Goggins: You can think of.

173
00:29:53.700 --> 00:29:54.060
Student 1: that's.

174
00:29:54.180 --> 00:30:04.620
Sean Goggins: kind of hard to say so, the one the one I can think of is if if you're asked so oftentimes on websites you're asked for consent to share information and.

175
00:30:05.580 --> 00:30:10.470
Sean Goggins: Arguably CBS could ask for consent to share information about my purchases.

176
00:30:11.040 --> 00:30:18.840
Sean Goggins: And what I would like what I think would be ethical would be to say all right i'm Okay, for example, in exchange for you, giving me extra coupons.

177
00:30:19.350 --> 00:30:30.270
Sean Goggins: If if you sell information about the mouthwash or the toothpaste, that I buy your store, but I don't want you to sell information about whatever prescription drugs.

178
00:30:32.400 --> 00:30:38.400
Sean Goggins: So there there's a case where, if you provide consent for the use of parts of your data that might be okay.

179
00:30:40.590 --> 00:30:57.540
Sean Goggins: What about this one, the next one, Edward snowden leaking classified information to the US classified US government information has generated a good deal of discussion in the face to face classes and there are essentially two perspectives.

180
00:30:59.160 --> 00:31:05.040
Sean Goggins: That dominate this discussion, but ethically and ethically morally.

181
00:31:07.470 --> 00:31:11.070
Sean Goggins: What are your thoughts on on that leak.

182
00:31:16.470 --> 00:31:20.940
Student 1: Well it's kind of like the way I look at it is it's kind of like the Roman.

183
00:31:23.760 --> 00:31:33.960
Student 1: I know this is like a weird time based kind of like the Roman civilization there's a there's some point where, if you look at something in the past, or you look back at some previous civilization.

184
00:31:34.650 --> 00:31:42.030
Student 1: there's always like instances of some level of corruption or just some instance where the civilization will just collapse or maybe it doesn't.

185
00:31:44.010 --> 00:31:55.650
Student 1: But if you look at it from the perspective that no government is like in principle to any level of corruption, then at.

186
00:31:56.430 --> 00:31:59.430
Student 1: Some point like there has to be people who.

187
00:32:00.840 --> 00:32:03.540
Student 1: Try to speak up for what they deem to be ethically.

188
00:32:04.590 --> 00:32:11.580
Student 1: wrong or correct and, in this case, Edward snowden felt that it was ethically wrong what.

189
00:32:13.050 --> 00:32:17.760
Student 1: The US Government was doing, and he decided that he wanted to disseminate that information.

190
00:32:19.830 --> 00:32:27.750
Sean Goggins: that's that's that's well well stated, I think, in the discussions that have occurred in previous classes focus on that.

191
00:32:28.350 --> 00:32:38.220
Sean Goggins: there's a there's a conflict between the code of ethics that we just discussed with regards to protecting the confidentiality of the things that we do for our employers.

192
00:32:38.880 --> 00:32:50.550
Sean Goggins: And the larger social responsibility that an individual might feel about wrongdoing that their employer is participating in or leading.

193
00:32:51.120 --> 00:33:02.520
Sean Goggins: And so, depending on your perspective if your perspective is as a Attorney General for the United States Government Edward snowden is a criminal who violated his oath.

194
00:33:03.210 --> 00:33:15.690
Sean Goggins: To the government and to his employer to hold sacred these secrets that he had access to if if you're examining it from the perspective of this long view of history.

195
00:33:16.320 --> 00:33:25.260
Sean Goggins: And the fact that the systems that he was working on and that he reveal violated several parts of the US Constitution.

196
00:33:25.830 --> 00:33:44.460
Sean Goggins: Because they were being employed on us soil against US citizens, not necessarily by design, but certainly, incidentally, then you can look at what he did as a sort of a moral imperative for him to do what he did and.

197
00:33:45.540 --> 00:33:48.180
Sean Goggins: Legally he's still a refugee.

198
00:33:49.560 --> 00:33:57.510
Sean Goggins: who cannot return to the United States without being arrested and there's ample public debate about whether what he did.

199
00:33:58.470 --> 00:34:11.850
Sean Goggins: should be punished or celebrated and I don't think we're going to land on an answer that here, but, but I think his actions reflect one of these points in time or individual was faced with a conflict between.

200
00:34:12.870 --> 00:34:14.220
Sean Goggins: The public what he.

201
00:34:14.340 --> 00:34:16.380
Sean Goggins: In this case, view this the public interest.

202
00:34:16.740 --> 00:34:19.980
Sean Goggins: and his ethical responsibilities to an employer.

203
00:34:22.530 --> 00:34:23.820
Sean Goggins: Cambridge analytica.

204
00:34:26.490 --> 00:34:38.250
Sean Goggins: Essentially, was responsible for analyzing Facebook data and sending out a bunch of messages and creating organizations and gathering information about people using social media.

205
00:34:39.540 --> 00:34:51.120
Sean Goggins: That were that explicit those people were explicitly then targeted with Facebook ads to try to influence them and their votes in an election in the United States and.

206
00:34:52.170 --> 00:35:02.520
Sean Goggins: Some of the details are the Cambridge analytica did not follow the terms of service that Facebook had laid out for using their data and so.

207
00:35:03.660 --> 00:35:11.850
Sean Goggins: Legally, they violated the terms of service to perform a data activity for for political purposes.

208
00:35:14.250 --> 00:35:24.720
Sean Goggins: Whether or not the terms of service are right is another question of debate does anyone have an opinion about that particular scandal.

209
00:35:32.700 --> 00:35:41.040
Student 1: like to believe that any piece of media should try to aim towards being like a neutral neutral party, but like.

210
00:35:43.050 --> 00:35:49.470
Student 1: Unfortunately, like most pieces of media end up being biased in one way or another, so.

211
00:35:50.790 --> 00:35:59.130
Student 1: I mean, I think it's ethically incorrect, but I could understand why other people would make the argument that like they either don't think it's a big issue or.

212
00:36:00.540 --> 00:36:05.400
Student 1: Like it's not a big thing in the scope of things so yeah I understand both sides of it.

213
00:36:05.940 --> 00:36:10.110
Sean Goggins: yeah I mean I think so it's it's it's.

214
00:36:11.940 --> 00:36:15.900
Sean Goggins: I think it's it's more than the other two a case where.

215
00:36:16.950 --> 00:36:21.720
Sean Goggins: it's very common for our ability to reason morally and ethically about technology.

216
00:36:23.070 --> 00:36:34.590
Sean Goggins: trails the development of the technology itself by 15 to 25 years so social media and the way that it influences the public's perspective on things.

217
00:36:35.100 --> 00:36:47.550
Sean Goggins: is a relatively new phenomena and honestly we don't fully understand the scope of that influence and clearly Cambridge analytica intended to manipulate public opinion.

218
00:36:47.970 --> 00:37:05.190
Sean Goggins: On purpose but we haven't worked out as a society, what about that is good and bad So you see these debates about what shouldn't should not be permitted on social media to continue, they have continued through the present day.

219
00:37:06.810 --> 00:37:17.100
Sean Goggins: You know the most recent example of a social media company taking a stand to say that you know you know you cannot use our platform for certain purposes is when.

220
00:37:17.730 --> 00:37:36.450
Sean Goggins: Former President trump's Twitter account was deleted because he according to twitter's terms of service, he used the account to incite violence in society so whether or not the Senate convicted him in his post posthumous electoral impeachment.

221
00:37:37.800 --> 00:37:49.290
Sean Goggins: Is one matter but Twitter as a company made a decision ethically using their they have a set of Community guidelines actually that are published that.

222
00:37:50.370 --> 00:37:59.520
Sean Goggins: Real Donald trump at Twitter violated, and so they deleted his account according to their terms of service and so that might be one example where.

223
00:38:00.060 --> 00:38:16.350
Sean Goggins: Some of the things that were learned by social media companies through the 2016 election are manifest going forward that that slowly or learning about the use and misuse of the technology that it's not a complete free for all.

224
00:38:19.710 --> 00:38:27.240
Sean Goggins: And then the last example our researchers at the university using analyzing posts from the Twitter community and.

225
00:38:27.960 --> 00:38:39.480
Sean Goggins: I won't extend the discussion on this one, but i'll say that what's important is respecting the terms of service that we get the data under and that we don't.

226
00:38:39.960 --> 00:38:46.620
Sean Goggins: Share individually identifying information that we would analyze the data in aggregate and talk about trends.

227
00:38:47.220 --> 00:38:58.890
Sean Goggins: But not talk about individuals in the course of conducting research on social media that that the point isn't to call out a person or a group of people.

228
00:38:59.790 --> 00:39:10.350
Sean Goggins: So much as it is to understand the dynamics of how groups or social networks of people within these technical social networks influence each other in different ways.

229
00:39:13.950 --> 00:39:21.840
Sean Goggins: So, again it's an ethical issue if it generates a question, so if you have to ask if it's right or wrong it's an ethical issue like if you pause for a minute.

230
00:39:22.470 --> 00:39:30.660
Sean Goggins: and wonder if it's right or wrong you've entered the territory where you need to follow some kind of you know, thoughtful ethical concerns.

231
00:39:34.620 --> 00:39:44.820
Sean Goggins: So another part of this is to think about data ethics, a lot of software and technology, these days, is really about the data that we have about people.

232
00:39:45.270 --> 00:39:53.190
Sean Goggins: And the amount of information about you about me about everyone that's available digitally is constantly increasing.

233
00:39:53.730 --> 00:40:06.270
Sean Goggins: As are the ways of using this data for both profit in terms of the more I engage you on a website and the more ads you see the more money, this software platform gets but also for social good so.

234
00:40:07.290 --> 00:40:14.340
Sean Goggins: gofundme campaigns or things with an explicit intent to do something positive for the world.

235
00:40:15.840 --> 00:40:22.740
Sean Goggins: The use of data for these objectives are also increasing so there's new products every day.

236
00:40:23.910 --> 00:40:27.870
Sean Goggins: Something called epic core kodiak data.

237
00:40:29.550 --> 00:40:31.080
Sean Goggins: kibo is, these are all.

238
00:40:32.340 --> 00:40:44.550
Sean Goggins: Big data tools that are used as products to analyze and make money from the data that's available online or that a platform can generate online every day and.

239
00:40:44.730 --> 00:40:46.980
Sean Goggins: So you have this persistent pressure.

240
00:40:47.340 --> 00:40:56.970
Sean Goggins: of innovation, creating unintended consequences, so the unintended consequences, then force an imbalance.

241
00:40:57.420 --> 00:41:04.230
Sean Goggins: In the innovation and each of the cases that we discussed ethically and one of the reasons that ethics.

242
00:41:04.800 --> 00:41:18.690
Sean Goggins: trail, the development of new technologies by 15 to 25 years in general is that understanding the effects social effects the ethical implications of a particular technology innovation.

243
00:41:19.230 --> 00:41:30.360
Sean Goggins: Or you know how we reason about that arises from the unintended consequences of the technology that we built and so there's this tension that goes on until we reach equilibrium and that takes some time.

244
00:41:32.910 --> 00:41:52.620
Sean Goggins: So your responsibilities regarding ethics as a software engineer really focus on decision making and so making good decisions ethical decisions in your day to day work at some stage, you might be involved in writing or enforcing policies.

245
00:41:53.670 --> 00:42:00.390
Sean Goggins: or writing or publishing and communication communicating results you're certainly going to be involved in writing code and.

246
00:42:00.960 --> 00:42:09.660
Sean Goggins: If again you have to pause and ask the question about if it's right or wrong, then you at least enter the territory of reasoning ethically about the work that you're doing.

247
00:42:10.710 --> 00:42:15.060
Sean Goggins: And you know I encourage you to be thoughtful and follow that through.

248
00:42:17.190 --> 00:42:24.780
Sean Goggins: This is a there's a case study section in this lecture which, with a small number of participants, I won't dive directly into.

249
00:42:26.040 --> 00:42:26.820
Sean Goggins: So.

250
00:42:29.400 --> 00:42:31.440
Sean Goggins: Here I would just encourage folks.

251
00:42:34.530 --> 00:42:48.570
Sean Goggins: To to read through the in bloom example on your own time and just right now i'm going to jump to the foundations of ethical decisions and stances so.

252
00:42:49.110 --> 00:43:08.010
Sean Goggins: The source of your beliefs in such cases and every person, you know you, you get to be you, you get to have your own moral code that hopefully aligns well with the ethical code that's been outlined by professional computing organizations.

253
00:43:09.090 --> 00:43:16.050
Sean Goggins: But, but your your own beliefs, are part of how you make decisions so there's these ethical standards that I referenced.

254
00:43:16.620 --> 00:43:24.270
Sean Goggins: That the ieee and acm put together there's also organizational goals and so to the extent that you are working for an organization, whose.

255
00:43:24.840 --> 00:43:32.520
Sean Goggins: goals you're morally and ethically aligned with the less likely, you are to have ethical tensions in your day to day existence.

256
00:43:33.180 --> 00:43:41.700
Sean Goggins: Your your past experience also guides how you make decisions ethically in the workplace, so if if you take a stand.

257
00:43:42.600 --> 00:43:50.430
Sean Goggins: Again, one position and you actually end up losing that job you may be less inclined to take an ethical stand in the future position.

258
00:43:50.970 --> 00:44:03.540
Sean Goggins: In a and so that's something to consider, you know how far does your ethical standard go and what are the right ways to raise the concern if you're in an organization, whose business is.

259
00:44:06.210 --> 00:44:21.180
Sean Goggins: getting old people, to give you all their money through some form of fraud you're likely to be facing ethical conundrums every day, and hopefully it's not an organization you'll want to work for any longer than you need to to feed yourself.

260
00:44:22.860 --> 00:44:28.230
Sean Goggins: And then finally lots of people in society have religious beliefs things that they're.

261
00:44:29.250 --> 00:44:32.250
Sean Goggins: Morally and ethically because of their beliefs.

262
00:44:33.360 --> 00:44:43.050
Sean Goggins: Okay, with a not okay with, and so there may be some jobs that don't align with your personal beliefs and that's okay.

263
00:44:44.190 --> 00:44:48.390
Sean Goggins: You can avoid the tension of ethical.

264
00:44:50.070 --> 00:45:02.310
Sean Goggins: quandaries by trying to not only focus on the work that you do, but focus on the mission of the organization that you join so that, to the extent possible it's aligned with something that you personally.

265
00:45:03.030 --> 00:45:14.160
Sean Goggins: Have internalized as right compared to wrong so ethics can stand for the whole computing profession and then you as an individual, have a right to inject.

266
00:45:14.610 --> 00:45:24.570
Sean Goggins: What you believe into the choices that you make mostly about whom you work for it's it's hard to have a tension between your personal beliefs and the goals of an organization.

267
00:45:26.760 --> 00:45:43.950
Sean Goggins: And so, these are the foundations of how you create your own ethical code your framework your standards there's there's laws and there's culture and there's personal beliefs and there's also the ethical standards that that that we have.

268
00:45:44.970 --> 00:45:45.840
Sean Goggins: So.

269
00:45:47.250 --> 00:45:57.600
Sean Goggins: there's there's things like the Nuremberg Code and the belmont report that look at how groups of people made.

270
00:45:58.290 --> 00:46:17.760
Sean Goggins: ethical decisions or didn't make ethical decisions in history and so these are these are things I encourage you to Google and look into because, having tension about the work that we do, and the ethical and moral codes, that we want to abide by is is not new in human history.

271
00:46:19.620 --> 00:46:33.420
Sean Goggins: there's a really good you know there's a number of these kinds of things, but the coolest Center for applied ethics at Santa Clara university is offers one framework for ethical decision making.

272
00:46:35.280 --> 00:46:46.020
Sean Goggins: Most contemporary ethical codes focus on respecting people and then balancing the risk that you pose with your technology and your software to individuals.

273
00:46:46.410 --> 00:46:56.640
Sean Goggins: Against the benefit that it has for society so there's always risk with software, but if that sometimes the social benefit is greater than that risk.

274
00:46:57.270 --> 00:47:06.360
Sean Goggins: You want to be careful about selecting the people who participate in your evaluations you want independent review of things that you propose.

275
00:47:06.840 --> 00:47:19.080
Sean Goggins: And I think this is really important that, as a profession we're self regulating that computer scientists that software developer software engineers, that we have organizations like acm ieee.

276
00:47:19.500 --> 00:47:26.640
Sean Goggins: That help us to express our professional code of ethics and that that professional code of ethics is important.

277
00:47:27.060 --> 00:47:38.850
Sean Goggins: To the work that we do important to the decision making, that we undertake in our jobs that it can by professionalising as a group of people who do highly technical work.

278
00:47:39.360 --> 00:47:53.790
Sean Goggins: We have more power to assert morality and ethics into the jobs that we do, then, if there's not a shared sort of ethical code, like the CEO and I Tripoli have developed and then.

279
00:47:54.690 --> 00:48:04.620
Sean Goggins: Making funding dependent on the adherence to ethical standards is is you know if capital follows ethics, we do better.

280
00:48:06.810 --> 00:48:19.140
Sean Goggins: And then the wrap up is that suffer engineering is an evolving field everything's happening really fast all the time, the technologies that we used in this class five years ago, are not the same as they are today.

281
00:48:19.950 --> 00:48:33.450
Sean Goggins: we're often faced with ambiguous situations, because what we do for a living what software development is is not unlike mechanical engineering or civil engineering.

282
00:48:34.050 --> 00:48:43.710
Sean Goggins: Which are constrained by the physical limits of the universe software engineering is is constrained only by the human imagination and so we are often in.

283
00:48:44.610 --> 00:48:57.090
Sean Goggins: Much more ambiguous situations than other kinds of engineers and because of that, having policies regulations and frameworks can help us to make decisions as we encounter each of these.

284
00:48:58.290 --> 00:49:00.480
Sean Goggins: Subsequent ambiguous situations.

285
00:49:01.500 --> 00:49:05.820
Sean Goggins: And ultimately, a lot is going to end up getting decided by the judicial system.

286
00:49:06.780 --> 00:49:16.680
Sean Goggins: That laws as as our ability to reason about technologies, moral and ethical impact on society coalesces.

287
00:49:17.100 --> 00:49:26.940
Sean Goggins: Over the course of the next decade or two we're going to see more clarity and the laws that exist about technology we're already starting to see it.

288
00:49:27.360 --> 00:49:38.580
Sean Goggins: With the gdpr in Europe, which is a standard for essentially you own the data about you so Facebook can collect all the data they want, but you have the right to be forgotten.

289
00:49:38.940 --> 00:49:52.560
Sean Goggins: which compels Facebook legally in Europe to delete all of your history from its databases, there are similar laws that will go into effect in California, I think, in the next 18 months and so.

290
00:49:53.310 --> 00:50:07.950
Sean Goggins: As we learn about the effects of storing data through software, there are laws that are emerging that are codified rules that then we will be compelled to follow as as technologists as software engineers.

291
00:50:09.720 --> 00:50:14.130
Sean Goggins: And that concludes the lecture portion of today's discussion.

292
00:50:15.150 --> 00:50:20.370
Sean Goggins: I would be happy to take any questions or continue any discussion that anyone wants to.

293
00:50:23.250 --> 00:50:28.770
Sean Goggins: And I can stop recording now or not, would you like me and stop recording.

294
00:50:32.040 --> 00:50:37.230
Sean Goggins: i'll stop recording because any questions you have may or may not be something that you want shared so.

